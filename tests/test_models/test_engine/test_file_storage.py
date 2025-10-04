#!/usr/bin/python3
<<<<<<< HEAD
"""test for file storage"""
import unittest
import pep8
import json
import os
=======
"""
Unittest for the FileStorage class
Test files by using the following command line:
python3 -m unittest tests/test_models/test_engine/test_file_storage.py
"""
import unittest
import pep8
import json
from os import path, remove
>>>>>>> c5c69c3b281ca80047e1f7969e0cd1ee2d9e23eb
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
<<<<<<< HEAD
=======
from models.engine import file_storage
>>>>>>> c5c69c3b281ca80047e1f7969e0cd1ee2d9e23eb
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
<<<<<<< HEAD
    '''this will test the FileStorage'''

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.user = User()
        cls.user.first_name = "Kev"
        cls.user.last_name = "Yo"
        cls.user.email = "1234@yahoo.com"
        cls.storage = FileStorage()

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.user

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_FileStorage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_all(self):
        """tests if all works in File Storage"""
        storage = FileStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._FileStorage__objects)

    def test_new(self):
        """test when new is created"""
        storage = FileStorage()
        obj = storage.all()
        user = User()
        user.id = 123455
        user.name = "Kevin"
        storage.new(user)
        key = user.__class__.__name__ + "." + str(user.id)
        self.assertIsNotNone(obj[key])

    def test_reload_filestorage(self):
        """
        tests reload
        """
        self.storage.save()
        Root = os.path.dirname(os.path.abspath("console.py"))
        path = os.path.join(Root, "file.json")
        with open(path, 'r') as f:
            lines = f.readlines()
        try:
            os.remove(path)
        except:
            pass
        self.storage.save()
        with open(path, 'r') as f:
            lines2 = f.readlines()
        self.assertEqual(lines, lines2)
        try:
            os.remove(path)
        except:
            pass
        with open(path, "w") as f:
            f.write("{}")
        with open(path, "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(self.storage.reload(), None)


if __name__ == "__main__":
    unittest.main()
=======
    """define variables and methods"""

    def setUp(self):
        """
        Sets the private class attributes __file_path and __objects back to
        'file.json' and {}, respectively
        Method called to prepare the test fixture. This is called immediately
        before calling the test method; other than AssertionError or SkipTest
        """
        FileStorage._FileStorage__file_path = 'file.json'
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """
        Sets the private class attributes __file_path and __objects back to
        'file.json' and {}, respectively
        Method called immediately after the test method has been called and
        the result recorded
        """
        del FileStorage._FileStorage__file_path
        del FileStorage._FileStorage__objects
        if path.exists("file.json"):
            remove("file.json")

    def test_pep8_conformance(self):
        """Test that FileStorage conforms to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_class_method_presence(self):
        """Test that the FileStorage methods are all present"""
        l1 = dir(FileStorage)
        self.assertIn('all', l1)
        self.assertIn('new', l1)
        self.assertIn('save', l1)
        self.assertIn('reload', l1)

    def test_class_attribute_presence(self):
        """Test that the FileStorage attributes are all present"""
        l1 = dir(FileStorage)
        self.assertIn('_FileStorage__file_path', l1)
        self.assertIn('_FileStorage__objects', l1)

    def test_instance_method_presence(self):
        """Test that the FileStorage instance as the same methods"""
        l1 = dir(FileStorage())
        self.assertIn('all', l1)
        self.assertIn('new', l1)
        self.assertIn('save', l1)
        self.assertIn('reload', l1)

    def test_instance_attribute_presence(self):
        """Test that the FileStorage instance has the same attributes"""
        l1 = dir(FileStorage())
        self.assertIn('_FileStorage__file_path', l1)
        self.assertIn('_FileStorage__objects', l1)

    def test_docstring_presence(self):
        """Test that Module, Class, and methods all have a docstring"""
        self.assertIsNot(file_storage.__doc__, None)
        self.assertIsNot(FileStorage.__doc__, None)
        self.assertIsNot(FileStorage.all.__doc__, None)
        self.assertIsNot(FileStorage.new.__doc__, None)
        self.assertIsNot(FileStorage.save.__doc__, None)
        self.assertIsNot(FileStorage.reload.__doc__, None)

    def test_instantiation(self):
        """Test proper instantiation of object 'storage'"""

        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)
        self.assertEqual(FileStorage._FileStorage__file_path, 'file.json')
        self.assertEqual(FileStorage._FileStorage__objects, {})

    def test_new(self):
        """Test the new method"""

        storage = FileStorage()

        ba = BaseModel()
        storage.new(ba)
        self.assertEqual(FileStorage._FileStorage__objects[ba.__class__.
                                               __name__+'.'+ba.id], ba)

        us = User()
        storage.new(us)
        self.assertEqual(FileStorage._FileStorage__objects[us.__class__.
                                               __name__+'.'+us.id], us)

        st = State()
        storage.new(st)
        self.assertEqual(FileStorage._FileStorage__objects[st.__class__.
                                               __name__+'.'+st.id], st)

        ci = City()
        storage.new(ci)
        self.assertEqual(FileStorage._FileStorage__objects[ci.__class__.
                                               __name__+'.'+ci.id], ci)

        am = Amenity()
        storage.new(am)
        self.assertEqual(FileStorage._FileStorage__objects[am.__class__.
                                               __name__+'.'+am.id], am)

        pl = Place()
        storage.new(pl)
        self.assertEqual(FileStorage._FileStorage__objects[pl.__class__.
                                               __name__+'.'+pl.id], pl)

        re = Review()
        storage.new(re)
        self.assertEqual(FileStorage._FileStorage__objects[re.__class__.
                                               __name__+'.'+re.id], re)

    def test_all(self):
        """Test the all method"""

        storage = FileStorage()

        ba = BaseModel()
        self.assertIsInstance(storage.all(), dict)
        self.assertEqual(storage.all()[ba.__class__.__name__+'.'+ba.id], ba)

        us = User()
        self.assertIsInstance(storage.all(), dict)
        self.assertEqual(storage.all()[us.__class__.__name__+'.'+us.id], us)

        st = State()
        self.assertIsInstance(storage.all(), dict)
        self.assertEqual(storage.all()[st.__class__.__name__+'.'+st.id], st)

        ci = City()
        self.assertIsInstance(storage.all(), dict)
        self.assertEqual(storage.all()[ci.__class__.__name__+'.'+ci.id], ci)

        am = Amenity()
        self.assertIsInstance(storage.all(), dict)
        self.assertEqual(storage.all()[am.__class__.__name__+'.'+am.id], am)

        pl = Place()
        self.assertIsInstance(storage.all(), dict)
        self.assertEqual(storage.all()[pl.__class__.__name__+'.'+pl.id], pl)

        re = Review()
        self.assertIsInstance(storage.all(), dict)
        self.assertEqual(storage.all()[re.__class__.__name__+'.'+re.id], re)

    def test_save(self):
        """Test the save method"""

        storage = FileStorage()

        storage.save()
        self.assertTrue(path.isfile('file.json'))
        with open("file.json") as f:
            self.assertEqual(f.read(), '{}')

        ba = BaseModel()
        storage.save()
        self.assertTrue(path.isfile('file.json'))
        with open("file.json") as f:
            self.assertIsInstance(json.loads(f.read()), dict)
        with open("file.json") as f:
            self.assertEqual(json.loads(f.read())
                             [ba.__class__.__name__+'.'+ba.id], ba.to_dict())

        us = User()
        storage.save()
        self.assertTrue(path.isfile('file.json'))
        with open("file.json") as f:
            self.assertIsInstance(json.loads(f.read()), dict)
        with open("file.json") as f:
            self.assertEqual(json.loads(f.read())
                             [us.__class__.__name__+'.'+us.id], us.to_dict())

        st = State()
        storage.save()
        self.assertTrue(path.isfile('file.json'))
        with open("file.json") as f:
            self.assertIsInstance(json.loads(f.read()), dict)
        with open("file.json") as f:
            self.assertEqual(json.loads(f.read())
                             [st.__class__.__name__+'.'+st.id], st.to_dict())

        ci = City()
        storage.save()
        self.assertTrue(path.isfile('file.json'))
        with open("file.json") as f:
            self.assertIsInstance(json.loads(f.read()), dict)
        with open("file.json") as f:
            self.assertEqual(json.loads(f.read())
                             [ci.__class__.__name__+'.'+ci.id], ci.to_dict())

        am = Amenity()
        storage.save()
        self.assertTrue(path.isfile('file.json'))
        with open("file.json") as f:
            self.assertIsInstance(json.loads(f.read()), dict)
        with open("file.json") as f:
            self.assertEqual(json.loads(f.read())
                             [am.__class__.__name__+'.'+am.id], am.to_dict())

        pl = Place()
        storage.save()
        self.assertTrue(path.isfile('file.json'))
        with open("file.json") as f:
            self.assertIsInstance(json.loads(f.read()), dict)
        with open("file.json") as f:
            self.assertEqual(json.loads(f.read())
                             [pl.__class__.__name__+'.'+pl.id], pl.to_dict())

        re = Review()
        storage.save()
        self.assertTrue(path.isfile('file.json'))
        with open("file.json") as f:
            self.assertIsInstance(json.loads(f.read()), dict)
        with open("file.json") as f:
            self.assertEqual(json.loads(f.read())
                             [re.__class__.__name__+'.'+re.id], re.to_dict())

    def test_reload(self):
        """Test the reload method"""

        storage = FileStorage()

        ba = BaseModel()
        storage.save()
        storage.reload()
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)
        self.assertIsInstance(FileStorage._FileStorage__objects
                              [ba.__class__.__name__+'.'+ba.id], BaseModel)
        self.assertEqual(FileStorage._FileStorage__objects
                         [ba.__class__.__name__+'.'+ba.id].to_dict(),
                         ba.to_dict())

        us = User()
        storage.save()
        storage.reload()
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)
        self.assertIsInstance(FileStorage._FileStorage__objects
                              [us.__class__.__name__+'.'+us.id], User)
        self.assertEqual(FileStorage._FileStorage__objects
                         [us.__class__.__name__+'.'+us.id].to_dict(),
                         us.to_dict())

        st = State()
        storage.save()
        storage.reload()
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)
        self.assertIsInstance(FileStorage._FileStorage__objects
                              [st.__class__.__name__+'.'+st.id], State)
        self.assertEqual(FileStorage._FileStorage__objects
                         [st.__class__.__name__+'.'+st.id].to_dict(),
                         st.to_dict())

        ci = City()
        storage.save()
        storage.reload()
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)
        self.assertIsInstance(FileStorage._FileStorage__objects
                              [ci.__class__.__name__+'.'+ci.id], City)
        self.assertEqual(FileStorage._FileStorage__objects
                         [ci.__class__.__name__+'.'+ci.id].to_dict(),
                         ci.to_dict())

        am = Amenity()
        storage.save()
        storage.reload()
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)
        self.assertIsInstance(FileStorage._FileStorage__objects
                              [am.__class__.__name__+'.'+am.id], Amenity)
        self.assertEqual(FileStorage._FileStorage__objects
                         [am.__class__.__name__+'.'+am.id].to_dict(),
                         am.to_dict())

        pl = Place()
        storage.save()
        storage.reload()
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)
        self.assertIsInstance(FileStorage._FileStorage__objects
                              [pl.__class__.__name__+'.'+pl.id], Place)
        self.assertEqual(FileStorage._FileStorage__objects
                         [pl.__class__.__name__+'.'+pl.id].to_dict(),
                         pl.to_dict())

        re = Review()
        storage.save()
        storage.reload()
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)
        self.assertIsInstance(FileStorage._FileStorage__objects
                              [re.__class__.__name__+'.'+re.id], Review)
        self.assertEqual(FileStorage._FileStorage__objects
                         [re.__class__.__name__+'.'+re.id].to_dict(),
                         re.to_dict())
>>>>>>> c5c69c3b281ca80047e1f7969e0cd1ee2d9e23eb
