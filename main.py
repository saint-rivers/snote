import sys
import snotestacks as snack
import os

global user_command

dir_path = os.path.dirname(os.path.realpath(__file__))

# noinspection SpellCheckingInspection
stack_filename = dir_path + '/main_snote_entries.txt'

# noinspection SpellCheckingInspection
command_not_found_message = "command not listed" \
                            "\nrun 'snote help' for commands I can run"


def get_help_input():
    try:
        command = str(input('Enter command: '))
        return command.replace(" ", "")
    except KeyboardInterrupt:
        print('\n')
        exit(0)


def display_menu():
    global user_command
    print("type 'stack' to enter entry mode")
    print("type 'read' to display all entries")
    print("type 'read simple' to display without timestamps")
    user_command = get_help_input()


command_dict = dict(
    read=snack.read_stack,
    stack=snack.stack_run,
    reads=snack.read_simple,
    readsimple=snack.read_simple,
    help=display_menu,
    q=snack.quick_write
)

if __name__ == '__main__':

    # combine user's space separated input into command
    user_command = ""
    entry = ""

    if len(sys.argv) == 1:
        snack.stack_run(stack_filename) # run default function
        exit(0)
    elif sys.argv[1] == 'help':
        display_menu()
    elif sys.argv[1] != '':
        for i in range(1, len(sys.argv)):
            user_command += str(sys.argv[i])
    else:
        try:
            user_command = str(sys.argv[1])
            for i in range(2, len(sys.argv)):
                entry += str(sys.argv[i]) + " "
        except IndexError:
            print(command_not_found_message)

    # run that command
    try:
        command_dict[user_command](stack_filename, entry)
    except TypeError:
        command_dict[user_command](stack_filename)
    except KeyError:
        print(command_not_found_message)
