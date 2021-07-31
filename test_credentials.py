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
        self.new_credentials=Credentials('instagram','mwanikiiii')

    def test_init(self):
        '''
        check if test object has be instatiated
        '''
        self.assertEqual(self.new_credentials.platform,'instagram')
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
        test_credentials=Credentials('test','credentials')
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

#delete credentials

    def test_delete_credentials(self):
        '''
        delete method to delete credentials
        '''
        self.new_credentials.save_credentials()
        test_credentials=Credentials('test','credentials')
        test_credentials.save_credentials()

        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
    
        

if __name__=='__main__':
    unittest.main()

        