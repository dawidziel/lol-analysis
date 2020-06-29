from classes.CurrentPlayers import CurrentPlayers
from classes.TeamStatsController import TeamStatsController

API_KEY = 'RGAPI-87bbf0d7-9a87-40ff-adfc-1de595edb315'

def main():
    try:
        server = input("Podaj nazwę serwera (np. eun1, euw1): ")
        match_id = 4674931321
        stats = StatsController(API_KEY,server, match_id)
        print(stats.enemy_team_id)
        print(stats.your_team_id)
        

    except:
        print("error")



if __name__ == "__main__":
    main()
