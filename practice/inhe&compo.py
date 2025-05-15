#Inheritance example

class Pessoa():
    def __init__(self, nome, idade): #base classes or super classes
        self.nome = nome
        self.idade = idade
        
class Gerente(Pessoa): #derived classes, subclasses, or subtypes
    def __init__(self, nome, idade, gerente: bool):
        super().__init__(nome, idade)
        self.gerente = gerente


#Composition example

class Tail:
    def __init__(self, length):
        self.length = length  # length in centimeters

class Dog:
    def __init__(self, name, tail: Tail):
        self.name = name
        self.tail = tail  # Composition: a Dog HAS a Tail

class Horse:
    def __init__(self, breed, tail: Tail):
        self.breed = breed
        self.tail = tail  # Composition: a Horse HAS a Tail