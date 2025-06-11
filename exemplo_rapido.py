# A lista é um objeto "iterável"
minha_lista = ["Maçã", "Banana", "Cereja"]

# Este laço 'for' usa um iterador por baixo dos panos!
# Ele funciona com listas, strings, dicionários, arquivos e mais.
for fruta in minha_lista:
    print(fruta)

# O que o 'for' realmente faz:
# 1. Pede um iterador para a `minha_lista`.
# 2. A cada ciclo, ele chama o método `next()` no iterador para obter o próximo item.
# 3. Quando a coleção acaba, o iterador avisa, e o laço para automaticamente.
