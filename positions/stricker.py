from player import Player

class Stricker(Player):
    def __init__(self, name:str, age:int, height:float, team:int):
        super().__init__(name, age, height, team)
        self.__position = "ST"

    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, new_position):
        self.__position = new_position

    def __str__(self):
        return self.__name