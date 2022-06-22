def main():
    password = get_user_password()
    valid = valid_password(password_user=password)

    if valid == True:
        print("Пароль правильный!")
    else:
        print("Пароль неправильный!")


def valid_password(password_user):
    correct_length = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    is_valid = False

    if len(password_user) >= 7:
        correct_length = True
        for letter in password_user:
            if letter.isupper():
                has_uppercase = True
            if letter.islower():
                has_lowercase = True
            if letter.isdigit():
                has_digit = True

    if correct_length and has_digit and has_lowercase and has_uppercase:
        is_valid = True
    else:
        is_valid = False

    return is_valid

def get_user_password():
    password = input("Введите пароль: ")
    return password

main()
