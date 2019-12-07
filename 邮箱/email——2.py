import smtplib

import string

from email.mime.text import MIMEText

HOST = "smtp-mail.outlook.com"

FROM = "shaojunshuai2020@outlook.com"

SUBJECT = "this is a test"

TO = "2319898127@qq.com"

TEXT = "good to see you"

BODY = string.join((

    "from: %s" % FROM,

    "to: %s" % TO,

    "Subject: %s" % SUBJECT,

    "", TEXT

), "\r\n")

server = smtplib.SMTP()

server.connect(HOST, "25")  # 这个端口貌似不对，不过好像没影响

server.starttls()

server.login(FROM, "xtrwhadykudmozrb")

server.sendmail(FROM, TO, BODY)

server.close()
