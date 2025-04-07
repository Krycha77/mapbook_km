def get_user_info(users_data:list[dict])->None:
    for user in users_data:
        print(f'Twój znajomy: {user["name"]} z {user["location"]} opublikował {user["posts"]}')

def add_user(user_data: list[dict]) -> None:
    tmp_name:str = input('podaj imię: ')
    tmp_location: str = input('podaj miejsce: ')
    tmp_posts: int = int(input('podaj liczbę postów: '))
    user_data.append({'name': tmp_name, 'location': tmp_location, 'posts': tmp_posts})