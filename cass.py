from riotwatcher import LolWatcher, ApiError
lol_watcher = LolWatcher('RGAPI-ca3abcba-f2e6-485d-b442-5b641048377d')
region = 'euw1'
me = lol_watcher.summoner.by_name(region, 'dywan1na')
match = lol_watcher.match.by_id(region, 4674931321)
print(match['participants'][0]['stats']['totalDamageDealtToChampions'])