1.) Identifying Information
 a. Full Name: Noah Estrada-Rand
 b. Student ID: 2272490
 c. Chapman email: estra146@mail.chapman.edu
 d. Course number and section: 408-01
 e. Assignment Number: 3 

2.) List of source files submitted
a. Main.py
b. DbHelper.py
c. FakeGenerator.py
d. ddl.sql

3.) Description of any known compile/runtime errors, or bugs.
 a. Error may occur if machine running the script is not registered on the Google Cloud platform

4.) References used to complete the assignment
a. stackoverflow.com
b. w3schools.com
c. dev.mysql.com
d. THE Rene German

5.) Instructions for running Assignment

1.) Pull the repository from git.
2.) Change directories to the correct directory with Main.py.
3.) Ensure that correct dependencies are installed (mysql.connector, pandas,numpy,Faker)
4.) Before running, open the file DbHelper.py and edit the information displayed to match your Google Cloud Platform
instance information.  This program assumes you have an instance already running.
5.) Run the ddl.sql file provided in your database console to create the necessary tables to interact with the data import functionality.
6.) Run the application using the format: python Main.py [option] [filename] [number of records*]
7.) [Option] - 'generate' (create new data for given csv), 'import' (used to import all data to normalized db)
8.) [Filename] (name of the csv file including extension)
9.) [Number of records*] - only needed if populating data to specify how many rows to populate.