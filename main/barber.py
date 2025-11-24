class Student:
    def __init__(self, name, phone, age, email, student_id):
        self.name = name
        self.phone = phone
        self.age = age
        self.email = email
        self.student_id = student_id


class Group:
    def __init__(self, title, profession):
        self.title = title
        self.profession = profession
        self.students = []

    def add_student(self):  
        name = input("Name: ")
        try:
            student_id = int(input("Student ID: "))
        except ValueError:
            print("student must be number")
            return
        phone = input("Phone: ")
        age = input("Age: ")
        email = input("Email: ")
        student = Student(name, phone, age, email, student_id)
        self.students.append(student)
        print("Student added successfully!")

    def get_one_student(self):
        try:
            student_id = int(input("Student ID: "))
        except ValueError:
            print("Student Id must be number")
            return
        for st in self.students:
            if st.student_id == student_id:
                print(f"Name: {st.name}, Phone: {st.phone}, Age: {st.age}, Email: {st.email}")
                return
        print("Student not found")

    def view_students(self):
        if not self.students:
            print("No students in this group")
            return

        print(f"Students of group {self.title}:")
        for i, st in enumerate(self.students, start=1):
            print(f"{i}. Name: {st.name}, Phone: {st.phone}, Age: {st.age}, Email: {st.email}")


class OTM:
    def __init__(self, title):
        self.title = title
        self.groups = []

    def add_group(self):
        title = input("Group title: ")
        profession = input("Profession: ")
        group = Group(title, profession)
        self.groups.append(group)
        print("Group added successfully!")

    def view_groups(self):
        if not self.groups:
            print("No groups available")
            return

        print(f"Groups in {self.title}:")
        for i, item in enumerate(self.groups, start=1):
            print(f"{i}. Title: {item.title}, Profession: {item.profession}")


class Erp:
    def __init__(self):
        self.title = "ERP"
        self.otms = []

    def add_otm(self):
        title = input("OTM title: ")
        otm = OTM(title)
        self.otms.append(otm)
        print("OTM added successfully!")

    def view_otms(self):
        if not self.otms:
            print("No OTM available")
            return

        for i, item in enumerate(self.otms, start=1):
            print(f"{i}. Title: {item.title}")


def group_manager(group: Group):
    while True:
        kod = input("\n1. Add Student\n2. View Students\n3. One Student\n4. Back\nChoose: ")

        if kod == "1":
            group.add_student()

        elif kod == "2":
            group.view_students()

        elif kod == "3":
            group.get_one_student()

        elif kod == "4":
            break

        else:
            print("Select a valid option!")


def otm_manager(otm: OTM):
    while True:
        code = input("\n1. Add Group\n2. View Groups\n3. Group Detail\n4. Back\nChoose: ")

        if code == "1":
            otm.add_group()

        elif code == "2":
            otm.view_groups()

        elif code == "3":
            otm.view_groups()
            if not otm.groups:
                continue

            mini = int(input("Group ID: "))
            if 1 <= mini <= len(otm.groups):
                group_manager(otm.groups[mini - 1])
            else:
                print("Invalid group ID")

        elif code == "4":
            break

        else:
            print("Select a valid option!")


def erp_manager(erp: Erp):
    while True:
        code = input("\n1. Add OTM\n2. View OTMs\n3. OTM Detail\n4. Exit\nChoose: ")

        if code == "1":
            erp.add_otm()

        elif code == "2":
            erp.view_otms()

        elif code == "3":
            erp.view_otms()
            if not erp.otms:
                continue

            index = int(input("OTM ID: "))
            if 1 <= index <= len(erp.otms):
                otm_manager(erp.otms[index - 1])
            else:
                print("Invalid OTM ID")

        elif code == "4":
            print("Exiting ERP...")
            break

        else:
            print("Select a valid option!")

erp = Erp()
erp_manager(erp)