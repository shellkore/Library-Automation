def send(bookname):
	import smtplib
	smtp = smtplib.SMTP('smtp.gmail.com',587)

	smtp.starttls()		#starting transport layer security

	with open('data.json') as json_file:
		data = json.load(json_file)

	smtp.login(data['email'],data['emailpass'])

	message = "You need to manually reissue the book ${bookname}"

	smtp.sendmail(data['email'],data['email'], message)

	smtp.quit()