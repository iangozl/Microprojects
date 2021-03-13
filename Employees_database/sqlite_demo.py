import sqlite3
from employee import Employee

# conn = sqlite3.connect('Employees_database/employee.db') # Python creates the file automatically

# CONNECTION USING MEMORY
conn = sqlite3.connect(':memory:') # It starts fresh everytime it runs

c = conn.cursor() # Now we can run SQL commands with the execute() method

c.execute("""CREATE TABLE employees (
            first text,
            last text,
            pay integer
            )""") # <- Using docstrings to use multiple lines for the query

def insert_emp(emp):
    with conn: # WITH allows us not to write a commit function
        c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp.first, emp.last, emp.pay))

def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last = :last", {'last': lastname}) # Using a Dictionary 
    return c.fetchall()

def update_pay(emp,pay):
    with conn:
        c.execute(""" UPDATE employees SET pay = :pay WHERE first = :first AND last = :last""",
                {'pay' : pay , 'first' : emp.first, 'last' : emp.last})

def remove_emp(emp):
    with conn:
        c.execute("DELETE FROM employees WHERE first = :first AND last = :last", {'first': emp.first, 'last': emp.last})


emp_1 = Employee('Ricardo', 'Ramirez', 10000)
emp_2 = Employee('Juan','Ramirez', 20000)

# c.execute("INSERT INTO employees VALUES ('Daniel', 'Lopez', 10000)")

# conn.commit() # <= Just to be explicit 


# This way of doing queries is vulnerable to SQL Injections
# c.execute("INSERT INTO employee VALUES ('{}', '{}', '{}')".format(emp_1.first, emp_1.last, emp_1.pay)) <- Values can be changed

# INSERT info into the DATABASE by using tuples
# c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay))
# conn.commit()

# # PROPER WAY to put the placeholder
# c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", 
#             {'first': emp_2.first, 'last':emp_2.last, 'pay':emp_2.pay})
# conn.commit() 

# c.execute("SELECT * FROM employees WHERE last = ?", ('Lopez', )) # Using a tuple

# Iterate THROUGH the result

# print(c.fetchall()) # All the results

# c.execute("SELECT * FROM employees WHERE last = :last", ('Ramirez', )) # Using a Dictionary 
# print(c.fetchall())

# conn.commit() # Commits the current transaction

insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emps_by_name('Ramirez')
print(emps)

update_pay(emp_2, 30000)
remove_emp(emp_1)

emps = get_emps_by_name('Ramirez')
print(emps)

conn.close()