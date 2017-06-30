import smtplib

fromaddr = 'dane.miller.info3180@gmail.com'

fromname = 'Dane Miller'

#toaddr  = 'info3180.justenmorgan@gmail.com'
toaddr  = 'dane.miller.info3180@gmail.com'

toname = "Raphy Col"

msg = "Hey Bro info3180 is so fun"

subject = "INFO3180"

message = """
From: {} <{}>
To: {} <{}>
Subject: {}


{}
"""

messagetosend = message.format(

                             fromname,

                             fromaddr,

                             toname,

                             toaddr,

                             subject,

                             msg)


# Credentials (if needed)

username = 'dane.miller.info3180@gmail.com'

password = 'ubsjbwmxmqsxufyl'

# The actual mail send

server = smtplib.SMTP('smtp.gmail.com:587')

server.starttls()

server.login(username, password)

server.sendmail(fromaddr, toaddr, messagetosend)

server.quit()