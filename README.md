# Software-Quality-Assignment

For the assignment I divided the parts into separate files for readability and better understanding.

The system contains four files:

•	Users.py
•	Clients.py
•	Main.py
•	Database.db

Users.py

In this file classes are defined for the creation, validation and encryption of the users. The first class ‘User’ is for the creating the user objects.The second class ‘Encryption’ handles the encryption and decryption of the user objects information. The encryption technique used is Caesar Cipher. The third class ‘ValidateUsers’ inherits from the ‘User’ and ‘Encryption’ class to apply the validation and encryption of the attributes/input. It contains two functions that validate the username and password through the use of Regular Expressions

I added some dummy data at the end of the file to run. When you run Users.py you can see the results from the techniques used. You can modify the information to see different results.

Clients.py

In the clients file the creation and validation of the clients is defined. The first class ‘Clients’ handles the creation of the client’s objects. The second class ‘ValidateClients’ inherits from the class ‘Clients’ to apply the validation of the attributes/input. For every attribute a validation function is defined to handle the specific requirements with Regular Expressions.

Here I also created a dummy client object to run Clients.py and see the process. You can modify the information to see different results.

Main.py

This is the file where it all comes together. Importing the classes from Clients.py and Users.py to get the functionality. To store the information, I use SQLite. I already created functions to initiate the database and add users and clients. I still need to implement the functions to create the users and clients with validation and authorization. At last I need to put the pieces together to make it function as a whole. 
