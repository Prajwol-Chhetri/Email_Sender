import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = '#Name of the sender'
email['to'] = '#email address of the receiver'
email['subject'] = '#subject for the email'

email.set_content('#CONTENT FOR THE EMAIL')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('#GMAIL ACCOUNT OF SENDER', '#PASSWORD OF ACCOUNT')
	smtp.send_message(email)
	print('email sent')