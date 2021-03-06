'''
Name: Noah Estrada-Rand
Student ID#: 2272490
Chapman email: estra146@mail.chapman.edu
Course Number and Section: CPSC-408-01
Assignment: Assignment 3
'''
import sys
import FakeGenerator as fg
import pandas as pd
import numpy as np
from DbHelper import Helper


'''
The main method is simply checking for command line arguments and if they are found, either populating data 
to provided filename or reading in the data from a given file and inserting/normalizing it into my db.
'''
def main():
    #check if command line arguments were give, if not tell the user
    args = sys.argv
    if len(args) <= 2:
        if len(args) <= 1:
            print('Failed to execute, command line arguments missing')
            exit(1)
        print('Failed to execute, filename missing from command line arguments')
        exit(1)
    else:
        action = args[1].lower()
        file_name = args[2]
        #handle the import functionality
        if action == 'import':
            db = Helper()
            try:
                df = pd.read_csv(file_name)
                df = df.replace({np.nan: None})
                print('Data found...')
                print(df.head())
                print('Importing...')
                #iterate over all tuples and insert into normalized tables
                for row in df.itertuples():
                    #attempt to enter new user
                    newest_id = db.insert_new_user(row.password,row.lastLogin,row.issuper,row.username,
                                                   row.firstName,row.lastName,row.email,row.isstaff,row.isactive,
                                                   row.dateJoined)
                    #if user exists, get their user id based on their username
                    if newest_id is None:
                        newest_id = db.get_user_id(row.username)
                    db.insert_new_bet(newest_id,row.spent,row.sport,row.won,row.dateRecorded,row.dateEnded,'Description here')
                print('Data Import Successful to {database} database!'.format(database = db.get_database_name()))

            except Exception as e:
                print('There was an error attempting to process specified file.')
                print(e)
                exit(1)
            finally:
                #close all connections in the db class
                db.close_connections()
        #Handles user input and generates data based on input
        elif action == 'generate':
            if len(args) > 3:
                try:
                    how_many = int(args[3])
                    if how_many <= 0:
                       print('You must enter a positive integer to populate the file you specified.')
                       exit(1)
                    else:
                       new_data = fg.get_fake_tuples(how_many)
                       df = pd.DataFrame(new_data,columns = new_data[0].keys())
                       df.to_csv(file_name,index=False)
                       print('{rows} rows generated to file {file} successfully!'.format(file = file_name,rows = how_many))
                except Exception as e:
                   print('Invalid input entered, please try again.')
                   print(e)
                   exit(1)
            else:
                print('Command line parameter missing for number of records to produce')








if __name__ == '__main__':
    main()