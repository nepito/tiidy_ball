from tidyball import read_json, get_appearences_on_season_for_player

data_to_test = "tests/data/data_file_16482_2021.json"
aguirre = read_json(data_to_test)
data_to_test = "tests/data/data_file_6485_2021.json"
berterame = read_json(data_to_test)


def test_get_appearences_on_season_for_player():
    aguirre_appearences = {
        "appearences": 32,
        "lineups": 26,
        "minutes": 2257,
        "number": None,
        "position": "Attacker",
        "rating": "7.165625",
        "captain": False,
    }
    _assert_appearences_on_season_for(aguirre, aguirre_appearences)
    berterame_appearences = {
        "appearences": 37,
        "lineups": 37,
        "minutes": 3219,
        "number": None,
        "position": "Attacker",
        "rating": "7.029729",
        "captain": False,
    }
    _assert_appearences_on_season_for(berterame, berterame_appearences)

def _assert_appearences_on_season_for(player, expected_appearences):
    obtained_appearences = get_appearences_on_season_for_player(player)
    assert expected_appearences == obtained_appearences
    