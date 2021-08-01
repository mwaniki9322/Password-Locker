#!/usr/bin/env python3.9
from credentials import Credentials


def create_credentials(platform,email,password):
    '''
    Function to create a new credential
    '''
    new_credentials = Credentials(platform,email,password)
    return new_credentials



def save_credentials(credentials):
    '''
    Function to save credentials
    '''
    Credentials.save_credentials(credentials)



def del_credentials(credentials):
    '''
    Function to delete a credentials
    '''
    Credentials.delete_credentials()


def find_credentials(platform):
    '''
    Function that finds a contact by number and return credentials
    '''
    return Credentials.find_by_platform(platform)



def check_existing_credentials(platform):
    '''
    Function that check if a credentials exists with that number and return a Boolean
    '''
    return Credentials.credentials_exists(platform)



def display_credentials():
    '''
    Function that returns all the saved contacts
    '''
    return Credentials.display_credentials()







def main():
    print("Hello Welcome to your Credential list.")

    while True:
                    print("Use these short codes : cc - create a new credentials, dc - display credentials, fc -find a credentials, ex -exit the credential list ")

                    short_code = input().lower()

                    if short_code == 'cc':
                            print("New Credentials")
                            print("-"*10)

                            print ("Platform ....")
                            platform = input()

                            print("Email ...")
                            e_address = input()

                            print("Password ...")
                            password = input()



                            save_credentials(create_credentials(platform,e_address,password)) # create and save new credential.
                            print ('\n')
                            print(f"New Credentials {platform} {e_address} {password} created")
                            print ('\n')

                    elif short_code == 'dc':

                            if display_credentials():
                                    print("Here is a list of all your credentials")
                                    print('\n')

                                    for credentials in display_credentials():
                                            print(f"{credentials.platform} {credentials.email} .....{credentials.password}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any credentials saved yet")
                                    print('\n')

                    elif short_code == 'fc':

                            print("Enter the platform you want to search for")

                            search_platform = input()
                            if check_existing_credentials(search_platform):
                                    search_credentials = find_credentials(search_platform)
                                    print(f"{search_credentials.platform}...{search_credentials.email}...{search_credentials.password}")
                                    print('-' * 20)

                                    print(f"Platform.......{search_credentials.platform}")
                                    print(f"Email address.......{search_credentials.email}")
                                    print(f'Password........{search_credentials.password}')
                            else:
                                    print("That credential does not exist")

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':
    
    main()                       