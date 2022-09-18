import random
import string
import datetime
import pandas as pd
from sqlalchemy import create_engine
import time

def get_birthday():
    return datetime.datetime(random.randrange(1900, 2021), random.randrange(1, 12), random.randrange(1, 28)).date()

def get_name():
    return ''.join(random.choice(string.ascii_letters + ' ') for i in range(random.randrange(20, 50)))

engine = create_engine('mysql+pymysql://my_user:my_password@localhost/my_db')
with engine.connect() as conn:
    ctq = "CREATE TABLE Users (Id int NOT NULL AUTO_INCREMENT, Name varchar(250) NOT NULL, Birthday DATE NOT NULL, PRIMARY KEY (Id))"
    result = conn.execute(ctq)
    #ctq = "CREATE INDEX Users_Birthday_BTREE USING BTREE ON Users (Birthday ASC);"
    #ctq = "CREATE INDEX Users_Birthday_HASH USING HASH ON Users (Birthday);"
    #result = conn.execute(ctq)
    print('Created table Users')

for i in range(40):
    users = [[get_name(), get_birthday()] for i in range(1000000)]
    print(f"Prepared 1M of users")
    df = pd.DataFrame(users, columns=['name', 'birthday'])
    df.to_sql('Users', con = engine, if_exists='append', index=False, chunksize=10000)
    print(f"Added 1M rows to Users ({i+1})")





# import threading 
  
# def print_hello_three_times():
#   for i in range(3):
#     print("Hello")
  
# def print_hi_three_times(): 
#     for i in range(3): 
#       print("Hi") 

# t1 = threading.Thread(target=print_hello_three_times)  
# t2 = threading.Thread(target=print_hi_three_times)  

# t1.start()
# t2.start()    