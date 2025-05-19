class Produto:
    def __init__(self, nome, preco, estoque):
        self.__nome = nome            # atributo privado
        self.__preco = preco          # atributo privado
        self.__estoque = estoque      # atributo privado

    # Getter para nome
    def get_nome(self):
        return self.__nome

    # Setter para nome
    def set_nome(self, novo_nome):
        if isinstance(novo_nome, str) and novo_nome.strip():
            self.__nome = novo_nome
        else:
            print("Nome inválido.")

    # Getter para preco
    def get_preco(self):
        return self.__preco

    # Setter para preco
    def set_preco(self, novo_preco):
        if novo_preco >= 0:
            self.__preco = novo_preco
        else:
            print("Preço deve ser maior ou igual a zero.")

    # Getter para estoque
    def get_estoque(self):
        return self.__estoque

    # Setter para estoque
    def set_estoque(self, novo_estoque):
        if isinstance(novo_estoque, int) and novo_estoque >= 0:
            self.__estoque = novo_estoque
        else:
            print("Estoque deve ser um número inteiro positivo.")

    # Método para exibir informações do produto
    def exibir_informacoes(self):
        print(f"Produto: {self.__nome}")
        print(f"Preço: R${self.__preco:.2f}")
        print(f"Estoque: {self.__estoque} unidades")


# Exemplo de uso:
produto1 = Pro
