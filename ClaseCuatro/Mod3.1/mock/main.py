# 2. Ejercicio Intermedio: Usando un mock, escribe una prueba para verificar
# que una función que envía un correo electrónico a un usuario ha sido llamada
# correctamente con los parámetros adecuados (por ejemplo, el correo del
# usuario y el mensaje).


class Mailable:
    def sendEmail(self, email, message):
        """
        Envía un correo electrónico.

        Args:
            email (string): Destinatario.
            message (string): Mensaje a enviar

        Returns:
            string: confirmación de envío de correo
        """
        if (
            (email is None or not isinstance(email, str))
            or
            (message is None or not isinstance(message, str))
        ):
            return "Invalid email o message"
        # Lógica de envío de correo
        return "Email sended"
