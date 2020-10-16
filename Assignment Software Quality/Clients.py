import re

class Clients:

    def __init__(self, fname, lname, email, street, hnumber, zipcode, city, mobile):
        self.name = fname + ' ' + lname
        self.email = email
        self.street = street
        self.hnumber = hnumber
        self.zipcode = zipcode
        self.city = city
        self.mobile = mobile

    def clientInfo(self):
        return '{}, {}, {}, {}, {}, {}, {}'.format(self.name, self.street, self.hnumber, self.zipcode, self.email, self.city, self.mobile)


class ValidateClients(Clients):

    cities = ['Rotterdam', 
            'Amsterdam', 
            'Utrecht', 
            'Den Haag', 
            'Leiden', 
            'Groningen', 
            'Tilburg', 
            'Zeeland',
            'Luxemburg',
            'Limburg']

    def __init__(self, fname, lname, email, street, hnumber, zipcode, city, mobile):
        super().__init__(fname, lname, email, street, hnumber, zipcode, city, mobile)
        self.name = self.isNameValid(fname + ' ' + lname)
        self.email = self.isEmailValid(email)
        self.street = self.isStreetValid(street)
        self.hnumber = self.isNumberValid(hnumber)
        self.zipcode = self.isZipCodeValid(zipcode)
        self.city = self.isCityValid(self.cities[city])
        self.mobile = self.isPhoneValid(mobile)

    def isNameValid(self, input):
        regEx = r"^[a-zA-Z ]{1,30}$"
        if re.match(regEx, input) != None:
            print('Correct name')
        else:
            print('Invalid name. Please try again\n')
        return input

    def isStreetValid(self, input):
        regEx = r"^[a-zA-Z ]{1,30}$"
        if re.match(regEx, input) != None:
            print('Correct Street')
        else:
            print('Invalid street. Please try again\n')
        return input
            
    def isNumberValid(self, input):
        regEx = r"^[1-9]{1}[0-9]{0,3}[a-zA-z]{0,1}$"
        if re.match(regEx, input) != None:
            print('Correct housenumber')
        else:
            print('Invalid housenumber. Please try again\n')
        return input
            
    def isZipCodeValid(self, input):
        regEx = r"^[1-9][0-9]{3}[a-zA-Z]{2}$"
        if re.match(regEx, input) != None:
            print('Correct zipcode')
        else:
            print('Invalid zipcode. Please try again\n')
        return input
            
    def isCityValid(self, input):
        regEx = r"^[a-zA-Z]{1,30}$"
        if re.match(regEx, input) != None:
            print('Correct city')
        else:
            print('Invalid city. Please try again\n')
        return input
            
    def isEmailValid(self, input):
        regEx = r"^[\w.-\_]+@[\w.\-]+\.[A-Za-z]{2,3}$"
        if re.match(regEx, input) != None:
            print('Correct email')
        else:
            print('Invalid email. Please try again\n')
        return input
             
    def isPhoneValid(self, input):
        regEx = r"^\+31\-6\-[0-9]{8}$"
        if re.match(regEx, input) != None:
            print('Correct phonenumber')
        else:
            print('Invalid phonenumber. Please try again\n')
        return input
                        

a = ValidateClients('Sebastian', 'Poot', '0880028@hr.nl', 'Wijnhaven', '107B', '3045TA', 0, '+31-6-12345678')
print('\n' + '-' * 30 + '\n')
print(a.clientInfo())
