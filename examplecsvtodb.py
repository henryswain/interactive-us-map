import csv, pymysql
#This will connect you to database you need
#Make shure to add your correct information
#Check it worked before moving on
db=pymysql.connect(
  host = 'webdev.divms.uiowa.edu',
  user = 'henryswain',
  passwd = 'AgRZXxndJYXOIStHrDqk',
  db='cs3910_henryswain')
#print ("connected")
#Create table (if doen't exist already)

cur = db.cursor()
cur.execute("DROP TABLE IF EXISTS us_states;")
db.commit()
#In this example has column Name and column gpa
create_SQL="""CREATE TABLE IF NOT EXISTS us_states (State VARCHAR(20), Population int, Median_age FLOAT(3, 1), Capital VARCHAR(20));"""
#Below print can be used to check what command it tries to execute in next line
#print (create_SQL)
cur = db.cursor()
cur.execute(create_SQL)
db.commit()
cur.close()
#If you you got here table is created - check in dbdev
#This will open file filename,csv
#It uses csvlibrary
with open('US_States.csv', newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    print(reader.fieldnames)  # This will show you the exact column names
    for row in reader:
        cur=db.cursor()
        # Next line creates sql string that represents
        # one insert sql command and current row data
        # Note row['Need to be one of the column names'] will grab
        # value in current row for that column
        # %s is replaced with first parameter in parentheses - string
        # %f is replaced with second parameter - float
        # sql = "INSERT INTO courses VALUES (%s, %s, %s, %s);" % (row['Code'], row['Name'], row['Skills'], row['Tools'])
        sql = "INSERT INTO us_states VALUES ('%s', '%s', '%s', '%s');" % (
          row['State'],  # Escape single quotes in the data
          row['Population'],
          row['Median age'],
          row['Capital']
        )
        # Below print can print sql command - check it legit before executing:)
        print(sql)
        cur.execute(sql)
        db.commit()
        cur.close()
db.close()