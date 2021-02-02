import sys
import snotestacks as snack
import Entry

# noinspection SpellCheckingInspection
stack_filename = '/home/saint-rivers/SnoteEntries/snote_entries.txt'

# noinspection SpellCheckingInspection
command_not_found_message = "no such command listed\n" \
                            "run 'snote help' for commands I can run"


command_dict = dict(
    stack=snack.stack_run,
    stackread=snack.read_stack,
    stacknew=snack.new_entry
)

if __name__ == '__main__':

    # combine user's space separated input into command
    user_command = ""
    for i in range(1, len(sys.argv)):
        user_command += str(sys.argv[i])

    # run that command
    try:
        command_dict[user_command](stack_filename)
    except KeyError:
        print(command_not_found_message)


