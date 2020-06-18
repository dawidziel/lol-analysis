import requests
import json
def taking_summoner_id(API_KEY,summoner_name, server):
    url = 'https://' + server +'.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + summoner_name + '?api_key=' + API_KEY
    answer = requests.get(url)
    json_answer = json.loads(answer.text)
    return json_answer
def taking_ladder_info(API_KEY,summoner_id,server):
    url = 'https://' + server + '.api.riotgames.com/lol/league/v4/entries/by-summoner/' + summoner_id + '?api_key=' + API_KEY
    answer = requests.get(url)
    json_answer = json.loads(answer.text)[0]
    return json_answer
def main():
    API_KEY = 'RGAPI-049e494c-77a8-43a3-b711-099b48eec15f'
    server = input("Podaj nazwę serwera (np. eun1, euw1)")
    summoner_name = input("Podaj nazwę summonera")
    summoner_id = taking_summoner_id(API_KEY,summoner_name,server)['id']
    #final response down there
    response_2 = taking_ladder_info(API_KEY,summoner_id,server)
    print(response_2['tier'])
    print(response_2['rank'])
    print(str(response_2['leaguePoints']) + " LP")
if __name__ == "__main__":
    main()

