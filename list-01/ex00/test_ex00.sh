#!/bin/bash

# Script de teste para ex00
# Execute com: bash test_ex00.sh

echo "=== Testando ex00 - Hello.py ==="
echo ""

echo "Output do seu programa:"
python3 Hello.py | cat -e
echo ""

echo "Output esperado (exemplo):"
echo "['Hello', 'World!']$"
echo "('Hello', 'France!')$"
echo "{'Hello', 'Paris!'}$"
echo "{'Hello': '42Paris!'}$"
echo ""

echo "Verificando norma:"
flake8 Hello.py
if [ $? -eq 0 ]; then
    echo "✅ Norma OK!"
else
    echo "❌ Erros de norma encontrados"
fi
