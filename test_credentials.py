#import test framework unittest
#import credential class

import unittest
from credentials import Credentials

#create subclass

class TestCredentials(unittest.TestCase):

    def setUp(self):
        '''
        Define a set of instructions to be executed before each task
        '''
        self.new_credentials=Credentials('instagram','mwanikiiii')
        