#!/usr/bin/python3
<<<<<<< HEAD
"""test for city"""
import unittest
import os
from models import city
from models.city import City
from models.base_model import BaseModel, Base
import pep8
import sqlalchemy


class TestCity(unittest.TestCase):
    """this will test the city class"""

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.city = City()
        cls.city.name = "LA"
        cls.city.state_id = "CA"

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.city

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_City(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_City(self):
        """checking for docstrings"""
        self.assertIsNot(city.__doc__, None)
        self.assertIsNotNone(City.__doc__)

    def test_class_method_presence_City(self):
=======
"""
Unittest for the City class
Test files by using the following command line:
python3 -m unittest tests/test_models/test_city.py
"""
import unittest
import pep8
from os import path, remove
import datetime
import models
from models import city
from models.city import City
from models.engine.file_storage import FileStorage


class TestCity(unittest.TestCase):
    """define variables and methods"""

    def setUp(self):
        """
        Sets the public class attributes of the City class back to ""
        Method called to prepare the test fixture. This is called immediately
        before calling the test method; other than AssertionError or SkipTest
        """
        City.state_id = ""
        City.name = ""
        FileStorage._FileStorage__objects = {}
        FileStorage._FileStorage__file_path = "file.json"

    def tearDown(self):
        """
        Sets the public class attributes of the City class back to ""
        Method called immediately after the test method has been called and
        the result recorded
        """
        del City.state_id
        del City.name
        del FileStorage._FileStorage__file_path
        del FileStorage._FileStorage__objects
        if path.exists("file.json"):
            remove("file.json")

    def test_pep8_conformance(self):
        """Test that City conforms to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_class_method_presence(self):
>>>>>>> c5c69c3b281ca80047e1f7969e0cd1ee2d9e23eb
        """Test that the City methods are all present"""
        l1 = dir(City)
        self.assertIn('__init__', l1)
        self.assertIn('save', l1)
        self.assertIn('to_dict', l1)
        self.assertIn('__str__', l1)

<<<<<<< HEAD
    def test_class_attributes_City(self):
        """checking if City have attributes"""
=======
    def test_class_attribute_presence(self):
        """Test that the City attributes are all present"""
>>>>>>> c5c69c3b281ca80047e1f7969e0cd1ee2d9e23eb
        l1 = dir(City)
        self.assertIn('state_id', l1)
        self.assertIn('name', l1)

<<<<<<< HEAD
    def test_instance_attributes_City(self):
=======
    def test_instance_method_presence(self):
        """Test that the City instance has the same methods"""
        l1 = dir(City())
        self.assertIn('__init__', l1)
        self.assertIn('save', l1)
        self.assertIn('to_dict', l1)
        self.assertIn('__str__', l1)

    def test_instance_attribute_presence(self):
>>>>>>> c5c69c3b281ca80047e1f7969e0cd1ee2d9e23eb
        """Test that the City instance attributes are all present"""
        l1 = dir(City())
        self.assertIn('id', l1)
        self.assertIn('updated_at', l1)
        self.assertIn('created_at', l1)
        self.assertIn('__class__', l1)
        self.assertIn('state_id', l1)
        self.assertIn('name', l1)

<<<<<<< HEAD
    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != "db", "not a database")
    def test_class_attributes_City_db(self):
        """chekcing if City have DBStorage-related attributes"""
        l1 = dir(City)
        self.assertIn('__tablename__', l1)
        self.assertIn('places', l1)

    def test_is_subclass_City(self):
        """test if City is subclass of Basemodel"""
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)
        self.assertTrue(issubclass(self.city.__class__, Base), True)

    def test_attribute_types_City(self):
        """test attribute type for City"""
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != "db", "not a database")
    def test_attribute_types_City_db(self):
        """test attribute type for City"""
        self.assertEqual(type(self.city.__tablename__), str)
        self.assertEqual(type(self.city.places), sqlalchemy.orm.collections.
                         InstrumentedList)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "skip test")
    def test_save_City(self):
        """test if the save works"""
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict_City(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.city), True)


if __name__ == "__main__":
    unittest.main()
=======
    def test_docstring_presence(self):
        """Test that Module, Class, and methods all have a docstring"""
        self.assertIsNot(city.__doc__, None)
        self.assertIsNot(City.__doc__, None)
        self.assertIsNot(City.__init__.__doc__, None)
        self.assertIsNot(City.save.__doc__, None)
        self.assertIsNot(City.to_dict.__doc__, None)
        self.assertIsNot(City.__str__.__doc__, None)

    def test_instantiation(self):
        """Test proper instantiation of object 'City()'"""

        ci = City()
        self.assertIsInstance(ci, City)
        self.assertIsInstance(ci.id, str)
        self.assertIsInstance(ci.created_at, datetime.datetime)
        self.assertIsInstance(ci.updated_at, datetime.datetime)
        self.assertIsInstance(ci.__class__, type)

        ci.size = "tall"
        l1 = dir(ci)
        self.assertIn('size', l1)
        self.assertEqual(ci.__dict__['size'], 'tall')

        ci.size = 'tall'
        l2 = dir(ci)
        self.assertIn('size', l2)
        self.assertEqual(ci.__dict__['size'], 'tall')

        ci.age = 28
        l3 = dir(ci)
        self.assertIn('age', l3)
        self.assertEqual(ci.__dict__['age'], 28)

        ci.age = 28.5
        l4 = dir(ci)
        self.assertIn('age', l4)
        self.assertEqual(ci.__dict__['age'], 28.5)

        ci.age = None
        l5 = dir(ci)
        self.assertIn('age', l5)
        self.assertEqual(ci.__dict__['age'], None)

        ci_kw1 = City(**{})
        self.assertIsInstance(ci_kw1, City)
        self.assertIsInstance(ci_kw1.id, str)
        self.assertIsInstance(ci_kw1.created_at, datetime.datetime)
        self.assertIsInstance(ci_kw1.updated_at, datetime.datetime)
        self.assertIsInstance(ci_kw1.__class__, type)

        ci_kw2 = City(**{"first_name": "John", "age": 25})
        l6 = dir(ci_kw2)
        self.assertIn('first_name', l6)
        self.assertIn('age', l6)
        self.assertEqual(ci_kw2.__dict__['first_name'], 'John')
        self.assertEqual(ci_kw2.__dict__['age'], 25)

    def test_save(self):
        """Test save method"""

        ci = City()
        temp = ci.__dict__['updated_at']
        self.assertFalse(path.isfile('file.json'))
        ci.save()
        self.assertTrue(path.isfile('file.json'))
        self.assertNotEqual(ci.__dict__['updated_at'], temp)
        temp = ci.__dict__['updated_at']
        models.storage.reload()
        self.assertEqual(ci.__dict__['updated_at'], temp)

    def test_to_dict(self):
        """Test to_dict method"""

        ci = City()
        ci.age = 28
        ci.size = "tall"
        for k, v in ci.__dict__.items():
            if k != 'updated_at' and k != 'created_at':
                self.assertIn(k, ci.to_dict())
                self.assertEqual(v, ci.to_dict()[k])
        self.assertEqual(ci.to_dict()['__class__'], ci.__class__.__name__)
        self.assertEqual(ci.to_dict()['updated_at'], ci.updated_at.isoformat())
        self.assertEqual(ci.to_dict()['created_at'], ci.created_at.isoformat())
        self.assertEqual(ci.to_dict()['age'], 28)
        self.assertEqual(ci.to_dict()['size'], 'tall')
        self.assertIsInstance(ci.to_dict(), dict)

    def test_str(self):
        """Test __str__ method"""

        ci = City()
        string = '['+ci.__class__.__name__+']'+' ('+ci.id+') '+str(ci.__dict__)
        self.assertEqual(string, ci.__str__())
>>>>>>> c5c69c3b281ca80047e1f7969e0cd1ee2d9e23eb
