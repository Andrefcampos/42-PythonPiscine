#!/usr/bin/env python3
"""
Template de exemplo para os exercícios da Piscine Python.

Este arquivo mostra a estrutura básica que deve ser seguida
a partir do exercício 05.
"""


def minha_funcao(parametro):
    """
    Descrição da função.

    Args:
        parametro: Descrição do parâmetro

    Returns:
        Descrição do retorno
    """
    # Seu código aqui
    return parametro


def main():
    """
    Função principal do programa.

    Aqui você deve:
    - Processar argumentos (se necessário)
    - Chamar suas funções
    - Tratar exceções
    """
    try:
        # Exemplo de uso
        resultado = minha_funcao("teste")
        print(resultado)
    except Exception as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    main()
