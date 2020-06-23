from kod.classes.SummonerController import SummonerController


def main():
    try:
        server = input("Podaj nazwę serwera (np. eun1, euw1)")
        summoner_name = input("Podaj nazwę summonera")
        summoner = SummonerController(server, summoner_name)
        response_2 = summoner.taking_ladder_info()
        print(response_2['tier'])
        print(response_2['rank'])
        print(str(response_2['leaguePoints']) + " LP")
    except:
        print("jo dupia pojebało sie")


if __name__ == "__main__":
    main()
