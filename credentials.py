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

#delete credentials

    def delete_credentials(self):
        '''
        delete a saved credentials
        '''
    
        Credentials.credentials_list.remove(self)

#class method informs interpreter that the method belongs to the entire class
    @classmethod
    def find_by_platform(cls,platform):
         '''
        Method that takes in a platform and returns a contact that matches that platform.

        Args:
            platform: platform to search for
        Returns :
            Credentials of person that matches the number.
        '''
         for credential in cls.credentials_list:
          if credential.platform==platform:
              return credential


    @classmethod
    def credentials_exists(cls,platform):
        '''
        Method that checks if a contact exists from the contact list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the credential exists
        '''
        for credential in cls.credentials_list:
            if credential.platform == platform:
                    return True

        return False    
    

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credential list
        '''
        return cls.credentials_list