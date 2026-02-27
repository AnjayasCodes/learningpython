student = {
    "Name": "Anjayash",
    "age": 20,
    "course": "python"
}

# print(dir(student))
# print(help(student))

if student.get("python"):
    print("The subject exist")
else:
    print("The subject don't exist")
