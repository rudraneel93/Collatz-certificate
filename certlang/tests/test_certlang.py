#!/usr/bin/env python3
"""
Test suite for CertLang interpreter.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'interpreter'))

from certlang_interpreter import run_certlang, Lexer, Parser, Interpreter, CertLangError

def test_basic_arithmetic():
    """Test basic arithmetic operations."""
    code = """
    define a: rational = 1/2
    define b: rational = 1/3
    define sum: rational = a + b
    verify sum == 5/6
    """
    assert run_certlang(code), "Basic arithmetic test failed"
    print("✓ Basic arithmetic test passed")

def test_comparisons():
    """Test comparison operations."""
    code = """
    define x: rational = 3/4
    define y: rational = 2/3
    verify x > y
    verify y < x
    verify x >= y
    verify y <= x
    verify x != y
    """
    assert run_certlang(code), "Comparison test failed"
    print("✓ Comparison test passed")

def test_functions():
    """Test built-in functions."""
    code = """
    define neg: rational = -5/3
    verify abs(neg) == 5/3
    verify max(1/2, 3/4) == 3/4
    verify min(1/2, 3/4) == 1/2
    """
    assert run_certlang(code), "Functions test failed"
    print("✓ Functions test passed")

def test_intervals():
    """Test interval operations."""
    code = """
    define iv: interval = interval(1/3, 2/3)
    verify width(iv) == 1/3
    """
    assert run_certlang(code), "Intervals test failed"
    print("✓ Intervals test passed")

def test_complex_expression():
    """Test complex mathematical expressions."""
    code = """
    define x: rational = 2/3
    define result: rational = (x + 1/6) * 3/2 - 1/4
    verify result == 1/1
    """
    assert run_certlang(code), "Complex expression test failed"
    print("✓ Complex expression test passed")

def test_error_cases():
    """Test error handling."""
    # Division by zero
    code = """
    define zero: rational = 0/1
    define bad: rational = 1/1 / zero
    """
    assert not run_certlang(code), "Division by zero should fail"
    print("✓ Division by zero test passed")
    
    # Invalid interval
    code = """
    define bad_iv: interval = interval(2/3, 1/3)
    """
    assert not run_certlang(code), "Invalid interval should fail"
    print("✓ Invalid interval test passed")

def test_lexer():
    """Test lexer functionality."""
    lexer = Lexer("define x: rational = 1/2")
    tokens = lexer.tokenize()
    expected_types = ['DEFINE', 'IDENTIFIER', 'COLON', 'RATIONAL', 'ASSIGN', 'RATIONAL_LIT']
    actual_types = [token.type for token in tokens]
    assert actual_types == expected_types, f"Expected {expected_types}, got {actual_types}"
    print("✓ Lexer test passed")

def test_parser():
    """Test parser functionality."""
    lexer = Lexer("define x: rational = 1/2\nverify x > 0")
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    statements = parser.parse()
    assert len(statements) == 2, f"Expected 2 statements, got {len(statements)}"
    assert statements[0]['type'] == 'definition'
    assert statements[1]['type'] == 'verification'
    print("✓ Parser test passed")

def run_all_tests():
    """Run all tests."""
    print("Running CertLang test suite...")
    print()
    
    try:
        test_lexer()
        test_parser()
        test_basic_arithmetic()
        test_comparisons()
        test_functions()
        test_intervals()
        test_complex_expression()
        test_error_cases()
        
        print()
        print("🎉 All tests passed!")
        return True
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)