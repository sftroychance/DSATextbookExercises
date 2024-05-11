basketball_players = [
    {'first_name': "Jill", 'last_name': "Huang", 'team': "Gators"},
    {'first_name': "Janko", 'last_name': "Barton", 'team': "Sharks"},
    {'first_name': "Wanda", 'last_name': "Vakulskas", 'team': "Sharks"},
    {'first_name': "Jill", 'last_name': "Moloney", 'team': "Gators"},
    {'first_name': "Luuk", 'last_name': "Watkins", 'team': "Gators"} ]

football_players = [
    {'first_name': "Hanzla", 'last_name': "Radosti", 'team': "32ers"},
    {'first_name': "Tina", 'last_name': "Watkins", 'team': "Barleycorns"},
    {'first_name': "Alex", 'last_name': "Patel", 'team': "32ers"},
    {'first_name': "Jill", 'last_name': "Huang", 'team': "Barleycorns"},
    {'first_name': "Wanda", 'last_name': "Vakulskas", 'team': "Barleycorns"} ]

def players_in_common(team1, team2):
    team1_hash = {}

    for player in basketball_players:
        team1_hash[f'{player['first_name']} {player['last_name']}'] = True

    result = []

    for player in football_players:
        name = f'{player['first_name']} {player['last_name']}'
        if team1_hash.get(name, ''):
            result.append(name)

    return result

print(players_in_common(basketball_players, football_players))
