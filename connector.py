import mysql.connector
def insert_data(id,name,email):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="roottoor",
        database="gowda_ece"
    )
    print("Connected to the database successfully")
    mycursor = mydb.cursor()
    sql = "INSERT INTO peoples (id,name,email)VALUES (%s, %s,%s)"
    val = [id, name, email]
    mycursor.execute("select *  from peoples")
    result = mycursor.fetchall()
    for row in result:
        print(row)

    mydb.commit()
    mycursor.close()
    mydb.close()
    print(mycursor.rowcount, "record inserted.")
id = input("enter the id")
name = input("enter the name")
email = input("enter the email")
insert_data(id,name,email) 