import os, send2trash, csv

def get_directory():
    while True:
        directory = input("Input directory: ")
        if os.path.isdir(directory):
            return directory
        print('INVALID PATH\n')
        
def get_row():
    while True:
        try:
            row = input("Input row number to be deleted: ")
            if int(row) < 1:
                print("INVALID ROW NUMBER, MUST BE 1 OR HIGHER\n")
            return int(row)
        except:
            print("INPUT MUST BE AN INTEGER!\n")
    
def valid_csv(filename, row_num):
    with open(filename) as file:
        return filename.endswith('.csv') and row_num in range(1, len(list(csv.reader(file))) + 1)


def copy_csv(absolute_filename, row_num):

    with open(absolute_filename) as f:
        csv_reader = csv.reader(f)
        csv_rows   = list(csv_reader)
        with open(_create_new_filename(absolute_filename.split('\\')[-1], row_num), 'w', newline = '') as new_file:
            csv_writer = csv.writer(new_file)
            for index in range(len(csv_rows)):
                if index + 1 != row_num:
                    csv_writer.writerow(csv_rows[index])
 
def delete_rows(directory, row_num):
    for dir_name, subdir_list, file_list in os.walk(directory):
        for file in file_list:
            absolute_directory = os.path.abspath(dir_name)
            absolute_filename  = os.path.join(absolute_directory, file)
            os.chdir(absolute_directory)

            if valid_csv(absolute_filename, row_num):
                print("FOUND")
                copy_csv(file, row_num)
            else:
                print("NOT FOUND")


def _create_new_filename(filename, row_num):
    return 'row' + str(row_num) + 'deleted_' + filename