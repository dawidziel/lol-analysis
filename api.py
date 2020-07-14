from classes.CurrentPlayers import CurrentPlayers
from classes.TeamStatsController import TeamStatsController
from classes.SQLController import SQLController
from Keys import Keys

API_KEY = Keys.API_KEY

match_id = Keys.match_id

def main():
    try:
        sqlc = SQLController(API_KEY, match_id)
        sqlc.your_team_stats_table()
        sqlc.enemy_team_stats_table()

    except:
        print("error")



if __name__ == "__main__":
    main()