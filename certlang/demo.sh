#!/bin/bash

# CertLang Demonstration Script
# This script demonstrates the key features of the CertLang language

echo "🔬 CertLang - Mathematical Certificate Verification Language"
echo "=========================================================="
echo ""

echo "📊 Running basic mathematical verification..."
cd /home/runner/work/Collatz-certificate/Collatz-certificate/certlang
python3 interpreter/certlang_interpreter.py examples/basic_math.cl
echo ""

echo "🧮 Running numerical analysis verification..."
python3 interpreter/certlang_interpreter.py examples/numerical_analysis.cl
echo ""

echo "🔢 Running Collatz certificate verification..."
python3 interpreter/certlang_interpreter.py examples/collatz_cert.cl
echo ""

echo "🧪 Running full test suite..."
python3 tests/test_certlang.py
echo ""

echo "📈 Language Statistics:"
echo "- Lines of interpreter code: $(wc -l interpreter/certlang_interpreter.py | awk '{print $1}')"
echo "- Lines of documentation: $(wc -l docs/certlang_book.md | awk '{print $1}')"
echo "- Number of example programs: $(ls examples/*.cl | wc -l)"
echo "- Number of test cases: $(grep -c 'def test_' tests/test_certlang.py)"
echo ""

echo "📖 Documentation available at: docs/certlang_book.md"
echo "✨ CertLang demonstration complete!"