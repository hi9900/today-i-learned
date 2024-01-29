class Player:
    def __init__(self, name, team):
        self.name = name
        self.xp = 1500
        self.team = team

    def introduce(self):
        print(f"Hello! I'm {self.name}")

class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []

    def show_players(self):
        for player in self.players:
            player.introduce()

    def add_player(self, name):
        new_player = Player(name, self.team_name)
        self.players.append(new_player)

    # 플레이어 삭제
    def remove_player(self, name):
        for player in self.players:
            if player.name == name:
                self.players.remove(player)

    # team XP
    def show_team_xp(self):
        team_xp = 0
        for player in self.players:
            team_xp += player.xp
        print(f"The {self.team_name} has {team_xp} points!")


team_x = Team("Team X")
team_x.add_player("hihi")
team_x.add_player("haha")
# team_x.show_players()
team_x.show_team_xp()