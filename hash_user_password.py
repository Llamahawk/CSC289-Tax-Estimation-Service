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