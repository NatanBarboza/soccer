class Player:
    def __init__(self, name:str, age:int, height:float, team:int):
        self.__name = name
        self.__age = age
        self.__height = height
        self.__team = team
        self.__position = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        self.__age = new_age

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_height):
        self.__height = new_height

    @property
    def team(self):
        return self.__team

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_position):
        self.__position = new_position