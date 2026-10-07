from pymongo import MongoClient

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["student_db"]
students = db["students"]

# ---------- FUNCTIONS ----------

# Add Student
def add_student():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    city = input("Enter City: ")

    student = {
        "name": name,
        "age": age,
        "course": course,
        "city": city
    }

    students.insert_one(student)
    print("✅ Student Added Successfully!\n")


# View Students
def view_students():
    print("\n📋 All Students:\n")
    for s in students.find():
        print(f"ID: {s['_id']}")
        print(f"Name: {s['name']}")
        print(f"Age: {s['age']}")
        print(f"Course: {s['course']}")
        print(f"City: {s['city']}")
        print("----------------------")


# Search Student
def search_student():
    name = input("Enter Name to Search: ")
    result = students.find_one({"name": name})

    if result:
        print("✅ Student Found:")
        print(result)
    else:
        print("❌ Student Not Found")


# Update Student
def update_student():
    name = input("Enter Name to Update: ")
    new_city = input("Enter New City: ")

    result = students.update_one(
        {"name": name},
        {"$set": {"city": new_city}}
    )

    if result.modified_count > 0:
        print("✅ Student Updated!")
    else:
        print("❌ No Student Found")


# Delete Student
def delete_student():
    name = input("Enter Name to Delete: ")

    result = students.delete_one({"name": name})

    if result.deleted_count > 0:
        print("✅ Student Deleted!")
    else:
        print("❌ No Student Found")


# ---------- MAIN MENU ----------

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("👋 Exiting...")
        break
    else:
        print("❌ Invalid Choice")
