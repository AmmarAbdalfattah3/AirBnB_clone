#!/usr/bin/python3
"""Test file for City class"""


from models.city import City
from tests.test_models.test_base_model import TestBaseModel


class TestCity(TestBaseModel):
    """Class to test the 'city' file"""

    def setUp(self):
        """Set up a two instance before each a test case,
           In addition to instance variable containing the model name.
        """
        self._model = City()
        self._model2 = City()
        self._name_class = "City"
