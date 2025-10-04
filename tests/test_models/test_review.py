#!/usr/bin/python3
<<<<<<< HEAD
"""test for review"""
import unittest
import os
from models.review import Review
from models.base_model import BaseModel
import pep8


class TestReview(unittest.TestCase):
    """this will test the place class"""

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.rev = Review()
        cls.rev.place_id = "4321-dcba"
        cls.rev.user_id = "123-bca"
        cls.rev.text = "The srongest in the Galaxy"

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.rev

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_Review(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/review.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_Review(self):
        """checking for docstrings"""
        self.assertIsNotNone(Review.__doc__)

    def test_attributes_review(self):
        """chekcing if review have attributes"""
        self.assertTrue('id' in self.rev.__dict__)
        self.assertTrue('created_at' in self.rev.__dict__)
        self.assertTrue('updated_at' in self.rev.__dict__)
        self.assertTrue('place_id' in self.rev.__dict__)
        self.assertTrue('text' in self.rev.__dict__)
        self.assertTrue('user_id' in self.rev.__dict__)

    def test_is_subclass_Review(self):
        """test if review is subclass of BaseModel"""
        self.assertTrue(issubclass(self.rev.__class__, BaseModel), True)

    def test_attribute_types_Review(self):
        """test attribute type for Review"""
        self.assertEqual(type(self.rev.text), str)
        self.assertEqual(type(self.rev.place_id), str)
        self.assertEqual(type(self.rev.user_id), str)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "skip test")
    def test_save_Review(self):
        """test if the save works"""
        self.rev.save()
        self.assertNotEqual(self.rev.created_at, self.rev.updated_at)

    def test_to_dict_Review(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.rev), True)


if __name__ == "__main__":
    unittest.main()
=======
"""
Unittest for the Review class
Test files by using the following command line:
python3 -m unittest tests/test_models/test_review.py
"""
import unittest
import pep8
from os import path, remove
import datetime
import models
from models import review
from models.review import Review
from models.engine.file_storage import FileStorage


