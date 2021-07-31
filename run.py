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

def del_credentials(credentials):
    '''
    function to delete credentials
    '''
    Credentials.delete_credentials()

def find_credentials(platform):
    '''
    Function that finds a credentials by number and returns the credentials
    '''
    return Credentials.find_by_platform(platform)

def check_existing_credentials(platform):
    '''
    Function that check if a credentials exists with that platform and return a Boolean
    '''
    return Credentials.credentials_exists(platform)