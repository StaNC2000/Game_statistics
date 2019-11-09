import os

def print_table_full(games):
    os.system('clear')
    for game in games:
            
        line = 170 * '-'
        double_line = 170 *'='
        title = str(game[0])
        value = str(game[1])
        year = str(game[2])
        genere = str(game[3])
        publisher = str(game[4])

        print(' |' +  line.ljust(1, '-') + '|')
        print(' | ' + title.ljust(55), ' | ' + value.ljust(20) +  ' | ' + year.ljust(20), ' | ' + genere.ljust(30)+ ' | ' + publisher.ljust(30) + '| ')
    print(' |' +  double_line.ljust(1, '=') + '|')
        
def print_table_2(games):
    '''Print table inventory = yours dict, order ascending or descending by default None''' 
    line = 170 * '-'
    double_line = 170 * '='
    title = str(games[0][0:])
    value = str(games[1])
    year = str(games[2])
    genere = str(games[3])
    publisher = str(games[4])
    
    print(' |' +  line.ljust(1, '-') + '|')
    print(' | ' + title.ljust(55), ' | ' + value.ljust(20) +  ' | ' + year.ljust(20), ' | ' + genere.ljust(30)+ ' | ' + publisher.ljust(30) + '| ')
    # print(' |' +  double_line.ljust(1, '=') + '|')
    
    # print(dot.rjust(18, '.') + '\n')
    # if order=="count,asc": 
    #     for key, value in sorted(games.items(), key=lambda kv: (-kv[1], kv[0])):
    #         print(key.rjust(10), '|' + str(value).rjust(6) + '\n')
    # elif order=="count,desc":
    #     for key, value in sorted(games.items(), key=lambda kv: (-kv[1], kv[0]), reverse=True):
    #         print(key.rjust(10 ), '|' + str(value).rjust(6) + '\n')
    # print(dot.rjust(18, '.') + '\n')

def display_logo():

    print('''

                                   _____      ____       __    __      _____      ______      _____   _____      ____     ______     ________  
                                  / ___ \    (    )      \ \  / /     / ___/     (   __ \    / ___/  (  __ \    / __ \   (   __ \   (___  ___) 
                                 / /   \_)   / /\ \      () \/ ()    ( (__        ) (__) )  ( (__     ) )_) )  / /  \ \   ) (__) )      ) )    
                                ( (  ____   ( (__) )     / _  _ \     ) __)      (    __/    ) __)   (  ___/  ( ()  () ) (    __/      ( (     
                                ( ( (__  )   )    (     / / \/ \ \   ( (          ) \ \  _  ( (       ) )     ( ()  () )  ) \ \  _      ) )    
                                 \ \__/ /   /  /\  \   /_/      \_\   \ \___     ( ( \ \_))  \ \___  ( (       \ \__/ /  ( ( \ \_))    ( (     
                                  \____/   /__(  )__\ (/          \)   \____\     )_) \__/    \____\ /__\       \____/    )_) \__/     /__\    
                                                                                                                                                                                                                                                    
                                                                          __  __                  
                                                                            \/  | ___ _ __  _   _ 
                                                                           |\/| |/ _ \ '_ \| | | |
                                                                           |  | |  __/ | | | |_| |
                                                                          _|  |_|\___|_| |_|\__,_|
                                                                
                ''')

def display_menu():
        print('''

                                                                |***************************************|
                                                                |   1 -> Display All                    |
                                                                |   2 -> Show number of games in file   |
                                                                |   3 -> Search by game title           |
                                                                |   4 -> Search by publisher            |
                                                                |   5 -> Search by genere               |
                                                                |   6 -> Search by year                 |
                                                                |   7 -> Search for sale value          |
                                                                |   8 ->                                |
                                                                |   9 -> Find shortest/longest album    |
                                                                |   0 -> Exit                           |
                                                                |_______________________________________|
                                                    ''')


def number_of_lines(games):
    os.system('clear')
    for game in games:
        print('Number of games in file ', len(games))
        break

def search_by_game_title(games):
    os.system('clear')
    game_title = input('Please enter game title: ')
    print(chr(27) + "[2J")
    for game in games:
        title = game[0]
        if game_title.upper() in title.upper():
            print_table_2(game)
            # print(' | ' .join(game))

def search_by_publisher(games):
    os.system('clear')
    game_publisher = input('Please enter name of publisher: ')
    print(chr(27) + "[2J")
    for game in games:
        publisher = game[4]
        if game_publisher.upper() in publisher.upper():
            print_table_2(game)

def search_by_year(games):
    os.system('clear')
    year = input('Enter year of publishing: (e.g. 1997: ')
    print(chr(27) + "[2J")
    for game in games:
        year_published = game[2]
        if year_published == year:
            print_table_2(game)

def search_by_genere(games):
    os.system('clear')
    genere_input = input('Please enter genere: ')
    print(chr(27) + "[2J")
    output_games = []
    for game in games:
        genere = game[3]
        if genere_input.upper() in genere.upper():
            genere_number = len(game)
            print(' | ' .join(game))
            output_games.append(game)
    for output in output_games:
        out = output[3]
        
    print()
    print('Total number of games: ', out, len(output_games))

def search_by_value(games):
    os.system('clear')
    # sale_value = input('Please enter year: ')
    print(chr(27) + "[2J")
    for game in games:
        value = game[1]
        # value = float(value)
        print(value)
        # if value == game:
        #     print(max(' | ' .join(game)))

def duration_to_seconds(albums): # duration = 42:20
    print(chr(27) + "[2J")
    minutes_seconds = albums # minutes_seconds = ['42', '21']
    albums  = albums.split(':')
    seconds = int(minutes_seconds[1]) + int(minutes_seconds[0]) * 60
    return seconds


def read_file(file_name):
    run_read = True

    while run_read:

        try:
            game_temp = []
            game_list = []
            # file_name = input('Enter full filname inculded extension: ')
            file_name = ('game_stat.txt')
            with open(file_name) as file:
                file = file.read().strip().split('\n')
                for element in file:
                    game_temp.append(element.split(','))
                for element in file:
                    game_list.append(element.split('\t'))
                break
        except FileNotFoundError:
            text = print('File not found. ')
    return game_list

    run_read = False


def enter_new (file_name):
    os.system('clear')
    
    new_entry = []

    with open(file_name, 'a+') as file:

        title = input('Enter full tile of the game: ')
        new_entry.append(title)
        value = float(input('Enter full value sale: '))
        new_entry.append(str(value))
        year_out = int(input('Enter game out year: '))
        new_entry.append(str(year_out))
        genere = input('''Enter genere: ''')
        new_entry.append(genere)
        publisher = input('Enter the name of game publisher: ')
        new_entry.append(publisher)
        print('\n', new_entry)
    
        file.write('\n' + str(title) + '\t' + str(value) + '\t' + str(year_out) + '\t' + str(genere) + '\t' + str(publisher))


