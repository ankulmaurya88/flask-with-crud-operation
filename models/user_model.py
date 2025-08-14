class UserModel:
    users = {}
    next_id = 1

    @classmethod
    def create(cls, name, email):
        user = {'id': cls.next_id, 'name': name, 'email': email}
        cls.users[cls.next_id] = user
        cls.next_id += 1
        return user

    @classmethod
    def get_all(cls):
        return list(cls.users.values())

    @classmethod
    def get(cls, user_id):
        return cls.users.get(user_id)

    @classmethod
    def update(cls, user_id, name=None, email=None):
        user = cls.users.get(user_id)
        if not user:
            return None
        if name:
            user['name'] = name
        if email:
            user['email'] = email
        cls.users[user_id] = user
        return user

    @classmethod
    def delete(cls, user_id):
        return cls.users.pop(user_id, None)
