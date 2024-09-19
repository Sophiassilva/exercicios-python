from datetime import date

class Pessoa:
    anoatual = date.today().year
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, anonascimento):
        self._idade = date.today().year - anonascimento

p1 = Pessoa('Harry', 1981, 'M')
print(p1.idade)
    