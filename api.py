from classes.SummonerController import SummonerController
from classes.CurrentPlayers import CurrentPlayers
from classes.StatsController import StatsController

def main():
    try:
        server = input("Podaj nazwę serwera (np. eun1, euw1): ")
        match_id = input("Podaj matchid: ")
        stats = StatsController(SummonerController.API_KEY,server, match_id)
        print(stats.match_stats)
        

    except:
        print("error")



if __name__ == "__main__":
    main()
