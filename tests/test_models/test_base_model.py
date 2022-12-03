#!/usr/bin/env bash
"""Test file for BaseModel class"""

import unittest
import io
from contextlib import redirect_stdout
from datetime import datetime
from time import sleep
from ....models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Class to test the 'base_model' file"""
    def setUp(self):
        """Set up a two instance before each a test case,
           In addition to instance variable containing the model name.
        """
        self._model = BaseModel()
        self._model2 = BaseModel()
        self._name_class = "BaseModel"

    # =========*Public instance variable tests*========

    def test_id_variable(self):
        """Test case for id variable"""
        key_model = self._model
        key_model2 = self.model2
        self.assertTrue(hasattr(key_model.id))
        self.assertTrue(type(key_model.id) is str)
        self.assertNotEqual(key_model.id, key_model2.id)

    def test_create_update_type(self):
        """Test the 'created_at' and 'updated_at' type"""
        self.assertTrue(isinstance(self._model.created_at, datetime))
        self.assertTrue(isinstance(self._model.updated_at, datetime))

    def test_createUpdate_initial(self):
        """Test that initial value of created_at and updated_at are equal
           and also are equal one when adding attributes but saving
        """
        self.assertEqual(self._model.created_at.second,
                         self._model.created_at.second)
        before = self._model.created_at.second
        sleep(1)
        self._model.name = "TEST"
        after = self._model.updated_at.second
        self.assertEqual(before, after)

    # =========*save method tests*========

    def test_save_changes_updated_at(self):
        """Test that 'updated_at' is different from 'created_at' after
           calling 'save()' method
        """
        t_model = self._model
        before = t_mode.created_at.second
        sleep(3)
        t_model.save()
        after = t_mode.updated_at.second
        self.assertNotEqual(before, after)
        self.assertGreater(after, before)

    def test_save_args(self):
        """Tests invalid argument to 'save' method"""
        self.assertRaises(TypeError, self._model.save, "model")

    # =========*to_dict method tests*========

    def test_to_dict_correct(self):
        t_model = self._model
        t_dict = t_model.to_dict()
        self.assertTrue(type(t_dict) is dict)
        self.assertTrue("__clase__" in t_dict.keys())
        signal = True
        for key, value in t_model.__dict__.items():
            if key not in t_dic:
                signal = False
        self.assertTrue(signal)

    def test_to_dict_args(self):
        """Tests invalid argument to 'to_dict' method"""
        self.assertRaises(TypeError, self._model.to_dict, "model")

    def test_created_format(self):
        """Test that created_at value returned by
           'to_dict' method is string in isoformat
        """
        t_model = self._model
        expected_value = datetime.isoformat(t_model.created_at)
        t_dict = t_model.to_dict()
        self.assertTrue(expected_value in t_dict.values())

    def test_updated_format(self):
        """Test that updated_at value returned by
           'to_dict' method is string in isoformat
        """
        t_model = self._model
        expected_value = datetime.isoformat(t_model.updated_at)
        t_dict = t_model.to_dict()
        self.assertTrue(expected_value in t_dict.values())

    # =========*str method tests*========

    def test_str_output(self):
        """Test that '__str__' method prints the required output"""
        t_model = self._model
        file = io.StringIO()
        str_output = "[{}] ({}) {}\n".format(self._name_class, t_model.id, t_model.__dict__)
        with redirect_stdout(file):
            print(t_model)
        self.assertEqual(file.getvalue(), str_output)

if __name__ == "__main__":
    unittest.main()
