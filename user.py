import random


class User:

    User_list=[]

    def __init__(self,username,password):
        self.username=username
        self.password=password


    def save_user(self):
        '''
        function to save users
        '''    
        User.User_list.append(self)

    def delete_user(self):
        '''
        Delete user 
        '''
        User.User_list.remove(self)

    @classmethod
    def find_by_username(cls,username):
        '''
        Method that takes in a username and returns a user that matches that username.
        '''

        for user in cls.User_list:
            if user.username == username:
                return user
    
    @classmethod
    def user_exist(cls,username):
        '''
        Method that checks if a user exists from the userlist.
        '''

        for user in cls.User_list:
            if user.username == username:
                    return True

        return False

    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.User_list 

    def generate_password():
        char='abcdefghijklmnopqrstuvwxyz1234567890@#$%^&*()'

        while True:
            password_len=int(input('What length would you like your password to be?'))

            password_count=int(input('How many passwords would you like :'))

            for x in range(0,password_count):
                password=''

            for x in range(0,password_len):
                password_char=random.choice(char)
                password=password+password_char

                print('here is your password :',password)  

    generate_password()