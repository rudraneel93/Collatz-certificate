# CertLang Language Specification

## Overview

CertLang is a declarative domain-specific language for mathematical certificate verification. It provides constructs for defining rational numbers, bounds, inequalities, and verification conditions.

## Grammar (EBNF)

```ebnf
Program       ::= Statement*
Statement     ::= Definition | Verification | Import
Definition    ::= "define" Identifier ":" Type "=" Expression
Verification  ::= "verify" Expression
Import        ::= "import" StringLiteral

Type          ::= "rational" | "natural" | "integer" | "bound" | "interval"
Expression    ::= BinaryOp | UnaryOp | Literal | Identifier | FunctionCall
BinaryOp      ::= Expression ("+" | "-" | "*" | "/" | "<=" | ">=" | "==" | "<" | ">") Expression
UnaryOp       ::= ("-" | "abs") Expression
Literal       ::= RationalLit | NaturalLit | IntegerLit
RationalLit   ::= IntegerLit "/" NaturalLit
NaturalLit    ::= Digit+
IntegerLit    ::= ["-"] NaturalLit
FunctionCall  ::= Identifier "(" (Expression ("," Expression)*)? ")"

Identifier    ::= Letter (Letter | Digit | "_")*
StringLiteral ::= "\"" ([^"\\] | EscapeSeq)* "\""
EscapeSeq     ::= "\\" ("n" | "t" | "r" | "\\" | "\"")
Letter        ::= [a-zA-Z]
Digit         ::= [0-9]
```

## Semantic Rules

1. All rational arithmetic is exact (no floating-point approximation)
2. Division by zero is a compile-time error
3. Type checking is static and strict
4. Variables must be defined before use
5. Verification statements evaluate to boolean and must be true for the program to succeed

## Built-in Functions

- `abs(x)` - absolute value
- `max(x, y)` - maximum of two values
- `min(x, y)` - minimum of two values
- `interval(lower, upper)` - create an interval bound
- `width(interval)` - width of an interval

## Example

```certlang
define pi_approx: rational = 22/7
define epsilon: rational = 1/1000

verify abs(pi_approx - 314159/100000) <= epsilon
```