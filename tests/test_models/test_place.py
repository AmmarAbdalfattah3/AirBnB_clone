#!/usr/bin/python3
"""Test file for Place class"""


from models.place import Place
from tests.test_models.test_base_model import TestBaseModel


class TestPlace(TestBaseModel):
    """Class to test the 'place' file"""

    def setUp(self):
        """Set up a two instance before each a test case,
           In addition to instance variable containing the model name.
        """
        self._model = Place()
        self._model2 = Place()
        self._name_model = "Place"