class TestReview(unittest.TestCase):
    """define variables and methods"""

    def setUp(self):
        """
        Sets the public class attributes of the Review class back to ""
        Method called to prepare the test fixture. This is called immediately
        before calling the test method; other than AssertionError or SkipTest
        """
        Review.place_id = ""
        Review.user_id = ""
        Review.text = ""
        FileStorage._FileStorage__objects = {}
        FileStorage._FileStorage__file_path = "file.json"

    def tearDown(self):
        """
        Sets the public class attributes of the Review class back to ""
        Method called immediately after the test method has been called and
        the result recorded
        """
        del Review.place_id
        del Review.user_id
        del Review.text
        del FileStorage._FileStorage__file_path
        del FileStorage._FileStorage__objects
        if path.exists("file.json"):
            remove("file.json")

    def test_pep8_conformance(self):
        """Test that Review conforms to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_class_method_presence(self):
        """Test that the Review methods are all present"""
        l1 = dir(Review)
        self.assertIn('__init__', l1)
        self.assertIn('save', l1)
        self.assertIn('to_dict', l1)
        self.assertIn('__str__', l1)

    def test_class_attribute_presence(self):
        """Test that the Review attributes are all present"""
        l1 = dir(Review)
        self.assertIn('place_id', l1)
        self.assertIn('user_id', l1)
        self.assertIn('text', l1)

    def test_instance_method_presence(self):
        """Test that the Review instance has the same methods"""
        l1 = dir(Review())
        self.assertIn('__init__', l1)
        self.assertIn('save', l1)
        self.assertIn('to_dict', l1)
        self.assertIn('__str__', l1)

    def test_instance_attribute_presence(self):
        """Test that the Review instance attributes are all present"""
        l1 = dir(Review())
        self.assertIn('id', l1)
        self.assertIn('updated_at', l1)
        self.assertIn('created_at', l1)
        self.assertIn('__class__', l1)
        self.assertIn('place_id', l1)
        self.assertIn('user_id', l1)
        self.assertIn('text', l1)

    def test_docstring_presence(self):
        """Test that Module, Class, and methods all have a docstring"""
        self.assertIsNot(review.__doc__, None)
        self.assertIsNot(Review.__doc__, None)
        self.assertIsNot(Review.__init__.__doc__, None)
        self.assertIsNot(Review.save.__doc__, None)
        self.assertIsNot(Review.to_dict.__doc__, None)
        self.assertIsNot(Review.__str__.__doc__, None)

    def test_instantiation(self):
        """Test proper instantiation of object 'Review()'"""

        re = Review()
        self.assertIsInstance(re, Review)
        self.assertIsInstance(re.id, str)
        self.assertIsInstance(re.created_at, datetime.datetime)
        self.assertIsInstance(re.updated_at, datetime.datetime)
        self.assertIsInstance(re.__class__, type)

        re.size = "tall"
        l1 = dir(re)
        self.assertIn('size', l1)
        self.assertEqual(re.__dict__['size'], 'tall')

        re.size = 'tall'
        l2 = dir(re)
        self.assertIn('size', l2)
        self.assertEqual(re.__dict__['size'], 'tall')

        re.age = 28
        l3 = dir(re)
        self.assertIn('age', l3)
        self.assertEqual(re.__dict__['age'], 28)

        re.age = 28.5
        l4 = dir(re)
        self.assertIn('age', l4)
        self.assertEqual(re.__dict__['age'], 28.5)

        re.age = None
        l5 = dir(re)
        self.assertIn('age', l5)
        self.assertEqual(re.__dict__['age'], None)

        re_kw1 = Review(**{})
        self.assertIsInstance(re_kw1, Review)
        self.assertIsInstance(re_kw1.id, str)
        self.assertIsInstance(re_kw1.created_at, datetime.datetime)
        self.assertIsInstance(re_kw1.updated_at, datetime.datetime)
        self.assertIsInstance(re_kw1.__class__, type)

        re_kw2 = Review(**{"first_name": "John", "age": 25})
        l6 = dir(re_kw2)
        self.assertIn('first_name', l6)
        self.assertIn('age', l6)
        self.assertEqual(re_kw2.__dict__['first_name'], 'John')
        self.assertEqual(re_kw2.__dict__['age'], 25)

    def test_save(self):
        """Test save method"""

        re = Review()
        temp = re.__dict__['updated_at']
        self.assertFalse(path.isfile('file.json'))
        re.save()
        self.assertTrue(path.isfile('file.json'))
        self.assertNotEqual(re.__dict__['updated_at'], temp)
        temp = re.__dict__['updated_at']
        models.storage.reload()
        self.assertEqual(re.__dict__['updated_at'], temp)

    def test_to_dict(self):
        """Test to_dict method"""

        re = Review()
        re.age = 28
        re.size = "tall"
        for k, v in re.__dict__.items():
            if k != 'updated_at' and k != 'created_at':
                self.assertIn(k, re.to_dict())
                self.assertEqual(v, re.to_dict()[k])
        self.assertEqual(re.to_dict()['__class__'], re.__class__.__name__)
        self.assertEqual(re.to_dict()['updated_at'], re.updated_at.isoformat())
        self.assertEqual(re.to_dict()['created_at'], re.created_at.isoformat())
        self.assertEqual(re.to_dict()['age'], 28)
        self.assertEqual(re.to_dict()['size'], 'tall')
        self.assertIsInstance(re.to_dict(), dict)

    def test_str(self):
        """Test __str__ method"""

        re = Review()
        string = '['+re.__class__.__name__+']'+' ('+re.id+') '+str(re.__dict__)
        self.assertEqual(string, re.__str__())
>>>>>>> c5c69c3b281ca80047e1f7969e0cd1ee2d9e23eb
