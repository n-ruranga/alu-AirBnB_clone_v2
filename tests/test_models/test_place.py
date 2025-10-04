#!/usr/bin/python3
<<<<<<< HEAD
"""test for place"""
import unittest
import os
from models.place import Place
from models.base_model import BaseModel
import pep8


class TestPlace(unittest.TestCase):
    """this will test the place class"""

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.place = Place()
        cls.place.city_id = "1234-abcd"
        cls.place.user_id = "4321-dcba"
        cls.place.name = "Death Star"
        cls.place.description = "UNLIMITED POWER!!!!!"
        cls.place.number_rooms = 1000000
        cls.place.number_bathrooms = 1
        cls.place.max_guest = 607360
        cls.place.price_by_night = 10
        cls.place.latitude = 160.0
        cls.place.longitude = 120.0
        cls.place.amenity_ids = ["1324-lksdjkl"]

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.place

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_Place(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/place.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_Place(self):
        """checking for docstrings"""
        self.assertIsNotNone(Place.__doc__)

    def test_attributes_Place(self):
        """chekcing if amenity have attributes"""
        self.assertTrue('id' in self.place.__dict__)
        self.assertTrue('created_at' in self.place.__dict__)
        self.assertTrue('updated_at' in self.place.__dict__)
        self.assertTrue('city_id' in self.place.__dict__)
        self.assertTrue('user_id' in self.place.__dict__)
        self.assertTrue('name' in self.place.__dict__)
        self.assertTrue('description' in self.place.__dict__)
        self.assertTrue('number_rooms' in self.place.__dict__)
        self.assertTrue('number_bathrooms' in self.place.__dict__)
        self.assertTrue('max_guest' in self.place.__dict__)
        self.assertTrue('price_by_night' in self.place.__dict__)
        self.assertTrue('latitude' in self.place.__dict__)
        self.assertTrue('longitude' in self.place.__dict__)
        self.assertTrue('amenity_ids' in self.place.__dict__)

    def test_is_subclass_Place(self):
        """test if Place is subclass of Basemodel"""
        self.assertTrue(issubclass(self.place.__class__, BaseModel), True)

    def test_attribute_types_Place(self):
        """test attribute type for Place"""
        self.assertEqual(type(self.place.city_id), str)
        self.assertEqual(type(self.place.user_id), str)
        self.assertEqual(type(self.place.name), str)
        self.assertEqual(type(self.place.description), str)
        self.assertEqual(type(self.place.number_rooms), int)
        self.assertEqual(type(self.place.number_bathrooms), int)
        self.assertEqual(type(self.place.max_guest), int)
        self.assertEqual(type(self.place.price_by_night), int)
        self.assertEqual(type(self.place.latitude), float)
        self.assertEqual(type(self.place.longitude), float)
        self.assertEqual(type(self.place.amenity_ids), list)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "skip test")
    def test_save_Place(self):
        """test if the save works"""
        self.place.save()
        self.assertNotEqual(self.place.created_at, self.place.updated_at)

    def test_to_dict_Place(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.place), True)


if __name__ == "__main__":
    unittest.main()
=======
"""
Unittest for the Place class
Test files by using the following command line:
python3 -m unittest tests/test_models/test_place.py
"""
import unittest
import pep8
from os import path, remove
import datetime
import models
from models import place
from models.place import Place
from models.engine.file_storage import FileStorage


