import sqlite3
from employee import Employee

conn = sqlite3.connect('Employees_database/employee.db') # Python creates the file automatically

c = conn.cursor() # Now we can run SQL commands with the execute() method

# c.execute("""CREATE TABLE employees (
#             first text,
#             last text,
#             pay integer
#             )""") # <- Using docstrings to use multiple lines for the query

emp_1 = Employee('Ricardo', 'Ramirez', 10000)
emp_2 = Employee('Juan','Perez', 20000)

# c.execute("INSERT INTO employees VALUES ('Daniel', 'Lopez', 10000)")

# conn.commit() # <= Just to be explicit 


# This way of doing queries is vulnerable to SQL Injections
# c.execute("INSERT INTO employee VALUES ('{}', '{}', '{}')".format(emp_1.first, emp_1.last, emp_1.pay)) <- Values can be changed

# INSERT info into the DATABASE by using tuples
c.execute("INSERT INTO employee VALUES (?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay))
conn.commit()

# PROPER WAY to put the placeholder
c.execute("INSERT INTO employee VALUES (:first, :last, :pay)", 
            ('first': emp_1.first, 'last':emp_1.last, 'pay':emp_1.pay))



c.execute("SELECT * FROM employees WHERE last = 'Lopez'")



# Iterate THROUGH the result

print(c.fetchall()) # All the results

conn.commit() # Commits the current transaction

conn.close()


