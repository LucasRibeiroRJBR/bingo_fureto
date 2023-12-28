import random

class Bingo:
    def __init__(self):
        self.cartela = list(range(1, 76))
        random.shuffle(self.cartela)
        self.numeros_chamados = set()

    def chamar_numero(self):
        if not self.cartela:
            print("Todos os números já foram chamados!")
            return None

        numero_chamado = self.cartela.pop()
        self.numeros_chamados.add(numero_chamado)
        return numero_chamado

    def verificar_cartela(self):
        return not bool(self.cartela)

    def jogar(self):
        while not self.verificar_cartela():
            input("Pressione Enter para chamar um número...")
            numero_chamado = self.chamar_numero()
            if numero_chamado:
                print(f"Número chamado: {numero_chamado}")
                print(f"Números chamados até agora: {sorted(self.numeros_chamados)}")

        print("Bingo! Todos os números foram chamados.")

# Exemplo de uso
jogo = Bingo()
jogo.jogar()