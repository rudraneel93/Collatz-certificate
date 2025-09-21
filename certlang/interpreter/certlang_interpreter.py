#!/usr/bin/env python3
"""
CertLang Interpreter - A simple interpreter for the CertLang mathematical certificate verification language.

This interpreter supports:
- Exact rational arithmetic using Python's fractions.Fraction
- Variable definitions and references
- Basic arithmetic operations
- Comparison operations
- Verification statements
- Built-in functions (abs, max, min, interval, width)
"""

import sys
import re
from fractions import Fraction
from typing import Dict, Any, Union, List, Tuple

class CertLangError(Exception):
    """Base exception for CertLang errors."""
    pass

class ParseError(CertLangError):
    """Raised when parsing fails."""
    pass

class RuntimeError(CertLangError):
    """Raised during execution."""
    pass

class Interval:
    """Represents a mathematical interval [lower, upper]."""
    def __init__(self, lower: Fraction, upper: Fraction):
        if lower > upper:
            raise RuntimeError(f"Invalid interval: lower bound {lower} > upper bound {upper}")
        self.lower = lower
        self.upper = upper
    
    def width(self) -> Fraction:
        return self.upper - self.lower
    
    def __str__(self):
        return f"[{self.lower}, {self.upper}]"

class Token:
    def __init__(self, type_: str, value: str, line: int, column: int):
        self.type = type_
        self.value = value
        self.line = line
        self.column = column
    
    def __repr__(self):
        return f"Token({self.type}, {self.value!r}, {self.line}:{self.column})"

class Lexer:
    """Tokenizes CertLang source code."""
    
    TOKEN_PATTERNS = [
        ('COMMENT', r'#.*'),
        ('WHITESPACE', r'\s+'),
        ('DEFINE', r'\bdefine\b'),
        ('VERIFY', r'\bverify\b'),
        ('IMPORT', r'\bimport\b'),
        ('RATIONAL', r'\brational\b'),
        ('NATURAL', r'\bnatural\b'),
        ('INTEGER', r'\binteger\b'),
        ('BOUND', r'\bbound\b'),
        ('INTERVAL', r'\binterval\b'),
        ('ABS', r'\babs\b'),
        ('MAX', r'\bmax\b'),
        ('MIN', r'\bmin\b'),
        ('WIDTH', r'\bwidth\b'),
        ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),
        ('RATIONAL_LIT', r'-?\d+/\d+'),
        ('INTEGER_LIT', r'-?\d+'),
        ('STRING_LIT', r'"([^"\\]|\\.)*"'),
        ('LE', r'<='),
        ('GE', r'>='),
        ('EQ', r'=='),
        ('NE', r'!='),
        ('LT', r'<'),
        ('GT', r'>'),
        ('ASSIGN', r'='),
        ('PLUS', r'\+'),
        ('MINUS', r'-'),
        ('MULTIPLY', r'\*'),
        ('DIVIDE', r'/'),
        ('LPAREN', r'\('),
        ('RPAREN', r'\)'),
        ('COLON', r':'),
        ('COMMA', r','),
        ('NEWLINE', r'\n'),
    ]
    
    def __init__(self, text: str):
        self.text = text
        self.pos = 0
        self.line = 1
        self.column = 1
        self.tokens = []
    
    def tokenize(self) -> List[Token]:
        while self.pos < len(self.text):
            matched = False
            for token_type, pattern in self.TOKEN_PATTERNS:
                regex = re.compile(pattern)
                match = regex.match(self.text, self.pos)
                if match:
                    value = match.group(0)
                    if token_type not in ['COMMENT', 'WHITESPACE']:
                        self.tokens.append(Token(token_type, value, self.line, self.column))
                    
                    # Update position and line/column tracking
                    self.pos = match.end()
                    if token_type == 'NEWLINE':
                        self.line += 1
                        self.column = 1
                    else:
                        self.column += len(value)
                    matched = True
                    break
            
            if not matched:
                raise ParseError(f"Unexpected character '{self.text[self.pos]}' at line {self.line}, column {self.column}")
        
        return self.tokens

