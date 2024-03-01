from flask import Flask, request, redirect, render_template_string, url_for
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)


def create_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='admin',
        database='mydatabase'
    )


def create_students_table():
    try:
        conn = create_db_connection()
        cursor = conn.cursor()
        create_table_query = """
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            age INT NOT NULL,
            grade VARCHAR(50) NOT NULL
        );
        """
        cursor.execute(create_table_query)
        conn.commit()
        print("Table 'students' created successfully.")
    except Error as e:
        print(f"Error: '{e}' occurred")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

create_students_table()
@app.route('/')
def index():
    # Fetch all students to display
    conn = create_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template_string(open('index.html').read(), students=students)


@app.route('/add_student', methods=['POST'])
def add_student():
    data = request.form
    conn = create_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)",
                   (data['name'], data['age'], data['grade']))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))


@app.route('/edit_student/<int:student_id>', methods=['GET', 'POST'])
def edit_student(student_id):
    conn = create_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        data = request.form
        cursor.execute("UPDATE students SET name=%s, age=%s, grade=%s WHERE id=%s",
                       (data['name'], data['age'], data['grade'], student_id))
        conn.commit()
    else:
        cursor.execute("SELECT * FROM students WHERE id = %s", (student_id,))
        student = cursor.fetchone()

    cursor.close()
    conn.close()

    if request.method == 'POST':
        return redirect(url_for('index'))
    else:
        # Assuming you have a separate HTML form for editing
        return render_template_string(open('edit_student.html').read(), student=student)


@app.route('/delete_student/<int:student_id>', methods=['POST'])
def delete_student(student_id):
    conn = create_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
