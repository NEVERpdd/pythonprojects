import os

funcionarios = []

class Vendedor():

    meta = 10

    def __init__(self, nome) -> None:
        self.nome = nome
        self.vendas = 0 

    def vendeu(self, vendas):
        self.vendas = int(vendas)

    def bateu_meta(self):
        if self.vendas >= self.meta:
            print(self.nome, "Bateu a meta")
        else: 
            print(self.nome, "Nao bateu a meta")

while True:
    os.system("cls")
    nome_funcionario = input("Qual o nome do funcionario ? ou (Digite 'sair' para encerrar)\n")
    if nome_funcionario.lower() == 'sair':
        os.system("cls")
        for funcionario in funcionarios:
            funcionario.bateu_meta()
        break
        
    venda = input("Qual a quantidade de vendas ?\n")

    vendedor = Vendedor(nome_funcionario)
    vendedor.vendeu(venda)
    vendedor.bateu_meta()
    funcionarios.append(vendedor)
    input("Continuar...")