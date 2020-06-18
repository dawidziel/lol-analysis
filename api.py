import requests
import json
def taking_summoner_id(API_KEY,summoner_name, server):
    url = 'https://' + server +'.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + summoner_name + '?api_key=' + API_KEY
    answer = requests.get(url)
    json_answer = json.loads(answer.text)
    return answer
def main():
    API_KEY = 'RGAPI-049e494c-77a8-43a3-b711-099b48eec15f'
    server = input("Podaj nazwę serwera (np. eun1, euw)")
    summoner_name = input("Podaj nazwę summonera")
    print(taking_summoner_id(API_KEY,summoner_name,server).content)
if __name__ == "__main__":
    main()

