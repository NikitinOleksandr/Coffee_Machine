class User:
    # create the class attributes
    n_active = 0
    users = []

    # create the __init__ method
    def __init__(self, active, user_name):
        self.active = active
        self.user_name = user_name
        User.users.append(self.user_name)


User.n_active += 1
