Here is a Python program that generates a task with the following specifications:
# User Management System
class User:
    def __init__(self, id, name, email, phone, createdDate):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.createdDate = createdDate

    def get_user(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "createdDate": self.createdDate
        }