class TestPlace(unittest.TestCase):
    """define variables and methods"""

    def setUp(self):
        """
        Sets the public class attributes of the Place class back to ""
        Method called to prepare the test fixture. This is called immediately
        before calling the test method; other than AssertionError or SkipTest
        """
        Place.city_id = ""
        Place.user_id = ""
        Place.name = ""
        Place.description = ""
        Place.number_rooms = 0
        Place.number_bathrooms = 0
        Place.max_guest = 0
        Place.price_by_night = 0
        Place.latitude = 0.0
        Place.longitude = 0.0
        Place.amenity_ids = []
        FileStorage._FileStorage__objects = {}
        FileStorage._FileStorage__file_path = "file.json"

    def tearDown(self):
        """
        Sets the public class attributes of the Place class back to ""
        Method called immediately after the test method has been called and
        the result recorded
        """
        del Place.city_id
        del Place.user_id
        del Place.name
        del Place.description
        del Place.number_rooms
        del Place.number_bathrooms
        del Place.max_guest
        del Place.price_by_night
        del Place.latitude
        del Place.longitude
        del Place.amenity_ids
        del FileStorage._FileStorage__file_path
        del FileStorage._FileStorage__objects
        if path.exists("file.json"):
            remove("file.json")

    def test_pep8_conformance(self):
        """Test that Place conforms to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_class_method_presence(self):
        """Test that the Place methods are all present"""
        l1 = dir(Place)
        self.assertIn('__init__', l1)
        self.assertIn('save', l1)
        self.assertIn('to_dict', l1)
        self.assertIn('__str__', l1)

    def test_class_attribute_presence(self):
        """Test that the Place attributes are all present"""
        l1 = dir(Place)
        self.assertIn('city_id', l1)
        self.assertIn('user_id', l1)
        self.assertIn('name', l1)
        self.assertIn('description', l1)
        self.assertIn('number_rooms', l1)
        self.assertIn('number_bathrooms', l1)
        self.assertIn('max_guest', l1)
        self.assertIn('price_by_night', l1)
        self.assertIn('latitude', l1)
        self.assertIn('longitude', l1)
        self.assertIn('amenity_ids', l1)

    def test_instance_method_presence(self):
        """Test that the Place instance has the same methods"""
        l1 = dir(Place())
        self.assertIn('__init__', l1)
        self.assertIn('save', l1)
        self.assertIn('to_dict', l1)
        self.assertIn('__str__', l1)

    def test_instance_attribute_presence(self):
        """Test that the Place instance attributes are all present"""
        l1 = dir(Place())
        self.assertIn('id', l1)
        self.assertIn('updated_at', l1)
        self.assertIn('created_at', l1)
        self.assertIn('__class__', l1)
        self.assertIn('city_id', l1)
        self.assertIn('user_id', l1)
        self.assertIn('name', l1)
        self.assertIn('description', l1)
        self.assertIn('number_rooms', l1)
        self.assertIn('number_bathrooms', l1)
        self.assertIn('max_guest', l1)
        self.assertIn('price_by_night', l1)
        self.assertIn('latitude', l1)
        self.assertIn('longitude', l1)
        self.assertIn('amenity_ids', l1)

    def test_docstring_presence(self):
        """Test that Module, Class, and methods all have a docstring"""
        self.assertIsNot(place.__doc__, None)
        self.assertIsNot(Place.__doc__, None)
        self.assertIsNot(Place.__init__.__doc__, None)
        self.assertIsNot(Place.save.__doc__, None)
        self.assertIsNot(Place.to_dict.__doc__, None)
        self.assertIsNot(Place.__str__.__doc__, None)

    def test_instantiation(self):
        """Test proper instantiation of object 'Place()'"""

        pl = Place()
        self.assertIsInstance(pl, Place)
        self.assertIsInstance(pl.id, str)
        self.assertIsInstance(pl.created_at, datetime.datetime)
        self.assertIsInstance(pl.updated_at, datetime.datetime)
        self.assertIsInstance(pl.__class__, type)

        pl.size = "tall"
        l1 = dir(pl)
        self.assertIn('size', l1)
        self.assertEqual(pl.__dict__['size'], 'tall')

        pl.size = 'tall'
        l2 = dir(pl)
        self.assertIn('size', l2)
        self.assertEqual(pl.__dict__['size'], 'tall')

        pl.age = 28
        l3 = dir(pl)
        self.assertIn('age', l3)
        self.assertEqual(pl.__dict__['age'], 28)

        pl.age = 28.5
        l4 = dir(pl)
        self.assertIn('age', l4)
        self.assertEqual(pl.__dict__['age'], 28.5)

        pl.age = None
        l5 = dir(pl)
        self.assertIn('age', l5)
        self.assertEqual(pl.__dict__['age'], None)

        pl_kw1 = Place(**{})
        self.assertIsInstance(pl_kw1, Place)
        self.assertIsInstance(pl_kw1.id, str)
        self.assertIsInstance(pl_kw1.created_at, datetime.datetime)
        self.assertIsInstance(pl_kw1.updated_at, datetime.datetime)
        self.assertIsInstance(pl_kw1.__class__, type)

        pl_kw2 = Place(**{"first_name": "John", "age": 25})
        l6 = dir(pl_kw2)
        self.assertIn('first_name', l6)
        self.assertIn('age', l6)
        self.assertEqual(pl_kw2.__dict__['first_name'], 'John')
        self.assertEqual(pl_kw2.__dict__['age'], 25)

    def test_save(self):
        """Test save method"""

        pl = Place()
        temp = pl.__dict__['updated_at']
        self.assertFalse(path.isfile('file.json'))
        pl.save()
        self.assertTrue(path.isfile('file.json'))
        self.assertNotEqual(pl.__dict__['updated_at'], temp)
        temp = pl.__dict__['updated_at']
        models.storage.reload()
        self.assertEqual(pl.__dict__['updated_at'], temp)

    def test_to_dict(self):
        """Test to_dict method"""

        pl = Place()
        pl.age = 28
        pl.size = "tall"
        for k, v in pl.__dict__.items():
            if k != 'updated_at' and k != 'created_at':
                self.assertIn(k, pl.to_dict())
                self.assertEqual(v, pl.to_dict()[k])
        self.assertEqual(pl.to_dict()['__class__'], pl.__class__.__name__)
        self.assertEqual(pl.to_dict()['updated_at'], pl.updated_at.isoformat())
        self.assertEqual(pl.to_dict()['created_at'], pl.created_at.isoformat())
        self.assertEqual(pl.to_dict()['age'], 28)
        self.assertEqual(pl.to_dict()['size'], 'tall')
        self.assertIsInstance(pl.to_dict(), dict)

    def test_str(self):
        """Test __str__ method"""

        pl = Place()
        string = '['+pl.__class__.__name__+']'+' ('+pl.id+') '+str(pl.__dict__)
        self.assertEqual(string, pl.__str__())
>>>>>>> c5c69c3b281ca80047e1f7969e0cd1ee2d9e23eb
