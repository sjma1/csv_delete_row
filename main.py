#Seong Ma


import functions 

'''
This program is used to automate the process of deleting a row from multiple .csv files.
It will ask the user to input a directory and a row number and then edit the .csv files
along that directory by deleting the specified row
'''

if __name__ == '__main__':
    functions.delete_rows(functions.get_directory(), functions.get_row())