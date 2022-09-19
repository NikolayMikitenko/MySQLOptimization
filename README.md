# MySQLOptimization 

## 1. Run container 
`docker-compose up` 

## 2. Create db and give permissions 
```
docker-compose exec mysql sh
mysql -uroot -p
my_password

CREATE DATABASE my_db;
CREATE USER 'my_user'@'%' IDENTIFIED WITH mysql_native_password BY 'my_password';
USE my_db;
GRANT ALL PRIVILEGES ON * TO 'my_user'@'%';
FLUSH PRIVILEGES;
``` 

## 3. Create conda environment for run python code 
```
conda create --name mysqlperfomance python==3.9
conda activate mysqlperfomance
conda install sqlalchemy
conda install pandas
conda install pymysql
``` 

## 4. Change innodb_flush_log_at_trx_commit value in file ./mysql/my.cnf and run tests
```
python addusers.py
``` 

 innodb_flush_log_at_trx_commit | thread 1 | thread 2 | thread 3 |
 --- | --- | --- | --- | 
 1 | 0:00:09.396509 | 0:00:09.432330 | 0:00:09.486554 |
 2 | 0:00:06.418410 | 0:00:06.418707 | 0:00:06.427257 |
 0 | 0:00:07.734345 | 0:00:07.753723 | 0:00:07.761428 |


## 5. Uncomment line with creating indexes in file addusers.py and run creating 40M users
#ctq = "CREATE INDEX Users_Birthday_BTREE USING BTREE ON Users (Birthday ASC);"
#ctq = "CREATE INDEX Users_Birthday_HASH USING HASH ON Users (Birthday);"
#result = conn.execute(ctq)
    
`python addusers.py` 

 Index | Select query duration |
 --- | --- |
 Without | 27,950s |
 BETREE | 22ms |
 HASH | 19ms |

![WithoutIndex](https://user-images.githubusercontent.com/52753625/190976585-e76ad0e1-08e6-43ef-98b6-70c0bf1c4549.PNG)
![WithBeTreeIndex](https://user-images.githubusercontent.com/52753625/190976627-9caf9c91-b3b2-47f3-b1ec-a9903943af33.PNG)
![WithHashIndex](https://user-images.githubusercontent.com/52753625/190976646-73e7e26a-a1f6-42b5-bf18-6f5b970eae3a.PNG)
