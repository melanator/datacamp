import json
from extract import save_json
from datetime import datetime


def parse_field(search_dict, field):
    """
    Wraps field parser in dict with exception handler. If KeyError returns None
    """
    try:
        return search_dict[field]
    except KeyError:
        return None

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


def parse_stats(game_dict):
    stats = game_dict['SC']['ST'][0]['Value']
    return [[x['ID'], int(x['S1']), int(x['S2'])] for x in stats]


def parse_odds(game_dict):
    try:
        return game_dict['E']
    except KeyError:
        return None


def parse_score(game_dict):
    try:
        s1 = game_dict['SC']['FS']['S1']
    except KeyError:
        s1 = 0
    try:
        s2 = game_dict['SC']['FS']['S2']
    except KeyError:
        s2 = 0
    return [s1, s2]


def parse_game(game_dict):
    game_json = {'stats': parse_stats(game_dict),
                 'odds': parse_odds(game_dict),
                 'score': parse_score(game_dict),
                 'id': parse_field(game_dict, 'I'),
                 'cps': parse_field(game_dict['SC'], 'CPS'),
                 'h_name': parse_field(game_dict, 'O1'),
                 'a_name': parse_field(game_dict, 'O2'),
                 'h_id': parse_field(game_dict, 'O1I'),
                 'a_id': parse_field(game_dict, 'O2I'),
                 'league': parse_field(game_dict, 'L'),
                 'league_id': parse_field(game_dict, 'LI'),
                 'country': parse_field(game_dict, 'CN'),
                 'country_id': parse_field(game_dict, 'COI'),
                 'time': parse_field(game_dict['SC'], 'TS')}
    return game_json



def transform_task(path: str, timestamp: str):

    with open(f'{path}/g_{timestamp}.json') as f:
        games_dict = json.load(f)

    transformed = []

    for game in games_dict:
        transformed.append(parse_game(game))

    save_json(transformed, f'{path}/r_g_{timestamp}.json')

"""
{"C":1.52,"G":1,"T":3}
T
1 - 1x2
8 - Double chance
17 - Total
2 - Handicap
19 - Both team to score
"""


