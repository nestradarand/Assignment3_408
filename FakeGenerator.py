'''
Name: Noah Estrada-Rand
Student ID#: 2272490
Chapman email: estra146@mail.chapman.edu
Course Number and Section: CPSC-408-01
Assignment: Assignment 3
'''


from faker import Faker
import random
from datetime import datetime

SPORTS = ['Baseball','Basketball','Casino','Football','Hockey','Horses','Other']


def get_fake_tuples(num_records:int) -> list:
    """This method is simply to produce a flat table in the form of a list of tuples.

    Arguments:
        num_records {int} -- The number of records to produce and return as a list of tuples

    Returns:
        list -- A list of tuples containing fake randomized data from Faker to fit the tables of my current db project.
    """    
    fake = Faker()
    new_rows = []
    for i in range(num_records):
        try:
            date_joined = fake.date()
            profile = fake.simple_profile()
            #make sure they record the bet after they have joined the website
            date_recorded = fake.date_between_dates(date_start = datetime.strptime(date_joined,"%Y-%M-%d"))
            #determine if the bet was one or lost or in progress (null if in progress)
            status = random.randint(0,2)
            if status != 0 and status != 1:
                status = None
            date_ended = None
            #if the bet was won or lost we need the date when it was settled
            if status is not None:
                date_ended = fake.date_between_dates(date_start = date_recorded)
            new_rows.append(
                {'username':profile.get('username'),
                 'password':fake.password(),
                 'email':profile.get('mail'),
                 'firstName':fake.first_name(),
                 'lastName':fake.last_name(),
                 'spent':random.randint(1,201),
                 'sport':SPORTS[random.randint(0,6)],
                 'won':status,
                 'lastLogin': fake.date_between_dates(date_start = datetime.strptime(date_joined,"%Y-%M-%d")),
                 'dateJoined':date_joined,
                 'dateRecorded':date_recorded,
                 'dateEnded':date_ended,
                 'isactive':random.randint(0,1),
                 'isstaff':0,
                 'issuper':0}
            )
        except Exception as e:
            print('skipped')
            print('Because of error', e)
    return new_rows
