

class UserCreateCommand:
    def __init__(self, user_repository: DjangoUserRepository):
        self.user_repository = user_repository

    def execute(
        self,
        email: str,
        password: Password,

    ):
