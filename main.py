users:list[dict] = [
    {'name': 'Krystian', 'location': 'Żyrardów', 'posts': 500, },
    {'name': 'Laura', 'location': 'Łuków', 'posts': 555, },
    {'name': 'Karol', 'location': 'Miedzyrzec Podlaski', 'posts': 666, }
]

for user in users:
    print(f'Twój znajomy:{user["name"]} z {user["location"]} opublikował {user["posts"]}')
