class User:
    def __init__(self):
        self.id_account = None

    def set_id_account(self, id_account):
        self.id_account = id_account

    def get_id_account(self):
        return self.id_account


user = User()
