import smtplib

# Configurar servidor SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'sopadecaracol123123@gmail.com'
smtp_password = 'Saban1808*'
smtp_sender = 'yosoysaban@gmail.com'

# Crear mensaje
message = """\
Subject: ¡Hola!

Hola,

Este es un mensaje de prueba enviado desde Python.

Saludos,
Tu Nombre"""

# Enviar correo electrónico
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(smtp_sender, 'DESTINATARIO', message)

# Imprimir mensaje de éxito
print('Correo electrónico enviado')
