from faker import Faker
import random
from datetime import datetime

SPORTS = ['Baseball','Basketball','Casino','Football','Hockey','Horses','Other']


def get_fake_tuples(num_records:int) -> list:
    fake = Faker()
    new_rows = []
    for i in range(num_records):
        profile = fake.simple_profile()
        date_recorded = fake.date()
        password = fake.password()
        new_email = profile.get('mail')
        new_name = profile.get('name')
        username = profile.get('username')
        spent = random.randint(1,201)
        sport = SPORTS[random.randint(0,6)]
        status = random.randint(0,2)
        if status != 0 and status != 1:
            status = None
        date_ended = None
        #if the bet was won or lost we need the date when it was settled
        if status is not None:
            date_ended = fake.date_between_dates(datetime.strptime(date_recorded,"%Y-%M-%d"))
        new_rows.append(
            {'username':username,
             'password':password,
             'email':new_email,
             'name':new_name,
             'spent':spent,
             'sport':sport,
             'won':status,
             'dateRecorded':date_recorded,
             'dateEnded':date_ended}
        )
    return new_rows
