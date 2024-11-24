import unittest
from unittest.mock import MagicMock
from main import Mailable


class TestMailable(unittest.TestCase):
    def test_mailable(self):
        """
        Esta prueba verifica la correcta llamada de la función
        de envío de un correo
        """
        service = Mailable()
        service.sendEmail = MagicMock(return_value="response")
        service.sendEmail()
        service.sendEmail()
        service.sendEmail.assert_called_once()


if __name__ == "__main__":
    unittest.main()
