import datetime
import smtplib


while True:

    def emailDefault():

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        server.login("xav.jobin97@gmail.com","Iact1v1ty")



        server.sendmail("xav.jobin97@gmail.com", "marc.jobin@gmail.com", "It's 2:45 o' clock!")

        server.quit 


    now = str(datetime.datetime.utcnow().strftime("%H:%M"))


    if now == "19:45":
        print("Sending...")
        emailDefault()
        print("Stopping...")
        quit()
        

    else:
        pass


