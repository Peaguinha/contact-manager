class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, nome, telefone):
        contato = Contato(nome, telefone)
        self.contatos.append(contato)

    def remover_contato_por_telefone(self, telefone):
        for contato in self.contatos:
            if contato.telefone == telefone:
                self.contatos.remove(contato)
                return f"Contato {contato.nome} removido com sucesso."
        return "Contato não encontrado."

    def pesquisar_contato_por_telefone(self, telefone):
        for contato in self.contatos:
            if contato.telefone == telefone:
                return contato.nome
        return "Contato não encontrado."

if __name__ == "__main__":
    agenda = Agenda()

    # Adicionando contatos
    agenda.adicionar_contato("João", "1234-5678")
    agenda.adicionar_contato("Maria", "9876-5432")
    agenda.adicionar_contato("Pedro", "1111-2222")

    # Pesquisando contato por telefone
    telefone_pesquisado = "9876-5432"
    resultado_pesquisa = agenda.pesquisar_contato_por_telefone(telefone_pesquisado)
    print(f"O contato com o telefone {telefone_pesquisado} é: {resultado_pesquisa}")

    # Removendo contato pelo telefone
    telefone_remover = "1234-5678"
    resultado_remover = agenda.remover_contato_por_telefone(telefone_remover)
    print(resultado_remover)

    # Verificando se o contato foi removido
    resultado_pesquisa_apos_remover = agenda.pesquisar_contato_por_telefone(telefone_remover)
    print(f"O contato com o telefone {telefone_remover} após remoção é: {resultado_pesquisa_apos_remover}")


