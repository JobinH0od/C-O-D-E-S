import datetime
import smtplib

def emailDefault():

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    server.login("xav.jobin97@gmail.com","Iact1v1ty")



    server.sendmail("xav.jobin97@gmail.com", "marc.jobin@gmail.com", "TEST")

    server.quit 

emailDefault()