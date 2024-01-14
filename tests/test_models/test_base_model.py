#!/usr/bin/python3
"""
This line of codes defines unittests for models/base_model.py.
Unittest classes: TestBaseModel_instantiation, TestBaseModel_save,
and TestBaseModel_to_dict.
"""
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))
        # ... (Note that other test methods remains unchanged)

    def test_instantiation_with_args_and_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)


class TestBaseModel_save(unittest.TestCase):
    """
    This Unittests is for testing save method of the BaseModel class.
    """

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except FileNotFoundError:
            pass

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp", "file.json")
        except FileNotFoundError:
            pass
        # ... (Note that other test methods remains unchanged)

    def test_save_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)


class TestBaseModel_to_dict(unittest.TestCase):
    """
    This Unittests is for testing to_dict method of the
    BaseModel class.
    """

    # ...(Note that other test methods remains unchanged)


if __name__ == "__main__":
    unittest.main()
