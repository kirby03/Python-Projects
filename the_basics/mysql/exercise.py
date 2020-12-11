import mysql.connector

con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

cursor = con.cursor()

word = input("Enter a word to find definition(s): ")

query = cursor.execute('SELECT * FROM Dictionary WHERE Expression LIKE "%s" ' % word)

result = cursor.fetchall()

if result:
    for r in result:
        print(r[1])
else:
    print("Word not found.")
