#!/usr/bin/python3
"""Test file for User class"""



from models.user import User
from tests.test_models.test_base_model import TestBaseModel


class TestUser(TestBaseModel):
    """Class to test the 'user' file"""

    def setUp(self):
        """Set up a two instance before each a test case,
           In addition to instance variable containing the model name.
        """
        self._model = User()
        self._model2 = User()
        self._name_class = "User"
