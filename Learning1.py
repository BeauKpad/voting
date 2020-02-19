from builtins import print
from typing import List

import mysql.connector
import re
my_db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='3640Outrage!',
    database='Test_DB'
)
my_cursor = my_db.cursor()
# my_cursor.execute("SELECT * FROM County_Codes")
# codes = my_cursor.fetchall()
# for row in codes:
#     print(row)
#     print("Test")
my_cursor.execute(
    "SELECT column_name FROM information_schema.columns WHERE table_schema = 'Test_DB' AND table_name = 'Current_Voter_Registration_Info_Table'")
column_names = my_cursor.fetchall()
with open("voterColumns.txt", "w") as myFile:
    for row in column_names:
        print(row[0], file=myFile)

# my_cursor.execute("SHOW DATABASES")
#
# for db in my_cursor:
#     print(db)
# my_cursor.execute('CREATE TABLE students (name VARCHAR(255), age INTEGER(10))')
pass
# my_cursor.execute('SHOW TABLES')
# for tb in my_cursor:
#     print(tb)
pass
# sql_student_insert_formula = 'INSERT INTO students (name, age) VALUES (%s, %s)'
# student_1 = ("Rachel", 22)
# print(sql_student_insert_formula)
# print(student_1)
# student_list = [("Sam", 12),
#                 ("LeBeau", 23),
#                 ("Ericka", 12),
#                 ("Pam", 28),
#                 ("Alex", 45),
#                 ]
# my_cursor.executemany(sql_student_insert_formula, student_list)
# my_db.commit()

# sql_county_code_insert_formula = 'INSERT INTO County_Codes (County_Code, County_Name) VALUES (%s, %s)'
# print(sql_county_code_insert_formula)

# f = open("/home/lebeau/Documents/County_Codes.tsv", "r")
# f_string = f.read()
# f_list: List[List[str]] = []
# insert_list = []
# for line in f_string.split('\n'):
#     f_list.append(line.split())
# f_list = list(filter(None, f_list))
# print(f_list)
# for data in f_list:
#     while len(data) > 2:
#         data[1] = data[1] + " " + data[2]
#         del data[2]
#     print(data)
#     insert_list.append(data)
# print(insert_list)
# my_cursor.executemany(sql_county_code_insert_formula, insert_list)
# my_db.commit()
