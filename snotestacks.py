import datetime

# noinspection SpellCheckingInspection
timech = 27


def attempt_entry_write(entry_file, msg):
    try:
        entered_line = input(msg + ' << ')
    except KeyboardInterrupt:
        print('\n')
        return False
    except ValueError:
        print('please input only strings')
        return True
    else:
        entry_file.write(stamp_time(entered_line) + '\n')
    return True


def stack_run(filename):
    with open(filename, 'a') as entry_file:
        is_operating = attempt_entry_write(entry_file, 'start typing')
        while is_operating:
            is_operating = attempt_entry_write(entry_file, 'keep typing')
    print('recorded')


def read_stack(filename):
    with open(filename, 'r') as stack_file:
        for line in stack_file.readlines():
            print(" " + line, end='')


def read_simple(filename):
    with open(filename, 'r') as stack_file:
        for line in stack_file.readlines():
            print(" " + line[timech:], end='')


def quick_write(filename, entry):
    with open(filename, 'a') as entry_file:
        entry_file.write((stamp_time(entry) + '\n'))
        print("recorded.")


def stamp_time(usr_str):
    x = datetime.datetime.now()
    return str(x.strftime("%c")) + ":  " + usr_str
