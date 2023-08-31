import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="dbstore"
)

mycursor = mydb.cursor()

def insert_sale():

    ORno = input("Enter the ORno: ")
    Amount = input("Enter the Amount: ")
    sql = "INSERT INTO tblsales (ORno, Amount) VALUES (%s, %s)"
    val = (ORno, Amount)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

def delete_sale():

    ORno = input("Enter the ORno: ")
    sql = "DELETE FROM tblsales WHERE ORno = '"+ORno+"'"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")

def update_sale():
    ORno = input("Enter the ORno: ")
    Amount = input("Enter the Amount(new): ")
    sql = "UPDATE tblsales SET Amount = '"+Amount+"' WHERE ORno = '"+ORno+"'"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")

def search_sale():

    ORno = input("Enter the ORno: ")
    sql = "SELECT * FROM tblsales WHERE ORno='"+ORno+"'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def main():
    while True:
        print("Sales Management System")
        print("1. Search Sales")
        print("2. Add Sales")
        print("3. Update Sales")
        print("4. Delete Sales")
        print("5. Exit")
        choice = input("Enter your choice [1/2/3/4/5]: ")

        if choice == '1':
            search_sale()
        if choice == '2':
            insert_sale()
        if choice == '3':
            update_sale()
        if choice == '4':
            delete_sale()
        if choice == '5':
            exit()
            print("Thank you for using Sales Management System")


if __name__=="__main__":
    main()

