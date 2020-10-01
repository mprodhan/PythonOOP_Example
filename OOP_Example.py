class PlayerCharacter:
    membership = True
    def __init__(self, name, age):
        if self.membership:
            self.name = name
            self.age = age

    def shout(self):
        print(f'my name is {self.name}')

player1 = PlayerCharacter('Mustafa', 28)
player2 = PlayerCharacter('Sabina', 21)

print(player1.name, player1.age, player1.shout())
print(f'{player1.name} is {player1.age}. {player1.shout()}.')


print(f'{player2.name} is {player2.age}. {player2.shout()}')

# help(PlayerCharacter)