#!/usr/bin/python3
"""Test for FileStorage class"""

from models import storage
from models.base_model import BaseModel
from datetime import datetime
import unittest
import io
from models.base_model import BaseModel
from contextlib import redirect_stdout
from time import sleep


class TestFileStorage(unittest.TestCase):
    """Class to test the 'file_storage' file"""
    def test_Correct(self):
        """Tests correct output"""
        self.assertRaises(TypeError, storage.all, "Test")
