# This script, opens a CSV file with football data
# Save it on a DICT
# And present it as you wish
import glob

# Preparing the Environment
stands = {}
LOADED = 0


def choose_file():
    try:
        print("Choose one file below:")
        print(glob.glob("*.csv"))
        print("")
        myfile = input('File: ')
        return myfile
    except Exception as error:
        print(error)

def open_csv_file(file, mode):
    try:
        with open(file, mode) as openfile:
            line = openfile.readlines()
            return line
    except FileNotFoundError:
        print('File Not Found')
    except Exception as error:
        print(error)


def import_data(data):
    try:
        season = {}
        teams = {''}
        counter = 0
        for match in data:
            if counter > 0:
                item = match.strip().split(',')
                season[counter] = {'Date': item[1], 'Home': item[2], 'Away': item[3], 'HG': item[4], 'AG': item[5]}
                teams.add(item[2])
                teams.add(item[3])
                if item[4] > item[5]:
                    import_stands(item[2], 3, 1, 0, 0, int(item[4]), int(item[5]))
                    import_stands(item[3], 0, 0, 0, 1, int(item[5]), int(item[4]))
                elif item[4] < item[5]:
                    import_stands(item[2], 0, 0, 0, 1, int(item[4]), int(item[5]))
                    import_stands(item[3], 3, 1, 0, 0, int(item[5]), int(item[4]))
                elif item[4] == item[5]:
                    import_stands(item[2], 1, 0, 1, 0, int(item[4]), int(item[5]))
                    import_stands(item[3], 1, 0, 1, 0, int(item[5]), int(item[4]))
            counter += 1
        return season, teams
    except Exception as error:
        print(error)


def show_teams(data):
    try:
        for item in data:
            print(item)
    except:
        print('Unknown Error')
    input()


def import_stands(team, points, won, draw, lost, hg, ag):
    try:
        n_points = stands[team]['points'] + points
        n_won = stands[team]['won'] + won
        n_draw = stands[team]['draw'] + draw
        n_lost = stands[team]['lost'] + lost
        n_hg = stands[team]['hg'] + hg
        n_ag = stands[team]['ag'] + ag
    except:
        n_points = points
        n_won = won
        n_draw = draw
        n_lost = lost
        n_hg = hg
        n_ag = ag
    finally:
        stands[team] = {'points': n_points, 'won': n_won, 'draw': n_draw, 'lost': n_lost, 'hg': n_hg, 'ag': n_ag }


def show_matches(data):
    try:
        for match in range(2,len(data)):
            match_date = data[match]['Date']
            match_home = data[match]['Home']
            match_away = data[match]['Away']
            match_hg = data[match]['HG']
            match_ag = data[match]['AG']
            print('Date: {} -> {} {} x {} {}'.format(match_date, match_home, match_hg, match_ag, match_away))
    except Exception as error:
        print(error)
    finally:
        input()


def show_stands():
    try:
        sorted_stands = sorted(stands.items(), key=lambda x: x[1]['points'], reverse=True)
        f_stands = dict(sorted_stands)
        print('{:15s} :  {:2s} -  {:2s} - {:2s} - {:2s} -  {:3s} - {:3s} - {:3s}'.format('Team', 'P', 'W', 'D', 'L', 'HG', 'AG', 'GD'))
        for stand in f_stands:
            print('{:15s} : {:3d} - {:3d} - {:2d} - {:2d} - {:3d} - {:3d} - {:3d}'.format(stand, f_stands[stand]['points'],
                                                                  f_stands[stand]['won'], f_stands[stand]['draw'],
                                                                  f_stands[stand]['lost'], f_stands[stand]['hg'],
                                                                  f_stands[stand]['ag'], f_stands[stand]['hg']-f_stands[stand]['ag']))
        input()
    except Exception as error:
        print(error)


def show_matches_team(data, team):
    try:
        for match in range(1,len(data)):
            if data[match]['Home'] == team or data[match]['Away'] == team:
                match_date = data[match]['Date']
                match_home = data[match]['Home']
                match_away = data[match]['Away']
                match_hg = data[match]['HG']
                match_ag = data[match]['AG']
                print('Date: {} -> {} {} x {} {}'.format(match_date, match_home, match_hg, match_ag, match_away))
    except Exception as error:
        print(error)
    finally:
        input()


def print_menu():
    print('------------------------------------------')
    print('1 - Show all matches')
    print('2 - Show all teams')
    print('3 - Matches for team')
    print('4 - Stands')
    print('9 - Load file')
    print('E - End program')
    print('------------------------------------------')
    print('')



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
       show_stands()
    elif option == '9':
        stands = {}
        myfile = choose_file()
        mydata = open_csv_file(myfile, 'r')
        mymatches, myteams = import_data(mydata)

    elif option == 'E' or option == 'e':
        print('Finishing...')
        break
    else:
        print('Invalid Option')
