import sys
import FakeGenerator as fg
import pandas as pd
import numpy as np
from DbHelper import Helper

##config info
HOST = '34.83.232.253'
USER = 'noah_e'
PASSWORD = 'Chapman1!'
DATABASE = 'Chapman_2'
def main():
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
        if action == 'import':
            db = Helper(HOST,USER,PASSWORD,DATABASE)
            try:
                df = pd.read_csv(file_name)
                df = df.replace({np.nan: None})
                for row in df.itertuples():
                    newest_id = db.insert_new_user(row.password,row.lastLogin,row.issuper,row.username,
                                                   row.firstName,row.lastName,row.email,row.isstaff,row.isactive,
                                                   row.dateJoined)

                    if newest_id is None:
                        newest_id = db.get_user_id(row.username)
                    db.insert_new_bet(newest_id,row.spent,row.sport,row.won,row.dateRecorded,row.dateEnded,'Description here')
                db.close_connections()
                print('Data Import Successful to {database} database!'.format(database = DATABASE))

            except Exception as e:
                print('There was an error attempting to process specified file.')
                print(e)
                exit(1)
        elif action == 'populate':
           try:
               how_many = int(input('Enter the number of instances you wish to randomly populate as a whole number:'))
               if how_many <= 0:
                   print('You must enter a positive integer to populate the file you specified.')
                   exit(1)
               else:
                   new_data = fg.get_fake_tuples(how_many)
                   df = pd.DataFrame(new_data,columns = new_data[0].keys())
                   df.to_csv(file_name,index=False)
                   print('{rows} rows populated to file {file} successfully!'.format(file = file_name,rows = how_many))


           except Exception as e:
               print('Invalid input entered, please try again.')
               print(e)
               exit(1)








if __name__ == '__main__':
    main()