class Parser:
    """Parses CertLang tokens into an AST."""
    
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.pos = 0
    
    def current_token(self) -> Token:
        if self.pos >= len(self.tokens):
            return Token('EOF', '', -1, -1)
        return self.tokens[self.pos]
    
    def consume(self, expected_type: str = None) -> Token:
        token = self.current_token()
        if expected_type and token.type != expected_type:
            raise ParseError(f"Expected {expected_type}, got {token.type} at line {token.line}")
        self.pos += 1
        return token
    
    def parse(self) -> List[Dict[str, Any]]:
        statements = []
        while self.current_token().type != 'EOF':
            stmt = self.parse_statement()
            if stmt:
                statements.append(stmt)
        return statements
    
    def parse_statement(self) -> Dict[str, Any]:
        token = self.current_token()
        
        if token.type == 'DEFINE':
            return self.parse_definition()
        elif token.type == 'VERIFY':
            return self.parse_verification()
        elif token.type == 'IMPORT':
            return self.parse_import()
        elif token.type == 'NEWLINE':
            self.consume('NEWLINE')
            return None
        else:
            raise ParseError(f"Unexpected token {token.type} at line {token.line}")
    
    def parse_definition(self) -> Dict[str, Any]:
        self.consume('DEFINE')
        name = self.consume('IDENTIFIER').value
        self.consume('COLON')
        type_name = self.consume().value  # type
        self.consume('ASSIGN')
        expr = self.parse_expression()
        return {'type': 'definition', 'name': name, 'data_type': type_name, 'expression': expr}
    
    def parse_verification(self) -> Dict[str, Any]:
        self.consume('VERIFY')
        expr = self.parse_expression()
        return {'type': 'verification', 'expression': expr}
    
    def parse_import(self) -> Dict[str, Any]:
        self.consume('IMPORT')
        path = self.consume('STRING_LIT').value[1:-1]  # Remove quotes
        return {'type': 'import', 'path': path}
    
    def parse_expression(self) -> Dict[str, Any]:
        return self.parse_comparison()
    
    def parse_comparison(self) -> Dict[str, Any]:
        left = self.parse_arithmetic()
        
        token = self.current_token()
        if token.type in ['LE', 'GE', 'EQ', 'NE', 'LT', 'GT']:
            op = self.consume().type
            right = self.parse_arithmetic()
            return {'type': 'binary_op', 'operator': op, 'left': left, 'right': right}
        
        return left
    
    def parse_arithmetic(self) -> Dict[str, Any]:
        left = self.parse_term()
        
        while self.current_token().type in ['PLUS', 'MINUS']:
            op = self.consume().type
            right = self.parse_term()
            left = {'type': 'binary_op', 'operator': op, 'left': left, 'right': right}
        
        return left
    
    def parse_term(self) -> Dict[str, Any]:
        left = self.parse_factor()
        
        while self.current_token().type in ['MULTIPLY', 'DIVIDE']:
            op = self.consume().type
            right = self.parse_factor()
            left = {'type': 'binary_op', 'operator': op, 'left': left, 'right': right}
        
        return left
    
    def parse_factor(self) -> Dict[str, Any]:
        token = self.current_token()
        
        if token.type == 'MINUS':
            self.consume('MINUS')
            expr = self.parse_factor()
            return {'type': 'unary_op', 'operator': 'MINUS', 'operand': expr}
        elif token.type == 'LPAREN':
            self.consume('LPAREN')
            expr = self.parse_expression()
            self.consume('RPAREN')
            return expr
        elif token.type == 'RATIONAL_LIT':
            value = self.consume('RATIONAL_LIT').value
            return {'type': 'literal', 'value': value, 'data_type': 'rational'}
        elif token.type == 'INTEGER_LIT':
            value = self.consume('INTEGER_LIT').value
            return {'type': 'literal', 'value': value, 'data_type': 'integer'}
        elif token.type == 'IDENTIFIER':
            name = self.consume('IDENTIFIER').value
            if self.current_token().type == 'LPAREN':
                return self.parse_function_call(name)
            else:
                return {'type': 'identifier', 'name': name}
        elif token.type in ['ABS', 'MAX', 'MIN', 'WIDTH', 'INTERVAL']:
            func_name = self.consume().value
            return self.parse_function_call(func_name)
        else:
            raise ParseError(f"Unexpected token {token.type} at line {token.line}")
    
    def parse_function_call(self, name: str) -> Dict[str, Any]:
        self.consume('LPAREN')
        args = []
        
        if self.current_token().type != 'RPAREN':
            args.append(self.parse_expression())
            while self.current_token().type == 'COMMA':
                self.consume('COMMA')
                args.append(self.parse_expression())
        
        self.consume('RPAREN')
        return {'type': 'function_call', 'name': name, 'arguments': args}

