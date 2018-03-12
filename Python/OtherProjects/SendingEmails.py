import smtplib

	
	
def sendEmails():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	
	email = input("Enter you're email adress : ")
	psw = input("Enter you're password : ")
	
	server.login(email, psw)

	
	
	msg = input("Type the message you want to send : ")
	
	receiver = input("Enter the email you want to send you're message to : ")
	
	server.sendmail(email, receiver, msg)
	print("")
	print("")
	print("Done... You're email was sent to : ", receiver)
	print("")
	print("The email sent contained this : ")
	print("-----")
	print(msg)
	print("-----")
	
	server.quit
	
	input()
	
sendEmails()