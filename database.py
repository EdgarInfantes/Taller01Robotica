import sqlite3

def create_database():
    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()

    # Crear tabla de estudiantes
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        class TEXT NOT NULL
    )
    ''')

    # Crear tabla de asistencia
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY,
        student_id INTEGER,
        date TEXT NOT NULL,
        status TEXT NOT NULL,
        comment TEXT,
        FOREIGN KEY (student_id) REFERENCES students (id)
    )
    ''')

    # Crear tabla de usuarios
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL
    )
    ''')

    conn.commit()
    conn.close()

def add_student(name, class_name):
    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, class) VALUES (?, ?)", (name, class_name))
    conn.commit()
    conn.close()

def get_students_by_class(class_name):
    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE class = ?", (class_name,))
    students = cursor.fetchall()
    conn.close()
    return students

def record_attendance(student_id, date, status, comment=""):
    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO attendance (student_id, date, status, comment) VALUES (?, ?, ?, ?)",
                   (student_id, date, status, comment))
    conn.commit()
    conn.close()

# Agregar más funciones según sea necesario para manejar la base de datos