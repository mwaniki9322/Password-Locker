#import test framework 
#import class user

import unittest
from user import User

#create a subclass

class TestUser(unittest.TestCase):

    def tearDown(self):
        User.User_list=[]

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
        self.new_user.save_user()
        test_user=User('test23','testty')
        test_user.save_user()
        self.assertEqual(len(User.User_list),2)
    
    def test_delete_user(self):
        '''
        delete method to delete user
        '''
        self.new_user.save_user()
        test_user=User('test23','testty')
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.User_list),1)

    
    def test_find_user_by_username(self):
        '''
        search for user by platform
        '''
        self.new_user.save_user()
        test_user=User('test23','testty')
        test_user.save_user()
        
        found_user=User.find_by_username('test23')
        self.assertEqual(found_user.password,test_user.password)
    


    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''

        self.new_user.save_user
        test_user = User('test23','testty') # new user
        test_user.save_user()

        user_exists = User.user_exist("test23")

        self.assertTrue(user_exists)


    def test_display_all_users(self):
        '''
        method that returns a list of all users saved
        '''
   



        self.assertEqual(User.display_users(),User.User_list)
if __name__=='__main__':
        unittest.main()
