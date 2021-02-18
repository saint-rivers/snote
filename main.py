import sys
import snotestacks as snack
import os

global user_command

dir_path = os.path.dirname(os.path.realpath(__file__))

# noinspection SpellCheckingInspection
stack_filename = dir_path + '/main_snote_entries.txt'

# noinspection SpellCheckingInspection
command_not_found_message: str = "command not listed" \
                            "\nrun 'snote help' for commands I can run"


def get_help_input() -> object:
    try:
        command = str(input('Enter command: '))
        return command.replace(" ", "")
    except KeyboardInterrupt:
        print('\n')
        exit(0)


def display_menu():
    print("type 'stack' to enter entry mode")
    print("type 'read' to display all entries")
    print("type 'read simple' to display without timestamps")


def run_interface(filename):
    display_menu()
    run_command(get_help_input(), filename, "")


def run_command(command, filename, entry):
    try:
        command_dict[command](filename, entry)
        return
    except TypeError:
        command_dict[command](filename)
        return
    except KeyError:
        print(command_not_found_message)
        return

    command_dict[command]()


def read_user_commands():
    command = ""
    try:
        for i in range(1, len(sys.argv)):
            command += str(sys.argv[i])
    except TypeError:
        print(command_not_found_message)
    return command


def get_quick_entry():
    entry = ""
    try:
        for i in range(2, len(sys.argv)):
            entry += str(sys.argv[i]) + " "
    except IndexError:
        print(command_not_found_message)
    finally:
        return entry


command_dict = dict(
    read=snack.read_stack,
    stack=snack.stack_run,
    reads=snack.read_simple,
    readsimple=snack.read_simple,
    help=run_interface
)

if __name__ == '__main__':

    user_command = ""
    q_entry = ""

    # run default function
    if len(sys.argv) == 1:
        user_command = 'stack'

    # check if it is a quick entry
    elif sys.argv[1] == 'q':
        # add every subsequent parameters as an entry
        q_entry = get_quick_entry()

    # if it's not a quick entry
    else:
        user_command = read_user_commands()

    run_command(user_command, stack_filename, q_entry)
