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

def display_credentials():
    '''
    Function that returns all the saved contacts
    '''
    return Credentials.display_credentials()


def main():
    print('hello now that you have logged in you can access your credentials.What would you like to do?')
    while True:
        print("Use these short codes : cc - create a new credential, dc - display credentials, fc -find credentials, ex -exit the credential list ")
        
        short_code=input().lower

        if short_code=='cc':
            print('New credential')
            print('-'*10)
            
            print('Platform....')
            platform=input()

            print('email...')
            email=input()

            print('password')
            password=input()

            save_credentials(create_credentials(platform,email,password))
            print('\n')
            print(f'New Credentials {platform} {email} {password}')
            print('\n')
            print(f'new_credentias {platform} {email} {password}')
            print('\n')


        elif short_code == 'dc':
    
                            if display_credentials():
                                    print("Here is a list of all your credentials")
                                    print('\n')

                                    for credential in display_credentials():
                                            print(f"{credential.platform} {credential.email} .....{credential.password}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any credentials saved yet")
                                    print('\n')
