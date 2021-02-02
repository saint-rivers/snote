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
        entry_file.write(entered_line + '\n')
    return True


def stack_run(filename):
    with open(filename, 'a') as entry_file:
        is_operating = attempt_entry_write(entry_file, 'start typing')
        while is_operating:
            is_operating = attempt_entry_write(entry_file, 'keep typing')


def read_stack(filename):
    with open(filename, 'r') as stack_file:
        for line in stack_file.readlines():
            print(line, end='')


def stack_delete(filename):
    user_input = str(input('are you sure you want to erase all entries? [y/n]'))
    print(user_input)


def new_entry():
    #with open(filename, 'w') as new_file:
    return
