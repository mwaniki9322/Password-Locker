#!/usr/bin/env python3.9
from credentials import Credentials

def create_credentials(platform,email,password):
    '''
    Function to create a new credential
    '''
    new_credentials= Credentials(platform,email,password)
    return new_credentials

def save_credentials(credentials):
    '''
    Function to save credentials
    '''
    Credentials.save_credentials()