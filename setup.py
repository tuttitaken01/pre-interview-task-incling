import psycopg2
import os

# establish connection
conn = psycopg2.connect(
    database='postgres', user='', password='', host='127.0.0.1', port='5432'
)
conn.autocommit = True

# create cursor object and set up database
cursor = conn.cursor()
cursor.execute('DROP DATABASE IF EXISTS task_db')

sql = '''CREATE DATABASE task_db'''
cursor.execute(sql)
print('Database created successfully......')

# Close connection
conn.close()

# Run migrations and load data from fixtures
os.system('python manage.py makemigrations')
os.system('python manage.py migrate')
os.system('python manage.py loaddata */fixtures/*.json')