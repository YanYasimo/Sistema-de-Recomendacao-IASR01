from dataclasses import dataclass 

@dataclass()
class Produto:
    id: int
    nome: str
    preco: float
    estoque: int

    def aumentarEstoque(self, adicionar):
        self.estoque: int = self.estoque + adicionar

    def diminuirEstoque(self, reduzir):
        self.estoque: int = self.estoque - reduzir

    def alterarPreco(self, novoPreco):
        self.preco: float = novoPreco

    def __str__(self):
        return f"Produto: {self.nome} | Preço: {self.preco} | Estoque: {self.estoque}"
    
    def __repr__(self):
        return f"Produto: {self.nome} | Preço: {self.preco} | Estoque: {self.estoque}"
    
    def __eq__(self, other):
        return self.id == other.id
    