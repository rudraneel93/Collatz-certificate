# CollatzScript Language Specification

## Overview

CollatzScript is a domain-specific language designed for mathematical verification and computational proof systems, particularly optimized for problems involving number theory, sequences, and mathematical conjectures like the Collatz conjecture.

## Language Philosophy

CollatzScript bridges the gap between formal proof assistants (like Lean and Coq) and accessible mathematical notation. It provides:

1. **Human-readable syntax** for mathematical expressions
2. **Built-in support** for rational arithmetic and interval analysis
3. **Verification primitives** for mathematical proofs
4. **Certificate checking** capabilities for computational mathematics

## Syntax and Grammar

### Basic Types

```
Number Types:
  rational ::= numerator '/' denominator | integer
  interval ::= '[' rational ',' rational ']'
  natural  ::= positive_integer

Basic Types:
  bool     ::= 'true' | 'false'
  string   ::= '"' [^"]* '"'
```

### Declarations

```
Constant Declaration:
  'const' identifier ':' type '=' expression ';'

Variable Declaration:
  'var' identifier ':' type ';'

Function Declaration:
  'function' identifier '(' params ')' ':' return_type '{' statements '}'

Theorem Declaration:
  'theorem' identifier ':' proposition '{' proof '}'
```

### Expressions

```
Arithmetic:
  expression ::= term (('+' | '-') term)*
  term       ::= factor (('*' | '/') factor)*
  factor     ::= number | identifier | '(' expression ')'

Comparison:
  comparison ::= expression ('<=' | '>=' | '<' | '>' | '==' | '!=') expression

Logical:
  logical ::= comparison (('&&' | '||') comparison)*
```

### Statements

```
Assignment:
  identifier '=' expression ';'

Conditional:
  'if' '(' expression ')' '{' statements '}' ('else' '{' statements '}')?

Loop:
  'for' identifier 'in' range '{' statements '}'
  'while' '(' expression ')' '{' statements '}'

Assertion:
  'assert' expression ';'
  'verify' expression ';'
```

### Proof Language

```
Proof Steps:
  'by' proof_tactic
  'calc' calculation_chain
  'cases' expression
  'induction' identifier

Proof Tactics:
  'norm_num'           // Numerical normalization
  'interval_check'     // Interval arithmetic verification
  'rational_arith'     // Rational arithmetic simplification
  'assumption'         // Use assumption from context
```

## Built-in Functions

### Mathematical Functions

- `abs(x)` - Absolute value
- `min(x, y)` - Minimum of two values
- `max(x, y)` - Maximum of two values
- `gcd(a, b)` - Greatest common divisor
- `lcm(a, b)` - Least common multiple

### Verification Functions

- `check_interval(value, lower, upper)` - Verify value is in interval
- `verify_bound(expr, bound)` - Verify expression satisfies bound
- `prove_inequality(left, right)` - Prove left <= right
- `certificate_check(cert)` - Validate mathematical certificate

### Sequence Functions

- `sequence(n -> expr)` - Define sequence by formula
- `iterate(f, x0, n)` - Apply function f to x0 n times
- `converges(seq, limit)` - Check if sequence converges

## Standard Library Modules

### `rational` module
- High-precision rational arithmetic
- Interval arithmetic operations
- Continued fraction expansions

### `verification` module
- Proof automation tools
- Certificate validation
- Error bound calculations

### `sequences` module
- Sequence analysis tools
- Convergence testing
- Pattern detection

## Example Programs

### Simple Rational Arithmetic
```collatzscript
const pi_approx : rational = 22/7;
const error_bound : rational = 1/1000;

theorem pi_approximation_bound : 
  abs(pi_approx - pi) <= error_bound {
  by interval_check;
}
```

### Collatz Function Definition
```collatzscript
function collatz_step(n : natural) : natural {
  if (n % 2 == 0) {
    return n / 2;
  } else {
    return 3 * n + 1;
  }
}

function stopping_time(n : natural) : natural {
  var steps : natural = 0;
  var current : natural = n;
  
  while (current != 1) {
    current = collatz_step(current);
    steps = steps + 1;
  }
  
  return steps;
}
```

## Error Handling

CollatzScript includes comprehensive error handling:

- **Type errors** - Compile-time type checking
- **Arithmetic errors** - Division by zero, overflow detection
- **Proof errors** - Failed verification attempts
- **Runtime errors** - Assertion failures, infinite loops

## Compilation and Execution

CollatzScript programs can be:

1. **Interpreted** for rapid prototyping
2. **Compiled** to efficient bytecode
3. **Transpiled** to Lean/Coq for formal verification
4. **Validated** through built-in proof checking

## Future Extensions

Planned features include:

- Integration with computer algebra systems
- Parallel computation support
- Machine learning integration for proof search
- Enhanced visualization capabilities
- Export to academic paper formats