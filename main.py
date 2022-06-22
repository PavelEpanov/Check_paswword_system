def main():
    password_of_user = get_password_user()
    check_user_password(password_user=password_of_user)


def check_user_password(password_user):

    track_problem = 0
    list_problem = []
    real_password = ""

    size_password = len(password_user)
    if size_password < 7:
        track_problem += 1
        list_problem.append("Пароль МЕНЬШЕ 7 символов")

    if password_user.islower():
        track_problem += 1
        list_problem.append("Пароль не содержит ПРОПИСНУЮ букву")

    if password_user.isupper():
        track_problem += 1
        list_problem.append("Пароль не содержит СТРОЧНУЮ букву")

    if password_user.isalpha():
        track_problem += 1
        list_problem.append("Пароль не содержит ЦИФРУ")

    while track_problem > 0:
        print("Ваш пароль не подходит")
        print("Ошибки: ")
        for error in list_problem:
            print(error)
        print("Введите пароль снова!")
        get_password_user()
        password_user = password_user
        check_user_password(password_user=password_user)

    if track_problem == 0:
        real_password = password_user

    print(f"{real_password} - Успешно добавлен")


def get_password_user():
    password_user = input("Введите ваш пароль: ")

    return password_user

main()
