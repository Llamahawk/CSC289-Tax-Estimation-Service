user = {}
class Hashuser:
    def __init__(self, first_name, last_name, username, password, email):
        self.firstname = first_name
        self.lastname = last_name
        self.username = username
        self.password = password
        self.email=email

    def hashpassword(self):
        password=hash(self.password)
        return password

    def save_in_user(self):
        user["first_name"]=self.firstname
        user["last_name"] = self.firstname
        user["username"] = self.firstname
        user["password"] = Hashuser.hashpassword(self)
        user["email"] = self.firstname





hashuser = Hashuser("userfirstname", "userlastname", "userusername", "userpassword", "user1@gmail.com")
hashuser.save_in_user()
print(user)

class Hash_and_check:
    def __init__(self, user_password):
        self.user_password = input("Enter the password ")

    def hash_user_password(self):
        user_password = hash(self.user_password)
        print(user_password)
        if user["password"] == user_password:
            print("access granted!")

        else:
            print("username and password do not mach!")

userp = Hash_and_check("userpassword")
userp.hash_user_password()