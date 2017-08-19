import os, send2trash, csv

def get_directory():
    while True:
        directory = input("Input directory: ")
        if os.path.isdir(directory):
            return directory
        print('INVALID PATH\n')
        
def get_row():
    while True:
        row = input("Input row number to be deleted: ")
        if row < 1:
            print("INVALID ROW NUMBER, MUST BE 1 OR HIGHER\N")
        return row
    
def valid_csv(filename, row_num):
    with open(filename) as file:
        return filename.endswith('.csv') and row_num in range(1, len(list(csv.reader(file))) + 1)
 
 

def copy_csv(directory, file, row_num):
    absolute_directory = os.path.abspath(directory)
    absolute_filename  = os.path.join(absolute_directory, file)
    os.chdir(absolute_directory)
    with open(absolute_filename) as f:
        csv_reader = csv.reader(f)
        csv_rows   = list(csv_reader)
        with open(_create_new_filename(file, row_num), 'w') as new_file:
            pass
 
def delete_rows(directory, row_num):
    for dir_name, subdir_list, file_list in os.walk(directory):
        for file in file_list:
            if valid_csv(file, row_num):
                pass


def _create_new_filename(filename, row_num):
    return 'row' + str(row_num) + '_' + filename