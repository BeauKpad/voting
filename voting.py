import mysql.connector
import csv


def populate_voter_db_from_file(file_name, mycursor):
    columns = []
    with open("voterColumns.txt") as columnFile:
        reader = csv.reader(columnFile, delimiter='\t')
        for row in reader:
            columns.append(row)
    # print(columns)
    bigdata = []
    with open(file_name) as datafile:
        reader = csv.reader(datafile, delimiter='\t')
        for myrow in reader:
            bigdata.append(myrow)
    columnstring = ""
    bigdatastring = ""
    firstpass = True
    for title in columns:
        if firstpass:
            columnstring = title[0]
            firstpass = False
        else:
            columnstring = columnstring + ", " + title[0]
    insertstring = ""
    firstpass = True
    for data in bigdata:
        for item in data:
            if firstpass:
                bigdatastring = '"' + item + '"'
                firstpass = False
            else:
                bigdatastring = bigdatastring + ', "' + item + '"'
                insertstring = "INSERT INTO VoterInfoTb (" + columnstring + ") VALUES (" + bigdatastring.replace("/",
                                                                                                                 "-") + ");"
            # print(insertstring)
        try:
            mycursor.execute(insertstring)
            mydb.commit()
        except:
            print(insertstring)
        finally:
            bigdatastring = ""
            insertstring = ""
            firstpass = True


def create_database(input_cursor):
    with open("Voter_DB-Create_String.txt") as string_file:
        create_string = string_file.read()
    input_cursor.execute(create_string)


mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="3640Outrage!",
        database="voterdb"
    )
mycursor = mydb.cursor()
create_database(mycursor)
#populate_voter_db_from_file('20191008_VoterDetail/ALA_20191008.txt', mycursor)
