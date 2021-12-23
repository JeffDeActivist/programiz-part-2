"""Still working on it...will be updated"""
print("Welcome.please create an account with us.")


class Errors(Exception):
    pass


class InvalidMatch(Errors):
    pass


class WrongLoginDetails(Errors):
    pass


class PasswordsDontMatch(Errors):
    pass


class UnRecommendedPassword(Errors):
    pass


class CodeVerificationError(Errors):
    pass


def create_login(username=input("Enter a username you shall be using\n"),
                 password=input("Enter a strong password\n"),
                 password1=input("Re-enter your password for confirmation\n"),
                 email=input("Enter your active email address\n")

                 ):
    if password != password1:
        raise PasswordsDontMatch("Make sure passwords match")
    elif password == password1 and password1 == '123456':
        raise UnRecommendedPassword("Enter a strong password")
    elif len(password1) < 6:
        raise UnRecommendedPassword("Password too short")
    if len(email) > 20:
        raise OverflowError("Email not valid.Make sure it has less than 20 characters")
    else:
        print('Wait for a verification that will automatically be generated and sent to you')

    import random
    import datetime
    today = datetime.datetime.now()
    time_today = today.date().strftime('%c')
    code_sent = random.randint(1000, 9999)
    print(code_sent)
    enter_code = int(input("Enter the code sent to your email"))
    if code_sent == enter_code:
        print("Code verified")
        print("Account created on", time_today, '.')
    else:
        raise CodeVerificationError("Code entered does not match code sent")

    def login(Username=input("Enter your username"),
              Password=input("Enter your password")
              ):
        if Password != password1:
            raise PasswordsDontMatch("Password does not match the password you created ")
        elif Username != username:
            raise InvalidMatch("Username does not match thr username you provided while creating your account")
        else:
            print("You have logged in successfully")

    login()


create_login()
print("Below are the products to select from:")
products = {'sugar': 100,
            'salt': 40,
            'soap': 70,
            'maize': 110,
            'tea leaves': 30,
            'chocolate': 150,
            'cooking oil': 100,
            'rice': 75,
            'chili': 45,
            'milk': 430
            }
for key, value in products.items():
    print(key, "::", value)
items = 1
item_selected = []
item_needed = 'continue'
no_selected = []
while items <= 10:
    print("enter product:", items)
    item_needed = input("Enter the product name here:\n").title()
    no_needed = int(input("Enter the number of items you need for the product above:\n"))
    item_selected.append(item_needed)
    if item_needed == 'Done':
        break
    items += 1

item_selected.remove('Done')
print("You have selected the following", item_selected)

