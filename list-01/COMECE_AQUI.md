# 🚀 GUIA DE INÍCIO RÁPIDO

## ✅ Ambiente Configurado!

Você já tem tudo pronto para começar:
- ✅ Python 3.10.12 instalado
- ✅ flake8 (norminette) configurado
- ✅ Estrutura de pastas criada (ex00 até ex09)
- ✅ Templates e exemplos prontos

## 📁 Estrutura Atual

```
piscine/
├── README.md                 # Documentação completa do projeto
├── COMANDOS_UTEIS.md        # Comandos e dicas úteis
├── template_example.py       # Template para estrutura de código
├── en.subject.pdf           # PDF original do projeto
├── ex00/                    # ⭐ COMECE AQUI!
│   ├── Hello.py             # Exercício para completar
│   └── test_ex00.sh         # Script de teste
├── ex01/
├── ex02/
├── ex03/
├── ex04/
├── ex05/                    # ⚠️ A partir daqui: usar main()
├── ex06/
├── ex07/
├── ex08/
└── ex09/
```

## 🎯 Próximos Passos

### 1. Começar pelo ex00
```bash
cd ex00
cat Hello.py                  # Ver o código atual
python3 Hello.py              # Testar
```

### 2. Resolver o exercício
- Editar `Hello.py` para modificar as saudações
- Trocar "tata!" por "World!"
- Trocar "toto!" por "France!" (ou país do seu campus)
- Trocar "tutu!" por "Paris!" (ou cidade do seu campus)
- Trocar "titi!" por "42Paris!" (ou nome do seu campus)

### 3. Testar sua solução
```bash
python3 Hello.py | cat -e     # Ver output com $
bash test_ex00.sh             # Rodar teste completo
norminette Hello.py           # Verificar norma
```

### 4. Quando terminar o ex00
```bash
cd ../ex01                    # Ir para próximo exercício
```

## 💡 Dicas para ex00

### Modificando list
```python
ft_list[1] = "World!"
# ou
ft_list = ["Hello", "World!"]
```

### Modificando tuple
```python
# Tuples são imutáveis, precisa recriar
ft_tuple = ("Hello", "France!")
```

### Modificando set
```python
# Sets são mutáveis mas sem ordem garantida
ft_set = {"Hello", "Paris!"}
```

### Modificando dict
```python
ft_dict["Hello"] = "42Paris!"
# ou
ft_dict = {"Hello": "42Paris!"}
```

## 📚 Recursos de Ajuda

1. **README.md** - Visão geral completa de todos os exercícios
2. **COMANDOS_UTEIS.md** - Comandos Python e Git úteis
3. **template_example.py** - Estrutura para exercícios com main()
4. **en.subject.pdf** - Enunciado oficial completo

## ⚠️ Lembre-se

### Até ex04 (inclusive)
- ✅ Pode escrever código no escopo global
- ✅ Estrutura simples

### A partir do ex05
- ⚠️ Obrigatório usar função main()
- ⚠️ Todas as funções devem ter docstrings
- ⚠️ Tratar todas as exceções
- ⚠️ Estrutura:
```python
def main():
    # código aqui
    pass

if __name__ == "__main__":
    main()
```

## 🔍 Verificar Norma

Sempre antes de submeter:
```bash
norminette seu_arquivo.py
```

Erros comuns de norma:
- Linha muito longa (> 79 caracteres)
- Importações não utilizadas
- Variáveis não utilizadas
- Espaços em branco extras
- Falta de linha em branco no final do arquivo

## 🎓 Aprendizado Progressivo

Cada exercício introduz um conceito novo:

1. **ex00**: Estruturas de dados básicas
2. **ex01**: Bibliotecas (time/datetime)
3. **ex02**: Funções e tipos
4. **ex03**: Valores "nulos" em Python
5. **ex04**: Argumentos de linha de comando
6. **ex05**: Programas completos com main()
7. **ex06**: List comprehensions e lambda
8. **ex07**: Dicionários
9. **ex08**: Generators (yield)
10. **ex09**: Criação de pacotes

## 🆘 Precisa de Ajuda?

Se tiver dúvidas:
1. Leia o enunciado com atenção (en.subject.pdf)
2. Consulte COMANDOS_UTEIS.md
3. Veja o template_example.py
4. Teste seu código incrementalmente
5. Use print() para debug

---

## ⚡ Comando para começar AGORA:

```bash
cd /home/andrefil/42/python/piscine/ex00
vim Hello.py
# ou
code Hello.py
```

**Boa sorte! 🚀**
