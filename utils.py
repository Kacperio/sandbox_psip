# from  dane import users_list

def add_user_to(users_list:list) -> None:
    name = input('Pod1aj imię: ')
    nick = input('Podaj ksyweczke: ')
    post = int(input('Ile wstawił postuf: '))
    users_list.append({"name": name, "nick": nick, "posts": post})

def remove_user_from(users_list:list) -> None:
    tp_list =[]
    name = input('kogo chcesz wykopac :')
    for user in users_list:
        if user['name']== name:
            tp_list.append(user)
    print('znaleziono takich uzytkownikuw:')
    print('0 usuwa wszystkich')
    for numerek, user_to_be_removed in enumerate(tp_list):
        print(numerek+1, user_to_be_removed)
    numer = int(input('wybierz kościa do wyautowania: '))
    if numer == 0:
        for user in tp_list:
            users_list.remove(user)
    else:
        users_list.remove(tp_list[numer-1])

def show_users_from(users_list:list) -> None:
    for user in users_list:
        # print(user['nick'], 'dodal tyle ', user['posts'], 'postuf')
        print(f'dodal {user["name"]} tyle {user["posts"]} postuf')

def GUI(users_list):
    while True:
        print('\nWitajze ksieciuniuniu\n'
            f'0: mam dosc wychodze\n'
            f'1: wyswietl uytkownikow\n'
            f'2: dodaj ich\n'
            f'3: usun frajerof\n'
            f'4. modyfikuj wacpanuw\n')
        wyb = int(input('podaj docelowa funkcja '))
        print('wybrano', wyb)

        match wyb:
            case 0:
                print('sajonara')
                break
            case 1:
                print('wyswietlam liste')
                show_users_from(users_list)
            case 2:
                print('dodawanie')
                add_user_to(users_list)
            case 3:
                print('usuwanie')
                remove_user_from(users_list)
            case 4:
                print('modyfikacjion')
                update_user(users_list)

def update_user(users_list: list[dict, dict]) -> None:
    nick_of_user = input('Podaj nick użytkownika do modyfikacji ')
    print(f'Wpisano {nick_of_user}')
    for user in users_list:
        if user['nick'] == nick_of_user:
            print('znaleziono')
            new_name = input('Podaj nowe imię użytkownika ')
            user['name'] = new_name
            new_nick = input('Podaj nowy nick użytkownika ')
            user['nick'] = new_nick
            new_posts = input('Podaj nową ilość postów ')
            user['posts'] = new_posts
# l_fraj = int(input('Ilu chcesz dodać frajeruf: '))

# for x in range(l_fraj):
#     add_user_to(users_list)


# for x in range(l_fraj):
#     name = input('Pod1aj imię: ')
#     nick = input('Podaj ksyweczke: ')
#     post = int(input('Ile wstawił postuf: '))
#     users_list.append({"name": name, "nick": nick, "posts": post})
