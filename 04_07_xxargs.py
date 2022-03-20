def save_user(**user):
    print(type(user))
    print(user)
    print(user['id'])

save_user(id=1, name="John", age=22)