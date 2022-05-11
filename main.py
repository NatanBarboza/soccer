from positions.goalkeeper import GoalKeeper
from positions.defender import Defender
from positions.midifielder import Midifielder
from positions.stricker import Stricker
from team import Team

gk = GoalKeeper("João", 20, 1.8, 1)
def_1 = Defender("José", 25, 1.76, 1)
def_2 = Defender("Zezinho", 22, 1.7, 1)
def_3 = Defender("Ricardo", 28, 1.72, 1)
mid_1 = Midifielder("Damião", 30, 1.65, 1)
mid_2 = Midifielder("Daniel", 21, 1.7, 1)
mid_3 = Midifielder("Jorginho", 20, 1.74, 1)
mid_4 = Midifielder("Davi", 26, 1.71, 1)
st_1 = Stricker("Ronaldo", 20, 1.92, 1)
st_2 = Stricker("Marcio", 32, 1.7, 1)
st_3 = Stricker("Romelu", 30, 1.9, 1)

players = [gk.name, def_1.name, def_2.name, def_3.name, mid_1.name, mid_2.name, mid_3.name, mid_4.name, st_1.name, st_2.name, st_3.name]

team = Team(1, "FulanosTeam", players)

print(team.team)
print(team.name_team)
print(team.players)