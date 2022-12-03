#!/usr/bin/python3
"""Test file for State class"""


from models.state import State
from tests.test_models.test_base_model import TestBaseModel


class TestState(TestBaseModel):
    """Class to test the 'state' file"""

    def setUp(self):
        """Set up a two instance before each a test case,
           In addition to instance variable containing the model name.
        """
        self._model = State()
        self._model2 = State()
        self._name_class = "State"
