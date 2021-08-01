#import test framework 
#import class user

import unittest
from user import User

#create a subclass

class TestUser(unittest.TestCase):

    def setUp(self):
        '''
        define a set of instructions to be executed before each task
        '''
        self.new_user=User('kim1234','kim564')

    def test_init(self):
        '''
        test if object has been instatited
        '''
        self.assertEqual(self.new_user.username,'kim1234')
        self.assertEqual(self.new_user.password,'kim564')
    

    def test_save_user(self):
        '''
        test to save use
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.User_list),1)   

    def test_save_multiple_users(self):
        '''
        save multiple users
        '''

if __name__=='__main__':
        unittest.main()
