# 🐍 Python Piscine for Data Science - Module 0 (Starting)

## 📖 Descrição
Este é o módulo inicial da Piscine Python da 42, focado em aprender os fundamentos da linguagem Python.

## ⚙️ Configuração do Ambiente

### Requisitos
- ✅ Python 3.10 (instalado)
- ✅ flake8 (instalado)
- ✅ Alias `norminette` configurado

### Verificar instalação
```bash
python3 --version  # Deve mostrar Python 3.10.x
norminette --version  # Deve funcionar (alias para flake8)
```

## 📋 Lista de Exercícios

### ✅ **ex00** - First Python Script
- **Arquivo**: `Hello.py`
- **Objetivo**: Modificar estruturas de dados (list, tuple, set, dict)
- **Output esperado**: Saudações formatadas

### ✅ **ex01** - First Use of Package  
- **Arquivo**: `format_ft_time.py`
- **Objetivo**: Formatar datas usando bibliotecas time/datetime
- **Bibliotecas**: time, datetime

### ✅ **ex02** - First Function Python
- **Arquivo**: `find_ft_type.py`
- **Objetivo**: Criar função que identifica tipos de objetos
- **Protótipo**: `def all_thing_is_obj(object: any) -> int:`

### ✅ **ex03** - NULL not Found
- **Arquivo**: `NULL_not_found.py`
- **Objetivo**: Identificar e exibir tipos "Null" em Python
- **Protótipo**: `def NULL_not_found(object: any) -> int:`

### ✅ **ex04** - The Even and the Odd
- **Arquivo**: `whatis.py`
- **Objetivo**: Verificar se número é par ou ímpar (com argumentos sys)
- **Bibliotecas**: sys

### ⚠️ **A partir do ex05**: Regras adicionais aplicadas!
- ❌ Sem código no escopo global
- ✅ Usar funções com main
- ✅ Todas as funções devem ter documentação (__doc__)
- ✅ Tratar todas as exceções

### ✅ **ex05** - First Standalone Program
- **Arquivo**: `building.py`
- **Objetivo**: Contar tipos de caracteres em string
- **Bibliotecas**: sys

### ✅ **ex06** - Filter (2 partes)
- **Arquivos**: `ft_filter.py`, `filterstring.py`
- **Parte 1**: Recriar função filter() usando list comprehensions
- **Parte 2**: Filtrar palavras por tamanho usando lambda
- **Bibliotecas**: sys

### ✅ **ex07** - Dictionaries SoS
- **Arquivo**: `sos.py`
- **Objetivo**: Codificar texto em Código Morse
- **Estrutura**: Usar dicionário para armazenar código Morse
- **Bibliotecas**: sys

### ✅ **ex08** - Loading...
- **Arquivo**: `Loading.py`
- **Objetivo**: Recriar função tqdm (barra de progresso)
- **Protótipo**: `def ft_tqdm(lst: range) -> None:`
- **Bibliotecas**: os

### ✅ **ex09** - My First Package Creation
- **Arquivos**: Múltiplos (*.py, *.txt, *.toml, README.md, LICENSE)
- **Objetivo**: Criar pacote Python instalável via pip
- **Bibliotecas**: PyPI

## 📏 Regras Gerais

### ✅ Sempre seguir
```bash
# Verificar código com norminette (flake8)
norminette seu_arquivo.py

# Estrutura padrão de programa (a partir do ex05)
def main():
    # seu código aqui
    pass

if __name__ == "__main__":
    main()
```

### ❌ Proibido
- Código no escopo global (a partir do ex05)
- Imports não explícitos (ex: `from pandas import *`)
- Variáveis globais
- Usar função filter() no ex06
- Exceções não tratadas

### 📝 Documentação obrigatória
```python
def minha_funcao():
    """
    Esta função faz algo incrível.
    """
    pass
```

## 🚀 Como Começar

1. **Comece pelo ex00** e vá progredindo
2. **Leia o enunciado** de cada exercício com atenção
3. **Teste seu código** antes de submeter
4. **Verifique a norma** com `norminette arquivo.py`

## 📦 Submissão
- Submeter via Git repository
- Apenas o conteúdo do repositório será avaliado
- Verificar nomes de pastas e arquivos

## 🎯 Dicas

- 💡 Use as funções built-in do Python quando permitido
- 💡 Teste com diferentes inputs
- 💡 Leia a documentação do Python
- 💡 Use `python3 --help` para entender argumentos
- 💡 Não reinvente a roda - use recursos da linguagem!

---

**Boa sorte! 🚀 By Odin, by Thor! Use your brain!!!**
