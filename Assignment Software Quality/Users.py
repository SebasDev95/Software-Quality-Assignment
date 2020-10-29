import re

class User:

    def __init__(self, username, password, status):
        self.username = username
        self.password = password
        self.status = status

    def credentials(self):
        return "Username: {} \nPassword: {} \nStatus: {}" .format(self.username, self.password, self.status)



class Encryption:

    '''Because Caesar Cipher only does letters, the special characters and numbers are not handled'''
    specialChar = re.compile("^[~!@#_$%^&*=`|\\()}{\\]\\+\\[:;'<>,.?/.-]*$")

    def encrypt(self, info):
        '''Function to encode the information using caesar cipher'''
        result = ""

        for i in range(len(info)):
            char = info[i]

            if char.isdigit():
                result += char
            elif Encryption.specialChar.search(char) != None:
                result += char
            elif (char.isupper()):
                result += chr((ord(char) + 4 - 65) % 26 + 65)
            else:
                result += chr((ord(char) + 4 - 97) % 26 + 97)
        
        return result


    def decrypt(self, info):
        '''Function to decode the information from the caesar cipher method'''
        result = ""

        for i in range(len(info)):
            char = info[i]

            if char.isdigit():
                result += char
            elif Encryption.specialChar.search(char) != None:
                result += char   
            elif (char.isupper()):
                result += chr((ord(char) - 4 - 65) % 26 + 65)
            else:
                result += chr((ord(char) - 4 - 97) % 26 + 97)
        
        return result



class ValidateUsers(User, Encryption):

    hierarchy = ['System Administrator', 'Advisor']

    def __init__(self, username, password, status):
        super().__init__(username, password, status)
        self.username = self.isUsernameValid(username)
        self.password = self.isPasswordValid(password)
        self.status = self.hierarchy[status]
    
    def isUsernameValid(self, input):
        '''Check if the username is valid with RegEx'''
        regExUsername = r"^(?=.{5,20}$)(^[A-Za-z])([a-zA-Z0-9-_'.]*$)"

        if re.match(regExUsername, input) != None:
            print('\nYour username is: {}'.format(input))
        else:
            print('\nInvalid username. Please try again\n')
        return input


    def isPasswordValid(self, input):
        '''Check if the password is valid with RegEx'''
        regExPassword = r"^(?=.{8,30}$)(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\W)[^-\s].*$"

        if re.match(regExPassword, input) != None:
            print('\nYour password is: {}'.format(input))
        else:
            print('\nInvalid password. Please try again\n')
        return input


user = ValidateUsers('Pootato@!@#@', 'P00t-@to!-12', 0)
print('\n' + '-' * 30 + '\n')
print(user.encrypt(user.username) + '\n' + user.encrypt(user.password))
print('\n' + '-' * 30 + '\n')
print(user.decrypt(user.encrypt(user.username)) + '\n' + user.decrypt(user.encrypt(user.password)))
print('\n' + '-' * 30 + '\n')
print(user.credentials())