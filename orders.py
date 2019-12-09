

def open_print_txt_file(file_name):
    try:
        opened_file = open(file_name, 'r')
        lines = opened_file.readlines()
        for line in lines:
            print(line.strip())

        opened_file.close() # closes the file so that it can be saved without conflict

    except FileNotFoundError as errormessage: #errormessage captures the original message
        print('Check file name exists - file name cannot be found ')
        print(errormessage) # prints the original message
        raise # can still raise the error message and break the rest of the code from running.

#with automatically opens and closes the file for you
def open_print_close(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                print(line.strip())

    except FileNotFoundError as error:
        print('Check your file ')
        print(error)

    finally: # finally is looked at the end, the last thing to check
        print('//// Programme Closing - execution done!')

# open_print_txt_file('order.txt')
# open_print_txt_file('order2.txt')

open_print_close('order.txt')
open_print_close('order2.txt')