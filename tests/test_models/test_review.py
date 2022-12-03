#!/usr/bin/python3
"""Test file for Review class"""


from models.review import Review
from tests.test_models.test_base_model import TestBaseModel


class TestReview(TestBaseModel):
    """Class to test the 'review' file"""

    def setUp(self):
        """Set up a two instance before each a test case,
           In addition to instance variable containing the model name.
        """
        self._model = Review()
        self._model2 = Review()
        self._name_class = "Review"
