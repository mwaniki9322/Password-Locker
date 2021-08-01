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