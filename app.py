import smtplib
import email.message


def enviar_email():
    # Lendo o conteúdo do arquivo HTML
    with open("index.html", "r", encoding="utf-8") as arquivo_html:
        corpo_email = arquivo_html.read()

    msg = email.message.Message()
    msg['Subject'] = "E-Mail automatico"
    msg['From'] = 'bscbreno1904@gmail.com'

    # List of email addresses as recipients
    recipients = ['brenos200304@gmail.com', 'brenoc200304@gmail.com']
    msg['To'] = ', '.join(recipients)

    password = "zaxqpypgchmbsfwf"

    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    # Login Credentials para enviar o e-mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], recipients, msg.as_string().encode('utf-8'))

    print('E-mail enviado')


# Chamando a função para enviar o e-mail
enviar_email()