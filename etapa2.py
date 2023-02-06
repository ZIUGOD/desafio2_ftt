class Personagem:
    def __init__(self, nome, descricao, link_imagem, programa, animador):
        self.nome = nome
        self.descricao = descricao
        self.link_imagem = link_imagem
        self.programa = programa
        self.animador = animador

nome = str(input("Nome do personagem: "))
descricao = str(input("Descrição do personagem: "))
link_imagem = str(input("Link da imagem do personagem: "))
programa = str(input("Programa do personagem: "))
animador = str(input("Animador do personagem: "))

novo_personagem = Personagem(nome, descricao, link_imagem, programa, animador)

print(f"Nome: {novo_personagem.nome}\n"
      f"Descrição: {novo_personagem.descricao}\n"
      f"Link da imagem: {novo_personagem.link_imagem}\n"
      f"Programa: {novo_personagem.programa}\n"
      f"Animador: {novo_personagem.animador}")
