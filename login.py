from datetime import datetime
import re
import sys
import openpyxl


class login_methods:
    """
    This will contain methods to run login program.
    It will have 2 methods:
    (1) run_dict(username, email) will store a dictonary of objects taken from the input of the user where the keys
        are the username and email as the values
    (2) run_notepad(username, email) will store username and email to a separate .txt file
    (3) run_excel(username, email) will store username and email to an excel file
    """

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def getUsername(username):
        if len(username.strip()) < 20 and len(username.strip()) >= 6:
            return True
        else:
            return False

   # @property
    def getEmail(email):
        if re.search('@[a-z]+', email.strip().lower()):
            return True
        else:
            return False

    def run_dict(dict_storage, username, email):
        """
        :param username, email
        :return updated dictonary
        """

        if (username.strip().lower() not in dict_storage.keys()) and (email.strip().lower() not in dict_storage.values()):
            dict_storage[username] = email.strip().lower()
            print("Your username & email has been successfully added on: {}".format(datetime.now().strftime('%c')))
            return dict_storage
        elif (username.strip().lower() in dict_storage.keys()):
            print("Sorry, your username is taken.")
            return dict_storage
        else:
            print("Sorry, your email is already registered")
            return dict_storage

    def run_notepad(file, username, email):
        """

        :param username:
        :param email:
        :return:
        """
        uname_bool = False
        email_bool = False
        f = open(file, 'r')
        for line in f:
                if username in line:
                    uname_bool = True
                if email in line:
                    email_bool = True
        f.close()
                #uname_bool = re.search(username.strip().lower(), contents)
                #email_bool = re.search(email.strip().lower(), contents)
        with open(file, 'a') as f:
            if (uname_bool is False and email_bool is False):
                f.write(" USERNAME={} , EMAIL_ADD={}\n".format(username.strip().lower(), email.strip().lower()))
                print("Your username and password has been added on {}".format(datetime.now().strftime('%c')))
                f.close()
                return file
            elif uname_bool is True:
                print("Sorry, this username is already taken.")
                f.close()
                return file
            else:
                print("Sorry, this email has already been registered.")
                f.close()
                return file

    def run_excel(excel_file, username, email):
        wb = openpyxl.load_workbook(excel_file)
        working_sheet = wb.get_sheet_by_name('Sheet2')
        for r in rows



class main():
    """
    This is a main login program.
    The user will be asked for a password and the program will store it in three (3) ways
    """
    dict1 = {}
    flag = True
    while (flag):
        print(
            "Hi, welcome to the login program!\nTo start, please pick and input the ff:\nPlease make sure that length of username is between 6 and 20 characters")
        uname = input("Username:")
        email = input("Email: ")

        uname_bool = login_methods.getUsername(uname)
        email_bool = login_methods.getEmail(email)

        INVENTORY_FILE = 'Inventory File Rev2.txt'
        EXCEL_INVENTORY = 'exceltest.xlsx'


# THIS WLL CHECK VALIDITY OF USERNAME AND EMAIL ADDRESS
        if (uname_bool is True and email_bool is True):
            #dict1 = login_methods.run_dict(dict1, uname, email)
            #INVENTORY_FILE = login_methods.run_notepad(INVENTORY_FILE, uname, email)
        elif (uname_bool is False and email_bool is False):
            print("Invalid username and email.")
        elif (uname_bool is False):
            print("Invalid username. Please make sure your username's length is within 6 to 20 characters.")
        elif (email_bool is False):
            print("Invalid email.")
        else:
            print("Ooops. There's something wrong here.")

#THIS WILL ASK USER TO CONTINUE LOOP
        answer = input('Would you like to do another login? [Y/N] ')
        if answer.upper() != 'Y':
            flag = False

    sys.exit(1)


if __name__ == "__main__":
    main()
