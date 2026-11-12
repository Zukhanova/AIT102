students = { "111-34-3434": "John", "132-56-6290": "peter"}
tuple(students.keys())
("111-34-3434", "132-56-6290")
tuple(students.values())
("John", "peter")
tuple(students.items())
(("111-34-3434", "John"), ("132-56-6290", "peter"))
students.get("111-34-3434")
"John"
print(students.get("999-34-3434"))
None
students.pop("111-34-3434")
"John"
students
{"132-56-6290": "peter"}
students.clear()
students
{}
