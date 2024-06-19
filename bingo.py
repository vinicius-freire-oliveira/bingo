import random

class Bingo:
    def __init__(self):
        self.numeros = list(range(1, 100))
        random.shuffle(self.numeros)

    def sortear_numero(self):
        if self.numeros:
            return self.numeros.pop()
        else:
            print("Todos os números foram sorteados.")
            return None

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.cartela = []

    def preencher_cartela(self, numeros):
        self.cartela = random.sample(numeros, 25)

    def verificar_vitoria(self, numeros_sorteados):
        if all(numero in numeros_sorteados for numero in self.cartela):
            print(f"{self.nome} grita: BINGO! Cartela completa!")
            return True
        return False

# Simulação de um jogo de bingo
def simular_bingo():
    bingo = Bingo()

    # Criando os jogadores
    num_jogadores = int(input("Quantos jogadores participarão? "))
    jogadores = [Jogador(input(f"Nome do jogador {i+1}: ")) for i in range(num_jogadores)]

    # Preenchendo as cartelas dos jogadores
    for jogador in jogadores:
        jogador.preencher_cartela(bingo.numeros)

    # Iniciando o jogo
    print("\nO jogo de Bingo começou!\n")
    numeros_sorteados = []
    vencedor = None
    while True:
        input("Pressione Enter para sortear um número...")
        numero_sorteado = bingo.sortear_numero()
        if numero_sorteado is None:
            break
        print(f"Número sorteado: {numero_sorteado}")
        numeros_sorteados.append(numero_sorteado)
        for jogador in jogadores:
            if jogador.verificar_vitoria(numeros_sorteados):
                vencedor = jogador
                break
        if vencedor:
            break

    # Exibir todos os números sorteados
    print("\nNúmeros sorteados:")
    print(numeros_sorteados)

    # Exibir números da cartela do jogador vencedor
    print(f"\nNúmeros da cartela do jogador vencedor {vencedor.nome}:")
    print(vencedor.cartela)

# Executar a simulação do bingo
simular_bingo()
