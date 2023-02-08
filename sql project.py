import mysql.connector

def create_database_and_table():
    try:
        connection = mysql.connector.connect(user='root', password='123456', host='localhost')
        cursor = connection.cursor()
        query = "CREATE DATABASE IF NOT EXISTS student_db"
        cursor.execute(query)
        print("Database created successfully.")
        connection.close()
        connection = mysql.connector.connect(user='root', password='123456', host='localhost', database='student_db')
        cursor = connection.cursor()

        query = "CREATE TABLE IF NOT EXISTS students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), roll_no INT, student_class VARCHAR(255), phone_number VARCHAR(255))"
        cursor.execute(query)
        print("Table created successfully.")
    except mysql.connector.Error as error:
        print("Error: {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == '__main__':
    create_database_and_table()

def add_student(name, roll_no, subject, phone_number):
    try:
        connection = mysql.connector.connect(user='root', password='123456', host='localhost', database='student_db')
        cursor = connection.cursor()
        query = "INSERT INTO students(name, roll_no, student_class, phone_number) VALUES(%s, %s, %s, %s)"

        values = (name, roll_no, subject, phone_number)
        cursor.execute(query, values)
        connection.commit()
        print("Student added successfully.")
    except mysql.connector.Error as error:
        print("Error: {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def view_all_students():
    try:
        connection = mysql.connector.connect(user='root', password='123456', host='localhost', database='student_db')
        cursor = connection.cursor()
        query = "SELECT * FROM students"
        cursor.execute(query)
        rows = cursor.fetchall()
        print("Student Details:")
        for row in rows:
            print("Name: {}, Roll No: {}, Subject: {}, Phone Number: {}".format(row[1], row[2], row[3], row[4]))
    except mysql.connector.Error as error:
        print("Error: {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def delete_student(id):
    try:
        connection = mysql.connector.connect(user='root', password='123456', host='localhost', database='student_db')
        cursor = connection.cursor()

        query = "SELECT * FROM students WHERE id=%s"
        values = (id,)
        cursor.execute(query, values)
        result = cursor.fetchall()
        if cursor.rowcount == 0:
            raise ValueError("Error: ID not found.")

        query = "DELETE FROM students WHERE id=%s"
        cursor.execute(query, values)
        connection.commit()
        print("Student deleted successfully.")
    except mysql.connector.Error as error:
        print(f"Error connecting to the database: {error}")
    except ValueError as error:
        print(str(error))
    finally:
        cursor.close()
        connection.close()


if __name__ == '__main__':
    choice = input("Enter 1 to add student, 2 to view all students, 3 to delete student record: ")
    if choice == '1':
        name = input("Enter name: ")
        roll_no = input("Enter roll number: ")
        subject = input("Enter class: ")
        phone_number = input("Enter phone number: ")
        add_student(name, roll_no, subject, phone_number)
    elif choice == '2':
        view_all_students()
    elif choice =='3' :
        id=int(input("enter id to delete: "))
        delete_student(id)
    else:
        print("Invalid choice.")
   
