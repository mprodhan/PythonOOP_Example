""" The class below is a constructor class. The idea is that the class
acts as a blueprint how the program will set the parameters for the parent
class and their inherited class. Note: There are no parent class or inherited
class in this example. There are only the constructor class and a basic call 
of the class function."""
class PlayerCharacter:  
    membership = True
    def __init__(self, name, age):
        if self.membership:
            self.name = name
            self.age = age

    def shout(self):
        print(f'my name is {self.name}')

# The below is the instantiation of the class PlayerCharacter.
player1 = PlayerCharacter('Mustafa', 28)
player2 = PlayerCharacter('Sabina', 21)

# The output of different players instantiated from above.
print(player1.name, player1.age, player1.shout())
print(f'{player1.name} is {player1.age}. {player1.shout()}.')


print(f'{player2.name} is {player2.age}. {player2.shout()}')

""" This call function and method calls the blueprint of the class.
This help() function can call anytthing on the parameter."""
help(PlayerCharacter)