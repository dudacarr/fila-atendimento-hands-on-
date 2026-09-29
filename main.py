import heapq
import random

class Cliente:
    def __init__(self, nome, senha, prioridade):
        self.nome = nome
        self.senha = senha
        self.prioridade = prioridade

    def __str__(self):
        return f"{self.nome} - Senha: {self.senha} - Prioridade: {self.prioridade}"

class Fila:
    def __init__(self):
        self.fila = []

    def enqueue(self, cliente):
        self.fila.append(cliente)

    def dequeue(self):
        if self.empty():
            return None
        return self.fila.pop(0)

    def head(self):
        if self.empty():
            return None
        return self.fila[0]

    def size(self):
        return len(self.fila)

    def empty(self):
        return len(self.fila) == 0

class FilaCircular:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.fila = [None] * capacidade
        self.front = 0
        self.rear = 0
        self.quantidade = 0

    def enqueue(self, cliente):
        if self.quantidade == self.capacidade:
            print("Fila circular cheia!")
            return False

        self.fila[self.rear] = cliente
        self.rear = (self.rear + 1) % self.capacidade
        self.quantidade += 1

        return True

    def dequeue(self):
        if self.quantidade == 0:
            return None

        cliente = self.fila[self.front]
        self.fila[self.front] = None

        self.front = (self.front + 1) % self.capacidade
        self.quantidade -= 1

        return cliente

    def mostrar(self):
        print("Fila:", end=" ")

        for cliente in self.fila:
            if cliente:
                print(cliente.nome, end=" | ")
            else:
                print("-", end=" | ")

        print()
        print("Front:", self.front)
        print("Rear:", self.rear)
        print()

class FilaPrioridade:
    def __init__(self):
        self.fila = []
        self.contador = 0

    def enqueue(self, cliente):
        heapq.heappush(
            self.fila,
            (cliente.prioridade, self.contador, cliente)
        )

        self.contador += 1

    def dequeue(self):
        if len(self.fila) == 0:
            return None

        prioridade, contador, cliente = heapq.heappop(self.fila)

        return cliente

    def empty(self):
        return len(self.fila) == 0

def nome_prioridade(numero):
    if numero == 1:
        return "Emergência"
    elif numero == 2:
        return "Prioritário"
    else:
        return "Normal"

print("SISTEMA INTELIGENTE DE ATENDIMENTO")


clientes = []

for i in range(1, 21):
    nome = f"Cliente {i}"
    senha = f"S{i:03d}"
    prioridade = random.randint(1, 3)

    cliente = Cliente(nome, senha, prioridade)
    clientes.append(cliente)

print("\n1 - ORDEM DE CHEGADA")

for cliente in clientes:
    print(
        cliente.nome,
        "| Senha:", cliente.senha,
        "| Prioridade:", nome_prioridade(cliente.prioridade)
    )


print("\n2 - FILA CLÁSSICA (FIFO)")

fila = Fila()

for cliente in clientes:
    fila.enqueue(cliente)

print("Ordem de atendimento:")

while not fila.empty():
    cliente = fila.dequeue()
    print(cliente)

print("\n3 - FILA CIRCULAR")

fila_circular = FilaCircular(5)

for i in range(5):
    fila_circular.enqueue(clientes[i])

print("Depois de inserir 5 clientes:")
fila_circular.mostrar()

print("Removendo 2 clientes:")

print("Atendido:", fila_circular.dequeue())
print("Atendido:", fila_circular.dequeue())

fila_circular.mostrar()

print("Inserindo novos clientes nas posições liberadas:")

fila_circular.enqueue(clientes[5])
fila_circular.enqueue(clientes[6])

fila_circular.mostrar()

print("\n4 - FILA DE PRIORIDADE")

fila_prioridade = FilaPrioridade()

for cliente in clientes:
    fila_prioridade.enqueue(cliente)

print("Ordem de atendimento:")

while not fila_prioridade.empty():
    cliente = fila_prioridade.dequeue()

    print(
        cliente.nome,
        "| Senha:", cliente.senha,
        "| Prioridade:", nome_prioridade(cliente.prioridade)
    )


print("\n5 - COMPARAÇÃO")

print("""
Fila Clássica:
Atende os clientes exatamente na ordem em que chegaram.

Fila Circular:
Utiliza posições fixas e reutiliza os espaços liberados
após a remoção de clientes.

Fila de Prioridade:
Atende primeiro os clientes de maior prioridade.
Prioridade 1 vem antes da 2, que vem antes da 3.
Em caso de empate, mantém a ordem de chegada.
""")
