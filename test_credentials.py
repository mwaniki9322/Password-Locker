#import test framework unittest
#import credential class

import unittest
from unittest.main import main
from credentials import Credentials

#create subclass

class TestCredentials(unittest.TestCase):

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


if __name__=='__main__':
    unittest.main()

        