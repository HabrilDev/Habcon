import logging
import os
import smtplib
import ssl
import time
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

logging.basicConfig(filename="RPI_Temp.log", format="%(asctime)s - %(levelname)s - %(message)s", filemode="w")
logger = logging.getLogger()
logger.setLevel(logging.INFO)

subject = "Problem In RPI Server"
body = """\
Hello, 
Temperature of RPI server has reached threshold 57°C.
Regards Boldmoon Servers Node1,
Automated Python message"""
sender_email = "-"
receiver_email1 = "1"
receiver_email2 = "2"
receiver_email3 = "3"
receiver_emailBCC = "4"
password = "pwd"


def measure_temp():
    temp = os.popen("vcgencmd measure_temp | egrep -o '[0-9]*\.[0-9]*'").readline()
    temp = float(temp)
    return temp


while measure_temp() < 57.0:
    logger.info(measure_temp())
    time.sleep(60)


logger.critical(measure_temp())
logger.critical("Temperature reached threshold 57°C.")

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email1
message["Subject"] = subject
message["Bcc"] = receiver_emailBCC


message.attach(MIMEText(body, "plain"))

filename = "RPI_Temp.log"


with open(filename, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

encoders.encode_base64(part)


part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)


message.attach(part)
text = message.as_string()


context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email1, text)
    server.sendmail(sender_email, receiver_email2, text)
    server.sendmail(sender_email, receiver_email3, text)

os.system('sudo shutdown now')
