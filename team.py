class Team:
    def __init__(self, team:int, name_team:str, players:list):
        self.__team = team
        self.__name_team = name_team
        self.__players = players
    
    @property
    def team(self):
        return self.__team

    @property
    def name_team(self):
        return self.__name_team

    @name_team.setter
    def name_team(self):
        return self.__name_team

    @property
    def players(self):
        return self.__players

    @players.setter
    def players(self, new_player, index):
        self.__players[index] = new_player