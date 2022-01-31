import requests
import json
from datetime import datetime
import time

games_link = 'https://1xstavka.ru/LiveFeed/Get1x2_VZip' \
             '?sports=1&count=50000&lng=en&antisports=188' \
             '&mode=4&country=1&partner=51&noFilterBlockEvent=true'
stats_link = 'https://1xstavka.ru/LiveFeed/GetGameZip?id={}&lng=en'


def get_json(link) -> dict:
    """
    Function to retrieve JSON
    :link: Linked where from retrieve API
    :return: JSON from API
    """
    result = requests.get(link)
    return result.json()


def save_json(file: dict, path: str) -> None:
    """
    Saves json to path
    :param file:
    :param path:
    """
    with open(path, 'w') as f:
        json.dump(file, f, indent=2)


def load_task(path: str):

    today_datetime = datetime.now().strftime("%m%d%y_%H%M")  # Current timestamp

    games = get_json(games_link)
    # Filtering out games without stats
    sorted_games = [x for x in games['Value'] if "SVoAP" not in x.keys() and "SC" in x.keys() and "ST" in x['SC'].keys()]
    save_json(sorted_games, f'{path}/g_{today_datetime}.json')

    return (today_datetime)


"""
{"C":1.52,"G":1,"T":3}
G
1 - 1x2
8 - Double chance
17 - Total
2 - Handicap
19 - Both team to score
"""

"""
VALUE['AM'] - Amatuer games
ST['Value']:
    ID
    45 - Attacks
    58 - Dangerous
    29 - Possesion
    59 - Shots on
    60 - Shoots off
    70 - Corner
    26 - Yellow
    72 - Pen?
"""



