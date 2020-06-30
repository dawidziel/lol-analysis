import requests
import json
from riotwatcher import LolWatcher
class TeamStatsController:
    def __init__(self, API_KEY, server, match_id):
#initalizing useful api interactions
        self.API_KEY = API_KEY
        self.server = server
        self.match_id = match_id
        self.api_values()
#initializing made functions
        self.diagnosing_team_id()
 #       self.taking_match_stats()

    def api_values(self):
        self.lol_watcher = LolWatcher(self.API_KEY)
        self.match = self.lol_watcher.match.by_id(self.server,self.match_id)
        self.champions_version = self.lol_watcher.data_dragon.versions_for_region(self.server)['n']['champion']
        self.champions = self.lol_watcher.data_dragon.champions(self.champions_version)['data']

#function that diagnoses which team_id is suited for your team   
    def diagnosing_team_id(self):
        list_your_champions = []
        id_list = [100,200]
        for i in id_list:
            champion_ids = [str(x['championId']) for x in self.match['participants'] if x['teamId'] == i]
            for x in self.champions:
                if self.champions[x]['key'] in champion_ids:
                    list_your_champions.append(self.champions[x]['id'])
            print(list_your_champions)
            question = input("Was it your teamcomp? (y/n)")
            if question == "y":
                self.your_team_id = i
                id_list.remove(i)
                self.enemy_team_id = id_list[0]
                break
            elif question == "n":
                list_your_champions.clear()
                continue
            else:
                print("Please input correct charakter")
                break

#diagnosing which champions are being played by which player
#    def diagnosing_
        

#below function takes overall team stats
    def taking_team_stats(self):
        team_stats = [x for x in self.match['teams'] if x['teamId'] == self.your_team_id]
        return team_stats

#function takes individual stats
#    def taking_player_stats(self):

