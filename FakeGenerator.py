from faker import Faker
import random
from datetime import datetime

SPORTS = ['Baseball','Basketball','Casino','Football','Hockey','Horses','Other']


def get_fake_tuples(num_records:int) -> list:
    fake = Faker()
    new_rows = []
    for i in range(num_records):
        try:
            date_joined = fake.date()
            profile = fake.simple_profile()
            #make sure they record the bet after they have joined the website
            date_recorded = fake.date_between_dates(datetime.strptime(date_joined,"%Y-%M-%d"))
            status = random.randint(0,2)
            if status != 0 and status != 1:
                status = None
            date_ended = None
            #if the bet was won or lost we need the date when it was settled
            if status is not None:
                date_ended = fake.date_between_dates(date_recorded)
            new_rows.append(
                {'username':profile.get('username'),
                 'password':fake.password(),
                 'email':profile.get('mail'),
                 'firstName':fake.first_name(),
                 'lastName':fake.last_name(),
                 'spent':random.randint(1,201),
                 'sport':SPORTS[random.randint(0,6)],
                 'won':status,
                 'dateRecorded':date_recorded,
                 'dateEnded':date_ended,
                 'isactive':random.randint(0,1),
                 'isstaff':0}
            )
        except Exception as e:
            print('skipped')
            print('Because of error', e)
    return new_rows
