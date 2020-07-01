from classes.CurrentPlayers import CurrentPlayers
from classes.TeamStatsController import TeamStatsController
from Keys import Keys

API_KEY = Keys.API_KEY

match_id = Keys.match_id

def main():
    try:
        server = input("Podaj nazwę serwera (np. eun1, euw1): ")
        team_stats = TeamStatsController(API_KEY,server, match_id)
        print(team_stats.enemy_team_id)
        print(team_stats.taking_team_stats())
        print("\n" + team_stats.list_enemy_champions)
        

    except:
        print("error")



if __name__ == "__main__":
    main()