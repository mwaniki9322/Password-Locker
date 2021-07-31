#import test framework unittest
#import credential class

import unittest
from unittest.main import main
from credentials import Credentials

#create subclass

class TestCredentials(unittest.TestCase):

    def tearDown(self):
        '''
        does a clean up after each task
        '''
        Credentials.credentials_list= []

    def setUp(self):
        '''
        Define a set of instructions to be executed before each task
        '''
        self.new_credentials=Credentials('instagram','res@gmail.com','mwanikiiii')

    def test_init(self):
        '''
        check if test object has be instatiated
        '''
        self.assertEqual(self.new_credentials.platform,'instagram')
        self.assertEqual(self.new_credentials.email,'res@gmail.com')
        self.assertEqual(self.new_credentials.password,'mwanikiiii')       

#save credentials test

    def test_save_credentials(self):
        '''
        test to save contact
        '''
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

#save multiple credentials

    def test_save_multiple_credentials(self):
        '''
        test to check if multiple contacts can be saved
        '''
        self.new_credentials.save_credentials()
        test_credentials=Credentials('testgram','test@gmail.com','pass')
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

#delete credentials

    def test_delete_credentials(self):
        '''
        delete method to delete credentials
        '''
        self.new_credentials.save_credentials()
        test_credentials=Credentials('testgram','test@gmail.com','pass')
        test_credentials.save_credentials()

        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

#find credential credential by platform

    def test_find_credential_by_platform(self):
        '''
        search for contact by platform
        '''
        self.new_credentials.save_credentials()
        test_credentials=Credentials('testgram','test@gmail','pass')
        test_credentials.save_credentials()
        
        found_credentials=Credentials.find_by_platform('testgram')
        self.assertEqual(found_credentials.email,test_credentials.email)

#test to check if object exists
    
    def test_credentials_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credentials.
        '''

        self.new_credentials.save_credentials()
        test_credentials=Credentials('testgram','test@gmail','pass') # new contact
        test_credentials.save_credentials()

        credential_exists = Credentials.credentials_exists("instagram")

        self.assertTrue(credential_exists)

#display the credentials 

    def test_display_credentials(self):
        '''
        display the credentials
        '''
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)





if __name__=='__main__':
    unittest.main()

        