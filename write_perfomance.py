from sqlalchemy import create_engine
import threading
from datetime import datetime

engine = create_engine('mysql+pymysql://my_user:my_password@localhost/my_db')
with engine.connect() as conn:
    ctq = "CREATE TABLE Users (Id int NOT NULL AUTO_INCREMENT, Name varchar(250) NOT NULL, Birthday DATE NOT NULL, PRIMARY KEY (Id))"
    result = conn.execute(ctq)
    print('Created table Users')

def write_user():
    with engine.connect() as conn:
        start = datetime.now()
        for i in range (1000):
            ctq = "INSERT INTO Users (Name, Birthday) VALUES ('Test Test Test', '2022-01-01')"
            result = conn.execute(ctq)
        end = datetime.now()
        print(end-start)

#0:00:07.002595
  
t1 = threading.Thread(target=write_user)  
t2 = threading.Thread(target=write_user)  
t3 = threading.Thread(target=write_user)  

t1.start()
t2.start()
t3.start()