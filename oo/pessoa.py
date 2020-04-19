class Pessoa:
    olhos=2

    def __init__(self, *filhos, nome=None, idade=21):
      self.idade = idade
      self.nome = nome
      self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


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
    krahe.olhos = 1
    del krahe.olhos
    print(krahe.__dict__)
    print(allek.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(krahe.olhos)
    print(allek.olhos)
    print(id(Pessoa.olhos), id(krahe.olhos), id(allek.olhos))
    print(Pessoa.metodo_estatico(), krahe.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), krahe.nome_e_atributos_de_classe())