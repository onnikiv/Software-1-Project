import gamecredits
import gamesql
from colorama import Fore,init
init(autoreset=True)


def end_game(score,co2_used,used_time):
    print(f"{Fore.GREEN}Your final score is: {score}")
    print(f"Your final co2 and how long your flighttime is: \n {co2_used:.2f}gramms and {used_time % 24:.2f}days")

    gamesql.top_players()

    gamecredits.game_credits_query()
    return False