class Pessoa:
    def __init__(self, *filhos, nome=None, idade=21):
      self.idade = idade
      self.nome = nome
      self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    allek = Pessoa(nome='Allek')
    krahe = Pessoa(allek, nome='Krahe')
    print(Pessoa.cumprimentar(krahe))
    print(id(krahe))
    print(krahe.cumprimentar())
    print(krahe.nome)
    print(krahe.idade)
    for filho in krahe.filhos:
        print(filho.nome)
    krahe.sobrenome = 'Vieira'
    del krahe.filhos
    print(krahe.__dict__)
    print(allek.__dict__)
