# 🛠️ Comandos Úteis - Python Piscine

## Verificação e Testes

### Verificar norma (flake8)
```bash
norminette arquivo.py
# ou
~/.local/bin/flake8 arquivo.py
```

### Executar programa Python
```bash
python3 arquivo.py
python3 arquivo.py argumento1 argumento2
```

### Testar com cat -e (ver caracteres invisíveis)
```bash
python3 arquivo.py | cat -e
```

### Verificar versão do Python
```bash
python3 --version
```

## Trabalhando com Argumentos (sys)

### Ex04, Ex05, Ex06, Ex07
```python
import sys

# Número de argumentos (incluindo nome do script)
len(sys.argv)

# Primeiro argumento (nome do script)
sys.argv[0]

# Segundo argumento (primeiro parâmetro)
sys.argv[1]

# Todos os argumentos exceto o nome do script
sys.argv[1:]
```

## Bibliotecas Comuns

### time e datetime (ex01)
```python
import time
import datetime

# Segundos desde 1970
time.time()

# Data formatada
datetime.datetime.now().strftime("%b %d %Y")
```

### string (para constantes úteis)
```python
import string

string.ascii_uppercase  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
string.digits           # '0123456789'
string.punctuation      # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
```

## Dicas de Python

### Type checking
```python
type(objeto)            # Retorna o tipo
isinstance(obj, tipo)   # Verifica se é de um tipo
```

### List comprehensions (ex06)
```python
# Filtrar elementos
[x for x in lista if condicao]

# Com lambda
list(filter(lambda x: condicao, lista))
```

### Dicionários (ex07)
```python
meu_dict = {
    "chave1": "valor1",
    "chave2": "valor2"
}

# Acessar valor
meu_dict["chave1"]

# Verificar se chave existe
if "chave1" in meu_dict:
    pass
```

### Yield (ex08)
```python
def meu_gerador():
    for i in range(10):
        yield i  # Retorna valor mas mantém estado

# Usar gerador
for valor in meu_gerador():
    print(valor)
```

## Tratamento de Exceções

### Lançar AssertionError
```python
# Método 1
assert condicao, "mensagem de erro"

# Método 2
if not condicao:
    raise AssertionError("mensagem de erro")
```

### Try-except
```python
try:
    # código que pode gerar erro
    valor = int(input())
except ValueError:
    print("Erro: não é um número")
except Exception as e:
    print(f"Erro inesperado: {e}")
```

## Ferramentas de Debug

### Print de debug
```python
print(f"Valor: {variavel}")
print(f"Tipo: {type(variavel)}")
print(f"Tamanho: {len(variavel)}")
```

### Verificar documentação
```python
print(funcao.__doc__)
help(funcao)
```

## Git (Submissão)

### Comandos básicos
```bash
# Ver status
git status

# Adicionar arquivos
git add ex00/Hello.py
git add .

# Commit
git commit -m "feat: add ex00"

# Push
git push
```

### Estrutura de commit (recomendado)
```
feat: add ex00 - first python script
feat: add ex01 - date formatting
fix: correct ex02 type checking
docs: update README
```

## Package Installation (ex09)

### Criar estrutura de pacote
```bash
# Estrutura mínima
ft_package/
├── ft_package/
│   ├── __init__.py
│   └── modulo.py
├── setup.py (ou pyproject.toml)
├── README.md
└── LICENSE
```

### Build e install
```bash
# Build
python3 -m build

# Install
pip3 install ./dist/ft_package-0.0.1.tar.gz
pip3 install ./dist/ft_package-0.0.1-py3-none-any.whl

# Verificar
pip3 list
pip3 show -v ft_package

# Desinstalar
pip3 uninstall ft_package
```

## Atalhos úteis no terminal

```bash
# Limpar terminal
clear
# ou
Ctrl + L

# Cancelar comando
Ctrl + C

# EOF (End of File) - útil para input
Ctrl + D

# Histórico de comandos
↑ (seta para cima)
history
```

---

**💡 Dica**: Mantenha este arquivo aberto enquanto trabalha nos exercícios!
