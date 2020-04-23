import sys
import FakeGenerator as fg
import pandas as pd
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
        if action == 'parse':
            try:
                with open(file_name,'r') as reader:
                    print('do some stuff here for reading and writing ')

            except Exception as e:
                print('There was an error attempting to read specified file.')
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
                   print(df.head())






           except Exception as e:
               print('Invalid input entered, please try again.')
               print(e)
               exit(1)








if __name__ == '__main__':
    main()