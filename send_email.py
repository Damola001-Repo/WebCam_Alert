import smtplib
from email.message import EmailMessage
import os
from PIL import Image

PASSWORD = os.getenv('PASSWORD2')
SENDER = 'damolabalogun79@gmail.com'
RECEIVER = 'damolabalogun79@gmail.com'

def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "New customer showed up!"
    email_message.set_content("Hey, we just saw a new customer!")

    try:
        with Image.open(image_path) as img:
            format = img.format.lower()
            mime_type = f'image/{format}'
    except Exception as e:
        mime_type = 'application/octet-stream'

    main_type, sub_type = mime_type.split('/', 1)

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=sub_type)

    gmail = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    gmail.ehlo()
    # gmail.starttls()
    gmail.ehlo()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()

if __name__ == "__main__":
    send_email("images/19.png")