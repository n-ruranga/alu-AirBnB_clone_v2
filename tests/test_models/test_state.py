#!/usr/bin/python3
<<<<<<< HEAD
"""test for state"""
import unittest
import os
from models import state
from models.state import State
from models.base_model import BaseModel, Base
import pep8
import sqlalchemy


class TestState(unittest.TestCase):
    """this will test the State class"""

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.state = State()
        cls.state.name = "CA"

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.state

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_Review(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/state.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_State(self):
        """checking for docstrings"""
        self.assertIsNotNone(state.__doc__)
        self.assertIsNotNone(State.__doc__)

    def test_class_method_presence_State(self):
        """Test that the State instance has the same methods"""
=======
"""
Unittest for the State class
Test files by using the following command line:
python3 -m unittest tests/test_models/test_state.py
"""
import unittest
import pep8
from os import path, remove
import datetime
import models
from models import state
from models.state import State
from models.engine.file_storage import FileStorage


class TestState(unittest.TestCase):
    """define variables and methods"""

    def setUp(self):
        """
        Sets the public class attributes of the State class back to ""
        Method called to prepare the test fixture. This is called immediately
        before calling the test method; other than AssertionError or SkipTest
        """
        State.name = ""
        FileStorage._FileStorage__objects = {}
        FileStorage._FileStorage__file_path = "file.json"

    def tearDown(self):
        """
        Sets the public class attributes of the State class back to ""
        Method called immediately after the test method has been called and
        the result recorded
        """
        del State.name
        del FileStorage._FileStorage__file_path
        del FileStorage._FileStorage__objects
        if path.exists("file.json"):
            remove("file.json")

    def test_pep8_conformance(self):
        """Test that State conforms to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_class_method_presence(self):
        """Test that the State methods are all present"""
>>>>>>> c5c69c3b281ca80047e1f7969e0cd1ee2d9e23eb
        l1 = dir(State)
        self.assertIn('__init__', l1)
        self.assertIn('save', l1)
        self.assertIn('to_dict', l1)
        self.assertIn('__str__', l1)

<<<<<<< HEAD
    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "not a database")
    def test_instance_method_presence_State_additional(self):
        """Test that the State instance has the extra "cities" method"""
        l1 = dir(State())
        self.assertIn('cities', l1)

    def test_class_attribute_presence_State(self):
=======
    def test_class_attribute_presence(self):
>>>>>>> c5c69c3b281ca80047e1f7969e0cd1ee2d9e23eb
        """Test that the State attributes are all present"""
        l1 = dir(State)
        self.assertIn('name', l1)

<<<<<<< HEAD
=======
    def test_instance_method_presence(self):
        """Test that the State instance has the same methods"""
        l1 = dir(State())
        self.assertIn('__init__', l1)
        self.assertIn('save', l1)
        self.assertIn('to_dict', l1)
        self.assertIn('__str__', l1)

>>>>>>> c5c69c3b281ca80047e1f7969e0cd1ee2d9e23eb
    def test_instance_attribute_presence(self):
        """Test that the State instance attributes are all present"""
        l1 = dir(State())
        self.assertIn('id', l1)
        self.assertIn('updated_at', l1)
        self.assertIn('created_at', l1)
        self.assertIn('__class__', l1)
        self.assertIn('name', l1)

<<<<<<< HEAD
    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != "db", "not a database")
    def test_class_attributes_State_db(self):
        """chekcing if State have DBStorage-related attributes"""
        l1 = dir(State)
        self.assertIn('__tablename__', l1)
        self.assertIn('cities', l1)

    def test_is_subclass_State(self):
        """test if State is subclass of BaseModel"""
        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)
        self.assertTrue(issubclass(self.state.__class__, Base), True)

    def test_attribute_types_State(self):
        """test attribute type for State"""
        self.assertEqual(type(self.state.name), str)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != "db", "not a database")
    def test_attribute_types_State_db(self):
        """test attribute type for State"""
        self.assertEqual(type(self.state.__tablename__), str)
        self.assertEqual(type(self.state.cities), sqlalchemy.orm.collections.
                         InstrumentedList)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "skip test")
    def test_save_State(self):
        """test if the save works"""
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def test_to_dict_State(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.state), True)


if __name__ == "__main__":
    unittest.main()
=======
    def test_docstring_presence(self):
        """Test that Module, Class, and methods all have a docstring"""
        self.assertIsNot(state.__doc__, None)
        self.assertIsNot(State.__doc__, None)
        self.assertIsNot(State.__init__.__doc__, None)
        self.assertIsNot(State.save.__doc__, None)
        self.assertIsNot(State.to_dict.__doc__, None)
        self.assertIsNot(State.__str__.__doc__, None)

    def test_instantiation(self):
        """Test proper instantiation of object 'State()'"""

        st = State()
        self.assertIsInstance(st, State)
        self.assertIsInstance(st.id, str)
        self.assertIsInstance(st.created_at, datetime.datetime)
        self.assertIsInstance(st.updated_at, datetime.datetime)
        self.assertIsInstance(st.__class__, type)

        st.size = "tall"
        l1 = dir(st)
        self.assertIn('size', l1)
        self.assertEqual(st.__dict__['size'], 'tall')

        st.size = 'tall'
        l2 = dir(st)
        self.assertIn('size', l2)
        self.assertEqual(st.__dict__['size'], 'tall')

        st.age = 28
        l3 = dir(st)
        self.assertIn('age', l3)
        self.assertEqual(st.__dict__['age'], 28)

        st.age = 28.5
        l4 = dir(st)
        self.assertIn('age', l4)
        self.assertEqual(st.__dict__['age'], 28.5)

        st.age = None
        l5 = dir(st)
        self.assertIn('age', l5)
        self.assertEqual(st.__dict__['age'], None)

        st_kw1 = State(**{})
        self.assertIsInstance(st_kw1, State)
        self.assertIsInstance(st_kw1.id, str)
        self.assertIsInstance(st_kw1.created_at, datetime.datetime)
        self.assertIsInstance(st_kw1.updated_at, datetime.datetime)
        self.assertIsInstance(st_kw1.__class__, type)

        st_kw2 = State(**{"first_name": "John", "age": 25})
        l6 = dir(st_kw2)
        self.assertIn('first_name', l6)
        self.assertIn('age', l6)
        self.assertEqual(st_kw2.__dict__['first_name'], 'John')
        self.assertEqual(st_kw2.__dict__['age'], 25)

    def test_save(self):
        """Test save method"""

        st = State()
        temp = st.__dict__['updated_at']
        self.assertFalse(path.isfile('file.json'))
        st.save()
        self.assertTrue(path.isfile('file.json'))
        self.assertNotEqual(st.__dict__['updated_at'], temp)
        temp = st.__dict__['updated_at']
        models.storage.reload()
        self.assertEqual(st.__dict__['updated_at'], temp)

    def test_to_dict(self):
        """Test to_dict method"""

        st = State()
        st.age = 28
        st.size = "tall"
        for k, v in st.__dict__.items():
            if k != 'updated_at' and k != 'created_at':
                self.assertIn(k, st.to_dict())
                self.assertEqual(v, st.to_dict()[k])
        self.assertEqual(st.to_dict()['__class__'], st.__class__.__name__)
        self.assertEqual(st.to_dict()['updated_at'], st.updated_at.isoformat())
        self.assertEqual(st.to_dict()['created_at'], st.created_at.isoformat())
        self.assertEqual(st.to_dict()['age'], 28)
        self.assertEqual(st.to_dict()['size'], 'tall')
        self.assertIsInstance(st.to_dict(), dict)

    def test_str(self):
        """Test __str__ method"""

        st = State()
        string = '['+st.__class__.__name__+']'+' ('+st.id+') '+str(st.__dict__)
        self.assertEqual(string, st.__str__())
>>>>>>> c5c69c3b281ca80047e1f7969e0cd1ee2d9e23eb
