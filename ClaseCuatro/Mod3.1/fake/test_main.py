import unittest
from main import FakeFileSystem


class TestFakeFileSystem(unittest.TestCase):
    def test_get_files(self):
        """Esta prueba obtiene la lista de libros"""
        fake_db = FakeFileSystem()
        result = fake_db.getFiles()
        expected_value = {}
        self.assertEqual(result, expected_value)

    def test_sucessfull_save_file(self):
        """Esta prueba verifica el correcto almacenado de un libro"""
        fake_db = FakeFileSystem()
        book = {
            "key": "book1",
            "value": "This is the book one"
        }
        fake_db.saveFile(book)
        expected_value = {
            "book1": "This is the book one"
        }
        get_files = fake_db.getFiles()
        self.assertEqual(get_files, expected_value)

    def test_failed_save_file(self):
        """Esta prueba verifica un valor esperado incorrecto"""
        fake_db = FakeFileSystem()
        book = {
            "key": "book1",
            "value": "This is the book one"
        }
        book2 = {
            "key": "book2",
            "value": "This is the book two"
        }
        fake_db.saveFile(book)
        fake_db.saveFile(book2)
        expected_value = {
            "book1": "This is the book one"
        }
        get_files = fake_db.getFiles()
        self.assertNotEqual(get_files, expected_value)

    def test_successfull_update_file(self):
        """Esta prueba verifica la correcta actualización de un libro"""
        fake_db = FakeFileSystem()
        book = {
            "key": "book1",
            "value": "This is the book one"
        }
        book2 = {
            "key": "book2",
            "value": "This is the book two"
        }
        fake_db.saveFile(book)
        fake_db.saveFile(book2)
        fake_db.updateFile({
            "key": "book1",
            "value": "This is the book one updated"
        })
        expected_value = {
            "book1": "This is the book one updated",
            "book2": "This is the book two"
        }
        get_files = fake_db.getFiles()
        self.assertEqual(get_files, expected_value)


if __name__ == "__main__":
    unittest.main()
