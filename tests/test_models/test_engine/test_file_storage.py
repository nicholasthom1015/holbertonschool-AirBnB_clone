#!/usr/bin/python3
""" Base Class Test Cases"""
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):

    file_storage_tester = None
    NeedCleanup = False

    def test_contructors(self):
        self.file_storage_tester.reload()
        start_count = len(self.file_storage_tester.all())
        obj = BaseModel()
        self.file_storage_tester.new(obj)
        self.assertEqual(len(self.file_storage_tester.all()), start_count + 1)
        pass

    def tearDown(self) -> None:
        if self.NeedCleanup:
            if os.path.exists("file.json"):
                os.remove("file.json")
            os.rename("temp.json", "file.json")
        return super().tearDown()

    def setUp(self):
        """initialize objects and file storage instance"""
        if os.path.exists("file.json"):
            os.rename("file.json", "temp.json")
            self.NeedCleanup = True
        self.obj1 = BaseModel(**{"id": 1, "name": "Test1"})
        self.obj2 = BaseModel(**{"id": 2, "name": "Test2"})
        self.file_storage_tester = FileStorage()

    def test_all(self):
        """Test if all method retrieves objects correctly"""
        start = len(self.file_storage_tester.all())
        self.file_storage_tester.new(self.obj1)
        self.file_storage_tester.new(self.obj2)
        self.assertEqual(len(self.file_storage_tester.all()), start + 2)

    def test_new(self):
        """Test if new method adds object to __objects correctly"""
        self.file_storage_tester.new(self.obj1)
        self.assertIn(self.obj1, self.file_storage_tester.all().values())

    def test_remove_method(self):
        """Tests if the remove method deletes an object from the dict"""
        self.file_storage_tester.remove("BaseModel.{}".format(self.obj1.id))
        all_objects = self.file_storage_tester.all()
        self.assertNotIn("BaseModel.{}".format(self.obj1.id), all_objects)

    def test_reload(self):
        """Test if reload method loads objects from file correctly"""
        self.file_storage_tester.new(self.obj1)
        self.file_storage_tester.new(self.obj2)
        preSaveAll = self.file_storage_tester.all()
        self.file_storage_tester.save()
        self.file_storage_tester.__objects = {}
        self.file_storage_tester.reload()
        self.assertDictEqual(self.file_storage_tester.all(), preSaveAll)

    def test_save_method(self):
        """Tests if the save method creates a file with the objects data"""
        self.file_storage_tester.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_all_method(self):
        """Tests if the all method returns a dict"""
        self.assertIsInstance(storage.all(), dict)