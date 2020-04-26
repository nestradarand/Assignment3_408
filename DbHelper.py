'''
Name: Noah Estrada-Rand
Student ID#: 2272490
Chapman email: estra146@mail.chapman.edu
Course Number and Section: CPSC-408-01
Assignment: Assignment 3
'''
import mysql.connector


##config info for my gcp instance
HOST = '34.83.232.253'
USER = 'noah_e'
PASSWORD = 'Chapman1!'
DATABASE = 'Chapman_2'

class Helper:
    #constructor
    def __init__(self):
        try:
            #establish connection and cursor
            self.db = mysql.connector.connect(
                        host=HOST,
                        user=USER,
                        passwd=PASSWORD,
                        database=DATABASE
                    )
            self.c = self.db.cursor()
        except:
            print('Error encountered trying to connect to gcp instance, please ensure correct configuration.')

    ###returns the id of the last entry
    #returns the primary key of the latest entry
    def insert_new_user(self,passwd,last_login,superuser,userName,firstName,lastName,email,isStaff,isActive,dateJoined):
        """Method used to insert a new user into the Chapman_2 database

        Arguments:
            passwd {string} -- new password for the user
            last_login {string} -- last date the user logged in
            superuser {boolean} -- if the user is an admin
            userName {string} -- new username for user
            firstName {string} -- first name for user
            lastName {string} -- last name for user
            email {string} -- new email for user
            isStaff {bool} -- indicates if the user is staff
            isActive {bool} -- indicates if the user still has an account
            dateJoined {datetime} -- date when the user joined

        Returns:
            int -- id of the last row entered if new user, otherwise returns None if user exists
        """        
        new_data = (passwd,last_login,superuser,userName,firstName,lastName,email,isStaff,isActive,dateJoined)
        try:
            self.c.execute('INSERT INTO auth_user(password,last_login,is_superuser,username, '
                           'first_name,last_name,email,is_staff,is_active,date_joined) '
                           'VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',new_data)
            self.db.commit()
        except Exception as e:
            return None
        return self.c.lastrowid

    def get_sport_id(self,the_sport:str):
        """Used to look up a sport in the Sports table

        Arguments:
            the_sport {string} -- Name of the sport that will be looked up

        Returns:
            integer -- the sport id of the sport looked for
        """        
        self.c.execute('SELECT SportId '
                       'FROM Sports '
                       'WHERE Sport = %s',(the_sport,))
        return self.c.fetchall()[0][0]

    def get_user_id(self,new_username):
        """Used to get the user id of someone based on their username

        Arguments:
            new_username {string} -- username to search

        Returns:
            integer -- returns number of the found user, otherwise None if not in table
        """        
        try:
            self.c.execute('SELECT id '
                           'FROM auth_user '
                           'WHERE username = %s',(new_username,))
        except:
            return None
        return self.c.fetchall()[0][0]

    def insert_new_bet(self,id,new_spend,new_sport,win_status,recorded_date,ended_date,new_description):
        """Method to call the stored procedure to insert a new bet record

        Arguments:
            id {integer} -- user id to base insertion on
            new_spend {integer} -- amount wagered for bet
            new_sport {string} -- sport to insert for record
            win_status {boolean} -- indicator of whether a bet was won lost or in progress
            recorded_date {datetime} -- date at the time of recording
            ended_date {datetime} -- when the bet terminated
            new_description {string} -- notes entered concerning the bet

        Returns:
            boolean -- true if successfully run
        """        
        try:
            new_tuple = [id,new_spend,new_sport,win_status,recorded_date,ended_date,new_description]
            self.c.callproc('Insert_New_Bet',new_tuple)
            return True
        except:
            print('Error occured attempting to enter new bet using stored procedure.')
            return False

    def close_connections(self):
        """Used to close all connections 
        """        
        self.db.close()
        self.c.close()
    def get_database_name(self):
        '''Used to return the name of the current databse'''
        return DATABASE
