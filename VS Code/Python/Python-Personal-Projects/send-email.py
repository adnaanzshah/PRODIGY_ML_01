import smtplib


sender_email = "slicewar100@gmail.com"
# get it from app passwords in google->manage accounts
sender_password = "xrwi lijb ukeb whqo"
receiver_email = "adishah6750@gmail.com"

msg=input("Enter the msg : ")
with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg)