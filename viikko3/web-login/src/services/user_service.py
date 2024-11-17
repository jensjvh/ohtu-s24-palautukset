from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)
import re


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user
    
    def is_lowercase_alpha(self, string: str) -> bool:
        return bool(re.fullmatch(r'[a-z]+', string))

    def validate(self, username, password, password_confirmation):
        if not username or not password:
            raise UserInputError("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
        if len(username) < 3 or not self.is_lowercase_alpha(username):
            raise UserInputError("Username is invalid")
        
        if len(password) < 8:
            raise UserInputError("Password is too short")
        
        if password.isalpha():
            raise UserInputError("Password should not consist of letters only")
        
        if password != password_confirmation:
            raise UserInputError("Password and confirmation do not match")
    
        user = self._user_repository.find_by_username(username)

        if user:
            raise UserInputError("User already exists")
        


user_service = UserService()
