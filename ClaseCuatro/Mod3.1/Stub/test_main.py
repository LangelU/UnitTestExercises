import unittest
from main import ApiService


class TestApiService(unittest.TestCase):
    def setUp(self):
        """
            Inicializar la clase
        """
        self.service = ApiService()

    def test_successfull_authentication_from_api_returns_data(self):
        """
            Esta prueba verifica la correcta autenticación en una
            api externa
        """
        credentials = {
            "user": "user@gmail.com",
            "password": "12345"
        }

        self.service.authenticate = lambda: self.stub_authenticate(credentials)

        result = self.service.authenticate()

        self.assertIsInstance(result, dict)
        self.assertEqual(result, {
            "token": "ghp|jsh82msns"
        })

    def test_failed_authentication_from_api_returns_data(self):
        """
            Definir el array con las credenciales que se
            usarán para la prueba
        """
        credentials = {
            "user": "user2@gmail.com",
            "password": "12345"
        }

        self.service.authenticate = lambda: self.stub_authenticate(credentials)

        result = self.service.authenticate()

        self.assertIsInstance(result, dict)
        self.assertEqual(result, {
            "error": "Invalid credentials"
        })

    def stub_authenticate(self, credentials):
        user = "user@gmail.com"
        password = "12345"

        """
            Validar si las credenciales recibidas coinciden,
            en cuyo caso authenticar. Retornar error de lo contrario
        """
        if credentials['user'] == user and credentials['password'] == password:
            return {
                "token": "ghp|jsh82msns"
            }
        else:
            return {
                "error": "Invalid credentials"
            }

    def tearDown(self):
        self.service = None


if __name__ == "__main__":
    unittest.main()