class Interpreter:
    """Executes CertLang programs."""
    
    def __init__(self):
        self.variables: Dict[str, Any] = {}
        self.verification_results: List[bool] = []
    
    def interpret(self, statements: List[Dict[str, Any]]) -> bool:
        """Execute a list of statements and return True if all verifications pass."""
        for stmt in statements:
            if stmt['type'] == 'definition':
                self.execute_definition(stmt)
            elif stmt['type'] == 'verification':
                result = self.execute_verification(stmt)
                self.verification_results.append(result)
            elif stmt['type'] == 'import':
                self.execute_import(stmt)
        
        return all(self.verification_results)
    
    def execute_definition(self, stmt: Dict[str, Any]):
        name = stmt['name']
        value = self.evaluate_expression(stmt['expression'])
        self.variables[name] = value
    
    def execute_verification(self, stmt: Dict[str, Any]) -> bool:
        result = self.evaluate_expression(stmt['expression'])
        if not isinstance(result, bool):
            raise RuntimeError(f"Verification expression must evaluate to boolean, got {type(result)}")
        print(f"Verification: {result}")
        return result
    
    def execute_import(self, stmt: Dict[str, Any]):
        # For now, imports are not implemented
        print(f"Import: {stmt['path']} (not implemented)")
    
    def evaluate_expression(self, expr: Dict[str, Any]) -> Any:
        if expr['type'] == 'literal':
            if expr['data_type'] == 'rational':
                return Fraction(expr['value'])
            elif expr['data_type'] == 'integer':
                return Fraction(int(expr['value']))
        elif expr['type'] == 'identifier':
            name = expr['name']
            if name not in self.variables:
                raise RuntimeError(f"Undefined variable: {name}")
            return self.variables[name]
        elif expr['type'] == 'binary_op':
            left = self.evaluate_expression(expr['left'])
            right = self.evaluate_expression(expr['right'])
            return self.apply_binary_operator(expr['operator'], left, right)
        elif expr['type'] == 'unary_op':
            operand = self.evaluate_expression(expr['operand'])
            return self.apply_unary_operator(expr['operator'], operand)
        elif expr['type'] == 'function_call':
            args = [self.evaluate_expression(arg) for arg in expr['arguments']]
            return self.call_function(expr['name'], args)
        else:
            raise RuntimeError(f"Unknown expression type: {expr['type']}")
    
    def apply_binary_operator(self, op: str, left: Any, right: Any) -> Any:
        if op == 'PLUS':
            return left + right
        elif op == 'MINUS':
            return left - right
        elif op == 'MULTIPLY':
            return left * right
        elif op == 'DIVIDE':
            if right == 0:
                raise RuntimeError("Division by zero")
            return left / right
        elif op == 'LE':
            return left <= right
        elif op == 'GE':
            return left >= right
        elif op == 'EQ':
            return left == right
        elif op == 'NE':
            return left != right
        elif op == 'LT':
            return left < right
        elif op == 'GT':
            return left > right
        else:
            raise RuntimeError(f"Unknown binary operator: {op}")
    
    def apply_unary_operator(self, op: str, operand: Any) -> Any:
        if op == 'MINUS':
            return -operand
        else:
            raise RuntimeError(f"Unknown unary operator: {op}")
    
    def call_function(self, name: str, args: List[Any]) -> Any:
        if name == 'abs':
            if len(args) != 1:
                raise RuntimeError(f"abs() takes exactly 1 argument ({len(args)} given)")
            return abs(args[0])
        elif name == 'max':
            if len(args) != 2:
                raise RuntimeError(f"max() takes exactly 2 arguments ({len(args)} given)")
            return max(args[0], args[1])
        elif name == 'min':
            if len(args) != 2:
                raise RuntimeError(f"min() takes exactly 2 arguments ({len(args)} given)")
            return min(args[0], args[1])
        elif name == 'interval':
            if len(args) != 2:
                raise RuntimeError(f"interval() takes exactly 2 arguments ({len(args)} given)")
            return Interval(args[0], args[1])
        elif name == 'width':
            if len(args) != 1:
                raise RuntimeError(f"width() takes exactly 1 argument ({len(args)} given)")
            if not isinstance(args[0], Interval):
                raise RuntimeError(f"width() requires an interval argument")
            return args[0].width()
        else:
            raise RuntimeError(f"Unknown function: {name}")

def run_certlang(source_code: str) -> bool:
    """Run CertLang source code and return True if all verifications pass."""
    try:
        lexer = Lexer(source_code)
        tokens = lexer.tokenize()
        
        parser = Parser(tokens)
        statements = parser.parse()
        
        interpreter = Interpreter()
        return interpreter.interpret(statements)
    except CertLangError as e:
        print(f"Error: {e}")
        return False

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 certlang_interpreter.py <file.cl>")
        sys.exit(1)
    
    filename = sys.argv[1]
    try:
        with open(filename, 'r') as f:
            source_code = f.read()
        
        success = run_certlang(source_code)
        if success:
            print("All verifications passed!")
            sys.exit(0)
        else:
            print("Some verifications failed!")
            sys.exit(1)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()