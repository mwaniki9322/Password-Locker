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
        