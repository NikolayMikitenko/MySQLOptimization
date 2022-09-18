# MySQLOptimization

docker-compose exec mysql sh
mysql -uroot -p
my_password

CREATE DATABASE my_db;
CREATE USER 'my_user'@'%' IDENTIFIED WITH mysql_native_password BY 'my_password';
USE my_db;
GRANT ALL PRIVILEGES ON * TO 'my_user'@'%';
FLUSH PRIVILEGES;

#conda deactivate
#conda env remove --name mysqlperfomance
conda create --name mysqlperfomance python==3.9
conda activate mysqlperfomance
#conda install mysql-connector-python
#conda install sqlalchemy
conda install pandas
conda install pymysql
python addusers.py



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