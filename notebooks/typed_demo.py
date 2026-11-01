from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    email: str | None = None

def find_user(users: list[User], name: str) -> User | None:
    for u in users:
        if u.name == name:
            return u
    return None

def email_domain(user: User) -> str | None:
    if user.email is None:
        return None
    return user.email.split('@')[1]

def averae_age(users: list[User]) -> float:
    return sum(u.age for u in users) / len(users)


users = [User('Anna', 39, 'anna@mail.ru'), User('Bob', 25)]
anna = find_user(users, 'Anna')
bob = find_user(users, 'Bob')
print(anna.name)
print(averae_age(users) + ' лет')
