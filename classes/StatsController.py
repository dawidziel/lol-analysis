import requests
import json
from riotwatcher import LolWatcher
class StatsController:
    def __init__(self, API_KEY, server, match_id):
        self.lol_watcher = LolWatcher(API_KEY)
        self.server = server
        self.match_id = match_id
        self.taking_match_stats()
    def taking_match_stats(self):
        print("nic")
        LolWatcher.match
        answer = requests.get(url)
        json_answer = json.loads(answer.text)
        self.match_stats = json_answer
        