import pymysql

def connect_to_database():
    try:
        connection = pymysql.connect(
            host='192.168.0.100',
            user='username',
            password='password',
            database='dbname'
        )
        print("Connected to MySQL database using PyMySQL")

    except pymysql.MySQLError as e:
        print("Error while connecting to MySQL:", e)

    finally:
        if 'connection' in locals():
            connection.close()
            print("MySQL connection is closed")

connect_to_database()
