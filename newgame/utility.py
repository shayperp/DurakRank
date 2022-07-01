loser = 5
players_stat = {'Reem': 0, 'Shay': 0, 'Kobi': 0}
game_name = "Game number"
players_default = ['Reem', 'Shay', 'Kobi']
players_list = 'players[]'
score_field = 'game_score'
userName_field = 'user_name'
gameName_field = 'game_name'
quick_score = [{'user_name': 'Reem', 'score': 0}, {'user_name': 'Shay', 'score': 0}, {'user_name': 'Kobi', 'score': 0}]
quick_name = 'Coalition - quick Game'


def make_game(score, name):
    game_stat = {score_field: score, gameName_field: name}
    return game_stat
