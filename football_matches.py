# This script, opens a CSV file with football data
# Save it on a DICT
# And present it as you wish

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
        teams = {''}
        counter = 1
        for match in data:
            item = match.strip().split(',')
            season[counter] = {'Date': item[1], 'Home': item[2], 'Away': item[3], 'HG': item[4], 'AG': item[5]}
            teams.add(item[2])
            teams.add(item[3])
            counter += 1
        teams.remove('')
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
            match_date = data[match+1]['Date']
            match_home = data[match+1]['Home']
            match_away = data[match+1]['Away']
            match_hg = data[match+1]['HG']
            match_ag = data[match+1]['AG']
            print('Date: {} -> {} {} x {} {}'.format(match_date, match_home, match_hg, match_ag, match_away))
    except:
        print('Unknown error')
    finally:
        input()

def show_matches_team(data, team):
    try:
        team_away = 0
        team_home = 0
        team_win = 0
        team_draw = 0
        team_lose = 0
        for match in range(len(data)):
            if data[match+1]['Home'] == team or data[match+1]['Away'] == team:
                match_date = data[match+1]['Date']
                match_home = data[match+1]['Home']
                match_away = data[match+1]['Away']
                match_hg = data[match+1]['HG']
                match_ag = data[match+1]['AG']
                print('Date: {} -> {} {} x {} {}'.format(match_date, match_home, match_hg, match_ag, match_away))
                if match_home == team:
                    team_home += 1
                    if match_hg > match_ag:
                        team_win += 1
                    elif match_hg < match_ag:
                        team_lose += 1
                    elif match_hg == match_ag:
                        team_draw += 1
                elif match_away == team:
                    team_away += 1
                    if match_hg > match_ag:
                        team_lose += 1
                    elif match_hg < match_ag:
                        team_win += 1
                    elif match_hg == match_ag:
                        team_draw += 1
        print('--- Sumary ---')
        print('Matches at home: ', team_home)
        print('Matchas Away   : ', team_away)
        print('Wins           : ', team_win)
        print('Draws          : ', team_draw)
        print('Loses          : ', team_lose)
        print('Total Points   : ', (team_win*3)+(team_draw))

    except:
        print('Unknown error')
    finally:
        input()

def print_menu():
    print('------------------------------------------')
    print('1 - Show all matches')
    print('2 - Show all teams')
    print('3 - Matches for team')
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
    elif option== '3' or option == '4':
        myteam = input('Choose the team: ')
        show_matches_team(mymatches, myteam)
    elif option == '5':
        pass
    elif option == 'E' or option == 'e':
        print('Finishing...')
        break
    else:
        print('Invalid Option')
