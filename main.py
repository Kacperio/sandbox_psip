from  dane import users_list

def add_user_to(users_list:list) -> None:
    name = input('Pod1aj imię: ')
    nick = input('Podaj ksyweczke: ')
    post = int(input('Ile wstawił postuf: '))
    users_list.append({"name": name, "nick": nick, "posts": post})

add_user_to(users_list)

# l_fraj = int(input('Ilu chcesz dodać frajeruf: '))

# for x in range(l_fraj):
#     name = input('Pod1aj imię: ')
#     nick = input('Podaj ksyweczke: ')
#     post = int(input('Ile wstawił postuf: '))
#     users_list.append({"name": name, "nick": nick, "posts": post})

for user in users_list:
    # print(user['nick'], 'dodal tyle ', user['posts'], 'postuf')
    print(f'dodal {user["nick"]} tyle {user["posts"]} postuf')

