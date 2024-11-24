# 3. Ejercicio Avanzado: Implementa un fake de un sistema de archivos. Crea un
# servicio que lea y escriba archivos. Escribe pruebas unitarias que
# verifiquen que los archivos se leen y escriben correctamente en un entorno
# controlado utilizando el fake.
class FakeFileSystem:
    def __init__(self):
        self.data = {}

    def getFiles(self):
        """
        Obtener lista de archivos.

        Returns:
            array: Lista de archivos almacenados.
        """
        return self.data

    def saveFile(self, book):
        """
        Almacenar un libro.

        Args:
            book (array): Array clave/valor. La clave es el nombre
            del libro, el valor será la cadena asociada a este.

        Returns:
            None
        """

        key = book['key']
        message = book['value']
        if (
            ([key] is None or not isinstance(key, str))
            or
            (key is None or not isinstance(message, str))
        ):
            return "Invalid key or value"

        self.data[key] = message

    def readFile(self, key):
        """
        Leer un archivo.

        Args:
            key (int o float): Key del archivo a leer.

        Returns:
            string: valor asociado al libro solicitado.
        """
        file = self.data.get(key)
        if file is None:
            return "File not found"
        return file

    def updateFile(self, book):
        """
        Actualizar el valor de un libro.

        Args:
            book (array): Array clave/valor. La clave es el nombre
            del libro, el valor será la cadena que se va actualizar.

        Returns:
            None
        """
        key = book['key']
        value = book['value']

        file = self.data.get(key)
        if file is None:
            return "File not found"
        self.data[key] = value
