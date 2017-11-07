import smtplib

server = smtplib.SMTP('webmail.whro.org', 25)
#server.starttls()
#server.login("digital\glennh", "S!l1c0ne")

msg = "py test"
server.sendmail("glennh@whro.org", "glennh@whro.org", msg)
server.quit()
