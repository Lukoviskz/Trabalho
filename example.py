from typing import List

# A classe Livro não estava no seu exemplo, então criei uma básica.
class Livro:
    def __init__(self, titulo: str):
        self.titulo = titulo

    def __repr__(self) -> str:
        return f"Livro(titulo='{self.titulo}')"

class LivroIterator:
    """
    Esta classe é o iterador concreto. Em Python, o método `next()`
    do pseudocódigo é geralmente chamado de `__next__` e `hasNext()`
    é implementado pela lógica dentro de `__next__` que levanta a
    exceção StopIteration.
    """
    def __init__(self, livros: List[Livro]):
        self._livros = livros
        self._posicao = 0

    def __iter__(self):
        # Retorna o próprio objeto iterador
        return self

    def __next__(self) -> Livro:
        """Retorna o próximo livro ou levanta StopIteration se não houver mais."""
        if self._posicao >= len(self._livros):
            raise StopIteration
        livro = self._livros[self._posicao]
        self._posicao += 1
        return livro

class Biblioteca:
    """
    Esta classe é o 'agregado' ou 'container'. Em Python, para que um
    objeto seja iterável, ele deve implementar o método `__iter__`.
    """
    def __init__(self, livros: List[Livro]):
        self._livros = livros

    def __iter__(self) -> LivroIterator:
        """
        Cria e retorna um novo objeto iterador. Isso permite que múltiplos
        loops 'for' possam percorrer a biblioteca independentemente.
        """
        return LivroIterator(self._livros)

# --- Exemplo de Uso ---

# 1. Criar alguns objetos Livro
livro1 = Livro("O Senhor dos Anéis")
livro2 = Livro("Duna")
livro3 = Livro("Fundação")

# 2. Criar a coleção (Biblioteca)
biblioteca = Biblioteca([livro1, livro2, livro3])

# 3. Iterar sobre a biblioteca usando um loop 'for' (a forma mais comum)
print("Iterando com um loop 'for':")
for livro in biblioteca:
    print(livro)

# 4. Usar o iterador manualmente (menos comum, mas demonstra o funcionamento)
print("\nIterando manualmente:")
meu_iterador = iter(biblioteca) # ou biblioteca.__iter__()
print(next(meu_iterador))      # ou meu_iterador.__next__()
print(next(meu_iterador))
print(next(meu_iterador))
# A próxima chamada a next(meu_iterador) levantaria a exceção StopIteration
