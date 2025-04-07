users:list[dict] = [
    {'name': 'Krystian', 'location': 'Żyrardów', 'posts': 500, },
    {'name': 'Laura', 'location': 'Łuków', 'posts': 555, },
    {'name': 'Karol', 'location': 'Miedzyrzec Podlaski', 'posts': 666, }
]


def get_user_info(users_data:list[dict])->None:
    for user in users_data:
        print(f'Twój znajomy:{user["name"]} z {user["location"]} opublikował {user["posts"]}')

get_user_info(users)