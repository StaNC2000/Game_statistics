
from printing import *
import os

def main():

    is_running = True
    
    display_logo()

    while is_running:
        
        games = read_file('file_name')

        display_menu()
        
        user_input = input()

        if user_input == 'E':
            print_table_full(read_file)
        elif user_input == '1':
            print_table_full(games)
        elif user_input == '2':
            number_of_lines(games)
        elif user_input == '3':
            if user_input == '':
                print_table_full(games)
            else:
                search_by_game_title(games)
        elif user_input == '4':
            search_by_publisher(games)
        elif user_input == '5':
            search_by_genere(games)
        elif user_input == '6':
            search_by_year(games)
        elif user_input == '7':
            search_by_value(games)
        elif user_input == ('A' or 'a'):
            enter_new('game_stat.txt')
        elif user_input == '0':
            is_running = False
            print('Bye Bye')

main()