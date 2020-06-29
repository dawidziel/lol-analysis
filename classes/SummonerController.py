import requests
import json

class SummonerController:   
    API_KEY = 'RGAPI-ca3abcba-f2e6-485d-b442-5b641048377d'
    server = ""
    summoner_name = ""
    summoner_id = ""

    def __init__(self, server, summoner_name):
        self.server = server
        self.summoner_name = summoner_name
        self.taking_summoner_id()

    def taking_summoner_id(self):
        url = 'https://' + self.server + '.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + self.summoner_name + '?api_key=' + self.API_KEY
        answer = requests.get(url)
        json_answer = json.loads(answer.text)
        self.summoner_id = json_answer['id']

    def taking_ladder_info(self):
        url = 'https://' + self.server + '.api.riotgames.com/lol/league/v4/entries/by-summoner/' + self.summoner_id + '?api_key=' + self.API_KEY
        answer = requests.get(url)
        json_answer = [x for x in json.loads(answer.text) if x['queueType'] == 'RANKED_SOLO_5x5']
        return json_answer[0]
