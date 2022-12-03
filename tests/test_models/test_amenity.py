#!/usr/bin/python3
"""Test file for Amenity class"""


from models.amenity import Amenity
from tests.test_models.test_base_model import TestBaseModel


class TestAmenity(TestBaseModel):
    """Class to test the 'amenity' file"""

    def setUp(self):
        """Set up a two instance before each a test case,
           In addition to instance variable containing the model name.
        """
        self._model = Amenity()
        self._model2 = Amenity()
        self._name_class = "Amenity"
