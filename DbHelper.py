import mysql.connector


##main class is helper
class Helper:
    ##pass path to db in to establish connection
    def __init__(self,host,user,passwd,database):
        self.db = mysql.connector.connect(
                    host=host,
                    user=user,
                    passwd=passwd,
                    database=database
                )
        self.c = self.db.cursor()

    ###returns the id of the last entry
    #returns the primary key of the latest entry
    def insert_new_user(self,passwd,last_login,superuser,userName,firstName,lastName,email,isStaff,isActive,dateJoined):
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
        self.c.execute('SELECT SportId '
                       'FROM Sports '
                       'WHERE Sport = %s',(the_sport,))

        return self.c.fetchall()[0][0]

    def get_user_id(self,new_username):
        try:
            self.c.execute('SELECT id '
                           'FROM auth_user '
                           'WHERE username = %s',(new_username,))
        except:
            return None
        return self.c.fetchall()[0][0]

    def insert_new_bet(self,id,new_spend,new_sport,win_status,recorded_date,ended_date,new_description):
        new_tuple = [id,new_spend,new_sport,win_status,recorded_date,ended_date,new_description]
        self.c.callproc('Insert_New_Bet',new_tuple)
        return True

    def commit_transaction(self):
        self.db.commit()
    def rollback_transaction(self):
        self.db.rollback()
    def close_connections(self):
        self.db.close()
        self.c.close()
