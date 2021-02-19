import datetime

# noinspection SpellCheckingInspection
TIME_BUFFER = 13


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


def quick_write(filename, entry):
    with open(filename, 'a') as entry_file:
        entry_file.write((stamp_time(entry) + '\n'))
        print("recorded.")


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
            print(" " + line[TIME_BUFFER:], end='')


def stamp_time(usr_str):
    today = datetime.date.today()
    return str(today) + ":  " + usr_str


def get_today_entry(filename):
    today = datetime.date.today()
    with open(filename, 'r') as stack_file:
        for line in stack_file.readlines():
            entry_date = line[0:TIME_BUFFER - 3]
            if entry_date == str(today):
                print(line, end='')


def read_recent(filename):
    with open(filename, 'r') as stack_file:
        for line in stack_file.readlines():
            pass