# pylint: disable=c

# empty = dict()
# type(empty)
# empty = {}
# type(empty)

students = {}

# Inserting new values later
students[10000] = ['John B', 'CS', 4.0]
students[20000] = ['Alexa', 'CS', 3.9]
print students
print students[10000]

# One method
key = 10
if key in students:
    value = students[key]

# Probably better
x = students.get(10)
print x
