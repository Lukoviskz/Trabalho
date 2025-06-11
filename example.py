# from typing import List
# A importação 'List' é uma "type hint" (dica de tipo). Ela informa a outros
# desenvolvedores e a ferramentas de análise de código que a variável 'livros'
# deve ser uma lista de objetos 'Livro'. Não é obrigatória para o funcionamento
# do código, mas é uma excelente prática de programação.
from typing import List

# --- Classe de Dados: Livro ---
# Esta classe representa o objeto que queremos armazenar e sobre o qual queremos iterar.
# É uma classe simples, apenas para termos algo para colocar na nossa coleção.
class Livro:
    # O método __init__ é o construtor da classe. É chamado quando criamos
    # um novo objeto Livro, como em: livro1 = Livro("O Senhor dos Anéis")
    def __init__(self, titulo: str):
        # 'self' se refere à instância específica do objeto que está sendo criado.
        # Aqui, estamos armazenando o 'titulo' que foi passado como argumento
        # em um atributo chamado 'titulo' dentro do objeto.
        self.titulo = titulo

    # O método __repr__ (representação) define como o objeto será exibido
    # em contextos de depuração, como quando você simplesmente digita o nome
    # da variável em um console Python ou usa a função print(). É muito útil
    # para entender o estado de um objeto.
    def __repr__(self) -> str:
        return f"Livro(titulo='{self.titulo}')"

# --- Classe Iteradora: LivroIterator ---
# Este é o objeto que faz o trabalho pesado da iteração. Ele mantém o estado
# da iteração, ou seja, qual item ele precisa retornar a seguir.
# Corresponde diretamente à sua classe 'LivroIterator'.
class LivroIterator:
    # O construtor recebe a coleção sobre a qual vai iterar.
    def __init__(self, livros: List[Livro]):
        # Armazena a lista de livros internamente. O '_' no início (_livros)
        # é uma convenção em Python para indicar que este é um atributo
        # "protegido", ou seja, para uso interno da classe.
        self._livros = livros
        # Este é o "cursor" ou "ponteiro". Mantém o controle de onde estamos
        # na iteração. Começa em 0, que é o índice do primeiro elemento.
        self._posicao = 0

    # Este método faz com que o próprio objeto iterador seja... iterável.
    # Em loops 'for', isso não faz muita diferença, mas é necessário para
    # cumprir o protocolo de iterador em Python. Ele simplesmente retorna a si mesmo.
    def __iter__(self):
        return self

    # Este é o coração do iterador. Corresponde à lógica combinada dos seus
    # métodos 'hasNext()' e 'next()'.
    def __next__(self) -> Livro:
        # 1. VERIFICAR SE HÁ UM PRÓXIMO (Lógica do 'hasNext')
        # Se a nossa posição atual for maior ou igual ao número total de livros,
        # significa que já percorremos toda a lista.
        if self._posicao >= len(self._livros):
            # Em vez de retornar 'false', Python levanta a exceção StopIteration.
            # O loop 'for' sabe como capturar essa exceção e encerrar o loop
            # de forma limpa e automática.
            raise StopIteration

        # 2. OBTER O PRÓXIMO ITEM E AVANÇAR (Lógica do 'next')
        # Pega o livro na posição atual da lista.
        livro = self._livros[self._posicao]
        # Incrementa a posição para que na próxima chamada de __next__,
        # peguemos o item seguinte.
        self._posicao += 1
        # Retorna o livro que acabamos de pegar.
        return livro

# --- Classe Agregadora/Contêiner: Biblioteca ---
# Esta é a coleção que contém os objetos 'Livro'. O papel dela é gerenciar
# a coleção e, quando solicitado, fornecer um iterador para percorrê-la.
class Biblioteca:
    def __init__(self, livros: List[Livro]):
        # O construtor simplesmente armazena a lista de livros.
        self._livros = livros

    # Este é o método que torna a classe Biblioteca "iterável".
    # Corresponde ao seu método 'createIterator()'.
    def __iter__(self) -> LivroIterator:
        # Quando um loop 'for' começa (ex: for livro in biblioteca:), Python
        # chama este método.
        # A responsabilidade deste método é criar e retornar UMA NOVA INSTÂNCIA
        # do nosso iterador. Isso é crucial, pois permite que várias iterações
        # ocorram ao mesmo tempo sobre a mesma biblioteca, sem interferir umas
        # com as outras.
        return LivroIterator(self._livros)

# --- Exemplo de Uso na Prática ---

# 1. Criamos os objetos de dados que farão parte da nossa coleção.
livro1 = Livro("O Senhor dos Anéis")
livro2 = Livro("Duna")
livro3 = Livro("Fundação")

# 2. Criamos a nossa coleção iterável, a 'Biblioteca', passando a lista de livros.
biblioteca = Biblioteca([livro1, livro2, livro3])

# 3. A forma Pythonica de usar o padrão: o loop 'for'.
# Esta é a maneira mais simples e legível de iterar.
print("Iterando com um loop 'for':")
# O que acontece aqui nos bastidores:
# a) Python chama `iter(biblioteca)`, que por sua vez chama `biblioteca.__iter__()`.
# b) Isso cria e retorna um novo objeto `LivroIterator`.
# c) A cada volta do loop, Python chama `next()` no objeto iterador retornado.
# d) O valor retornado por `next()` é atribuído à variável `livro`.
# e) Quando o iterador levanta `StopIteration`, o loop termina.
for livro in biblioteca:
    print(livro)

# 4. A forma manual, para entender o que o 'for' faz por baixo dos panos.
print("\nIterando manualmente:")
# a) Chamamos explicitamente a função `iter()` no nosso objeto iterável.
#    Isso chama `biblioteca.__iter__()` e nos dá o iterador.
meu_iterador = iter(biblioteca)

# b) Chamamos a função `next()` no iterador para pegar cada item, um por um.
#    Cada chamada executa o código dentro de `LivroIterator.__next__()`.
print(next(meu_iterador)) # Retorna o primeiro livro e avança a posição para 1
print(next(meu_iterador)) # Retorna o segundo livro e avança a posição para 2
print(next(meu_iterador)) # Retorna o terceiro livro e avança a posição para 3

# Se tentássemos chamar `next(meu_iterador)` mais uma vez, a condição
# `if self._posicao >= len(self._livros)` seria verdadeira (3 >= 3),
# e o código levantaria a exceção `StopIteration`, resultando em um erro
# se não for tratado.
