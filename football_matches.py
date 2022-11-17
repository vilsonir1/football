# This script, opens a CSV file with football data
# Save it on a DICT
# And present it as you wish

import pdb; pdb.set_trace()

def open_csv_file(file, mode):
    try:
        with open(file, mode) as openfile:
            line = openfile.readlines()
            return line
    except FileNotFoundError:
        print('File Not Found')
    except:
        print('Unknown error')


def import_data(data):
    try:
        season = {}
        stands = {}
        teams = {''}
        counter = 1
        wins = 0
        draws = 0
        loses = 0
        points = 0
        new_wins = 0
        new_draws = 0
        new_loses = 0
        new_points = 0
        for match in data:
            item = match.strip().split(',')
            season[counter] = {'Date': item[1], 'Home': item[2], 'Away': item[3], 'HG': item[4], 'AG': item[5]}
            teams.add(item[2])
            teams.add(item[3])
            counter += 1
            if item[4] > item[5]:
                if not stands[item[2]]:
                    new_wins = wins + 1
                    new_draws = draws
                    new_loses = loses
                    new_points = points
                else:
                    new_wins = stands[item[2]]['wins'] + wins + 1
                    new_points = stands[item[2]]['points'] + points + 3
            elif item[4] == item[5]:
                if stands[item[2]]:
                    new_draws = stands[item[2]]['draws'] + draws + 1
                    new_points = stands[item[2]]['points'] + points + 1
                else:
                    new_wins = wins
                    new_draws = draws + 1
                    new_loses = loses
                    new_points = points
            elif item[4] < item[5]:
                if not stands[item[2]]:
                    new_wins = wins
                    new_draws = draws
                    new_loses = loses + 1
                    new_points = points
                else:
                    new_wins = stands[item[2]]['loses'] + loses + 1

            stands[item[2]]['wins'] = new_wins
            stands[item[2]]['draws'] = new_draws
            stands[item[2]]['loses'] = new_loses
            stands[item[2]]['points'] = new_points
        teams.remove('')
        print(stands)
        return season, teams
    except:
        print('Unknown error')


def show_teams(data):
    try:
        for item in data:
            print(item)
    except:
        print('Unknown Error')
    input()


def show_matches(data):
    try:
        for match in range(len(data)):
            match_date = data[match + 1]['Date']
            match_home = data[match + 1]['Home']
            match_away = data[match + 1]['Away']
            match_hg = data[match + 1]['HG']
            match_ag = data[match + 1]['AG']
            print('Date: {} -> {} {} x {} {}'.format(match_date, match_home, match_hg, match_ag, match_away))
    except:
        print('Unknown error')
    finally:
        input()


def show_stands(stands):
    try:
        for stand in stands:
            # print('Team : {} - P{} - W{} - D{} - L{}'.format(stand[]))
            print(stand)
    except:
        print('Unknown Error')


def show_matches_team(data, team):
    try:
        for match in range(len(data)):
            if data[match + 1]['Home'] == team or data[match + 1]['Away'] == team:
                match_date = data[match + 1]['Date']
                match_home = data[match + 1]['Home']
                match_away = data[match + 1]['Away']
                match_hg = data[match + 1]['HG']
                match_ag = data[match + 1]['AG']
                print('Date: {} -> {} {} x {} {}'.format(match_date, match_home, match_hg, match_ag, match_away))
    except:
        print('Unknown error')
    finally:
        input()


def print_menu():
    print('------------------------------------------')
    print('1 - Show all matches')
    print('2 - Show all teams')
    print('3 - Matches for team')
    print('4 - Stands')
    print('E - End program')
    print('------------------------------------------')


# Preparing the Environment
mydata = open_csv_file('2000-01.csv', 'r')
mymatches, myteams = import_data(mydata)

while True:
    print_menu()
    option = input('Choose one option: ')
    if option == '1':
        show_matches(mymatches)
    elif option == '2':
        show_teams(myteams)
    elif option == '3':
        myteam = input('Choose the team: ')
        show_matches_team(mymatches, myteam)
    elif option == '4':
        show_stands(mystands)
    elif option == 'E' or option == 'e':
        print('Finishing...')
        break
    else:
        print('Invalid Option')
