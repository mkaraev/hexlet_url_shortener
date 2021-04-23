from entities import URL, User

users = {}
short_to_original = {}


def create_user(user: User) -> User:
    users[user.id] = user
    return user


def delete_user(user_id: int) -> User:
    return users.pop(user_id)


def get_user(user_id: int) -> User:
    return users[user_id]


def create_url(url: URL) -> URL:
    short_to_original[url.short_url] = url
    return url


def delete_url(short_url: str) -> URL:
    return short_to_original.pop(short_url)


def get_url(short_url: str) -> URL:
    return short_to_original[short_url]
