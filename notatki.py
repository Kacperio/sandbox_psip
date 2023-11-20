from  dane import users_list

def update_user(user_list: list[dict, dict]) -> None:
    nick_of_user = input('Podaj nick użytkownika do modyfikacji ')
    print(f'Wpisano {nick_of_user}')
    for user in users_list:
        if user['nick'] == nick_of_user:
            print('znaleziono')
            new_name = input('Podaj nowe imię użytkownika ')
            user['name'] = new_name
            new_nick = input('Podaj nowy nick użytkownika ')
            user['nick'] = new_nick
        
update_user(users_list)
for user in users_list:
    print(user)