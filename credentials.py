class Credentials:
    '''
    a class generates a new instance credentials
    '''
    credentials_list=[]
    def __init__(self,platform,password):
        self.platform=platform
        self.password=password

    def save_credentials(self):

        '''
          save_credentials method saves credentials objects into credentials_list
        '''
        
        Credentials.credentials_list.append(self)
