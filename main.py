from  dane import users_list

tp_list = []

def add_user_to(users_list:list) -> None:
    name = input('Pod1aj imię: ')
    nick = input('Podaj ksyweczke: ')
    post = int(input('Ile wstawił postuf: '))
    users_list.append({"name": name, "nick": nick, "posts": post})

def remove_user_from(users_list:list) -> None:
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

    # print(numer)
    # print(tp_list[numer-1])


remove_user_from(users_list)


# l_fraj = int(input('Ilu chcesz dodać frajeruf: '))

# for x in range(l_fraj):
#     add_user_to(users_list)


# for x in range(l_fraj):
#     name = input('Pod1aj imię: ')
#     nick = input('Podaj ksyweczke: ')
#     post = int(input('Ile wstawił postuf: '))
#     users_list.append({"name": name, "nick": nick, "posts": post})

for user in users_list:
    # print(user['nick'], 'dodal tyle ', user['posts'], 'postuf')
    print(f'dodal {user["name"]} tyle {user["posts"]} postuf')

