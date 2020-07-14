from .TeamStatsController import TeamStatsController
import pandas as pd
import sqlite3


class SQLController:
    def __init__(self, API_KEY, match_id):
        self.matchId = match_id
        self.enemy_name = input("Input enemy team name: ")
        self.server = input("Input server name (eun1, euw1): ")
        self.team_stats = TeamStatsController(API_KEY, self.server, match_id)

#collecting data for your team and inserting into sql database
    def your_team_stats_table(self):
#creating adequate dataframe
        data = self.team_stats.taking_team_stats()
        df = pd.DataFrame(data, columns=['win','firstBlood','firstTower','firstInhibitor','firstBaron','firstDragon','firstRiftHerald',
        'towerKills','inhibitorKills','baronKills','dragonKills','riftHeraldKills'] , index = [0])
#adding additional columns to dataframe
        df.insert(0, 'matchId', self.matchId)
        df.insert(1, 'enemyTeamName', self.enemy_name.upper())
        df.insert(2, 'whichTeam', "yours")

        conn = sqlite3.connect("lol_stats.db")
        cursor = conn.cursor()
        cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='team_stats'")

        if cursor.fetchone()[0] == 1:
            cursor.execute("SELECT COUNT(*) FROM team_stats WHERE matchId = ?",(self.matchId,))

            if cursor.fetchone()[0] == 0:
                df.to_sql("team_stats", conn, if_exists = 'append', index = False)
            else:
                print("This record already exists")

        else:
            df.to_sql("team_stats", conn, if_exists = 'append', index = False)

#collecting data for enemy team and inserting into sql database
    def enemy_team_stats_table(self):

        data = self.team_stats.taking_enemy_team_stats()
        df = pd.DataFrame(data, columns=['win','firstBlood','firstTower','firstInhibitor','firstBaron','firstDragon','firstRiftHerald',
        'towerKills','inhibitorKills','baronKills','dragonKills','riftHeraldKills'] , index = [0])

        df.insert(0, 'matchId', self.matchId)
        df.insert(1, 'enemyTeamName', self.enemy_name.upper())
        df.insert(2, 'whichTeam', "enemy")

        conn = sqlite3.connect("lol_stats.db")
        cursor = conn.cursor()
        cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='team_stats'")

        if cursor.fetchone()[0] == 1:
            cursor.execute("SELECT COUNT(*) FROM team_stats WHERE matchId = ? AND whichTeam = ?",(self.matchId,"enemy",))
 
            if cursor.fetchone()[0] == 0:
                df.to_sql("team_stats", conn, if_exists = 'append', index = False)
            else:
                print("This record already exists")

        else:
            df.to_sql("team_stats", conn, if_exists = 'append', index = False)
