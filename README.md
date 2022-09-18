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
 1 | 0:00:09.396509 | 0:00:09.432330 | 0:00:09.486554 |
 2 | 0:00:06.418410 | 0:00:06.418707 | 0:00:06.427257 |
 0 | 0:00:07.734345 | 0:00:07.753723 | 0:00:07.761428 |

CREATE INDEX Users_Birthday_BTREE USING BTREE ON Users (Birthday ASC);
CREATE INDEX Users_Birthday_HASH USING HASH ON Users (Birthday);




1
0:00:09.396509
0:00:09.432330
0:00:09.486554
2
0:00:06.418410
0:00:06.418707
0:00:06.427257
3
0:00:07.734345
0:00:07.753723
0:00:07.761428
