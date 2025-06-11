Exemplo em pseudo-código:

interface Iterator {
boolean hasNext();
Object next();
}

class LivroIterator implements Iterator {
private Livro[] livros;
private int posicao = 0;

public LivroIterator(Livro[] livros) {
this.livros = livros;
}

public boolean hasNext() {
return posicao < livros.length;
}

public Object next() {
return livros[posicao++];
}
}

class Biblioteca {
private Livro[] livros;

public Biblioteca(Livro[] livros) {
this.livros = livros;
}

public Iterator createIterator() {
return new LivroIterator(livros);
}
}
