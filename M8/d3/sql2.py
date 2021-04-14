import sqlite3
from sqlalchemy import create_engine
import pandas as pd
import os
import pymysql




conn = sqlite3.connect("strive.db")
      

def get_remote_conn(user, pas, IP, port):
    try:
        engine = create_engine("mysql+pymysql://{}:{}@{}/{}?host={}?port={}").format(user,pas,IP,user,IP,port)
        conn = engine.connect()
        return conn
    except Exception as ex:
        print(ex)
        return ex
    
def sql_execute(sentence):
    
    try:
        c = conn.cursor()
        a = c.execute(sentence)
        conn.commit()
        print(a)
    except Exception as ex:
        print(ex)
        return ex

def sql_execute_many(sentence, lists):
    
    try:
        c = conn.cursor()
        a = c.executemany(sentence, lists)
        conn.commit()
        print(a)
    except Exception as ex:
        print(ex)
        return ex
    
def pd_select(sentence):
    
    try:
        df = pd.read_sql_query(sentence, conn)
        return df
    except Exception as ex:
        print(ex)
        return ex

def pd_upload_csv(name : str, pth, head = 0):
    
    try:
        df = pd.read_csv(pth, header = head )
        frame = df.to_sql(name, conn, if_exists = 'replace')
        return frame
    except Exception as ex:
        print(ex)
        return ex

def close():
    conn.close()



# STUDENT TABLE

student_table = """CREATE TABLE IF NOT EXISTS student_table (
    name varchar(20) NOT NULL,
    surname varchar(20) NOT NULL DEFAULT 'a',
    id int NOT NULL PRIMARY KEY,
    country varchar(20),
    city varchar(20),
    FOREIGN KEY (id) REFERENCES project_table (st)
    );"""

students = [('Kimberley','Taylor', 1, 'Spain', 'Barcelona'),
            ('John', 'Smith', '2', 'England', 'London'),
            ('Mary', 'Campbell', '3', 'Scotland', 'Edinburgh'),
            ('Sara', 'Google', '4', 'Italy', 'Milan')]

drop_student = "drop table student_table"

a = sql_execute(student_table)  
a = sql_execute_many('INSERT INTO student_table VALUES (?,?,?,?,?)', students)

df_students = pd_select("select * from student_table")
print(df_students)

# Count how many students there are
df_count = pd_select("SELECT COUNT(*) FROM student_table")
print(df_count)

# Add a new field referencing their favourite teacher
a = sql_execute("ALTER TABLE student_table ADD favourite_teacher varchar(20)")
a = sql_execute("UPDATE student_table SET favourite_teacher = 'Jan' WHERE name = 'Kimberley' AND surname='Taylor'")
updated_students = pd_select("select * from student_table")
print(updated_students)

# Delete all students with name starting 'j' and ending 'n'
#pattern = "\j+(.*?)n+\s+"

a = sql_execute("DELETE FROM student_table WHERE name like 'j%n'")
updated_students = pd_select("select * from student_table")
print(updated_students)

# COunt how many unique student names there are
unique_names = pd_select("SELECT COUNT ( DISTINCT name ) AS 'Number of unique student names' FROM student_table")
print(unique_names)





# PROJECT TABLE

project_table = """CREATE TABLE IF NOT EXISTS project_table (
    nameP varchar(20) NOT NULL,
    topic varchar(20) NOT NULL DEFAULT 'a',
    st int NOT NULL,
    grade float,
    id int NOT NULL PRIMARY KEY,
    tch varchar(20) NOT NULL,
    FOREIGN KEY (st) REFERENCES student_table(id),
    FOREIGN KEY (tch) REFERENCES teacher_table(id)
    );"""

projects = [('Python', 'Pandas', '2', '7.9', '1', '2'),
            ('SQL', 'FullStack', '3', '9.9', '2', '1'),
            ('BoW', 'NLP', '3', '7.9', '3', '1'),
            ('BoW', 'NLP', '4', '8.4', '4', '1')]


drop_project = "drop table project_table"

b = sql_execute(project_table)      
b = sql_execute_many('INSERT INTO project_table VALUES (?,?,?,?,?,?)', projects)

df_projects = pd_select("select * from project_table")
print(df_projects)

# Create a table with all the students that made an NLP project
print(pd_select("SELECT * FROM student_table NATURAL JOIN project_table WHERE topic='NLP'"))







# TEACHER TABLE

teacher_table = """CREATE TABLE IF NOT EXISTS teacher_table (
    name varchar(20) NOT NULL,
    surname varchar(20) NOT NULL DEFAULT 'a',
    id int NOT NULL PRIMARY KEY,
    country varchar(20),
    city varchar(20),
    speciality varchar(20) NOT NULL,
    salary int,
    FOREIGN KEY (id) REFERENCES project_table(st)
    );"""

drop_teacher = "drop table teacher_table"

teachers = [('Jan','Carbonell', '1', 'Canaries', 'Las Iguanas', 'AI', '1000'),
             ('Antonio', 'Marsella', '2', 'Italy', 'Rome', 'Python', '2000'),
            ('Javier', 'Abellan', '3', 'Spain', 'Madrid', 'ML', '1300'),
            ('Jon', 'Perez', '4', 'Greece', 'Athens', 'ML', '1500')]

c = sql_execute(teacher_table)
c = sql_execute_many('INSERT INTO teacher_table VALUES (?,?,?,?,?,?,?)', teachers)       
df_teachers = pd_select("select * from teacher_table")
print(df_teachers)

# Create a table with all the teachers who specialise in ML and have a salary greater than 1200.
print(pd_select("SELECT * FROM teacher_table WHERE speciality='ML' AND salary>1200"))




# Join tables student and projects
join = pd_select("""SELECT * FROM student_table INNER JOIN project_table ON student_table.id = project_table.st""")
print(join)

# Get the name of the student with the highest grade in a project
highest_grade = pd_select("""SELECT MAX(grade) AS MAX_GRADE, student_table.name as student_name FROM project_table
INNER JOIN student_table ON project_table.st = student_table.id""")
print(highest_grade)


# Create a ttable with the name of the students who made a project where the responsible teacher was not specialised in the topic



close()
