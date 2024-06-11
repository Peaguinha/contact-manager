from main import Agenda

class ContactManager:
    def __init__(self):
        self.agenda = Agenda()

    def exibir_menu(self):
        print("### MENU ###")
        print("1. Adicionar Contato")
        print("2. Pesquisar Contato por Telefone")
        print("3. Remover Contato por Telefone")
        print("4. Sair")

    def adicionar_contato(self):
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        self.agenda.adicionar_contato(nome, telefone)
        print("Contato adicionado com sucesso!")

    def pesquisar_contato_por_telefone(self):
        telefone = input("Digite o telefone do contato que deseja pesquisar: ")
        resultado_pesquisa = self.agenda.pesquisar_contato_por_telefone(telefone)
        print(f"O contato com o telefone {telefone} é: {resultado_pesquisa}")

    def remover_contato_por_telefone(self):
        telefone = input("Digite o telefone do contato que deseja remover: ")
        resultado_remover = self.agenda.remover_contato_por_telefone(telefone)
        print(resultado_remover)

    def executar(self):
        while True:
            self.exibir_menu()
            opcao = input("Digite o número da opção desejada: ")

            if opcao == "1":
                self.adicionar_contato()
            elif opcao == "2":
                self.pesquisar_contato_por_telefone()
            elif opcao == "3":
                self.remover_contato_por_telefone()
            elif opcao == "4":
                print("Saindo...")
                break
            else:
                print("Opção inválida. Por favor, digite um número válido.")

if __name__ == "__main__":
    manager = ContactManager()
    manager.executar()