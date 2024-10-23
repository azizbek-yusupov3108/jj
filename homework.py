class user:
    def init(self,ism,username,email):
        self.ism = ism
        self.username = username
        self.email = email

    def websayt(self):
        print(f"ismim{self.ism} {self.username} {self.email}")


user1 = user("shaydo" , "bekturdieva_shaydo","bekturdiyevashaydo9@gmail.com")

user2= user('zilola','mov1','zilola9@gmail.com')
user3 = user ('azizbek','azizbek_08','azizbek8@gmail.com')
user1.websayt()
user3.websayt()
user2.websayt()


# print(user1.ism)
# print(user3.username)
# print(user2.email)


# def get_username(self):
#     return self.username
# print(user1.get_fullname())