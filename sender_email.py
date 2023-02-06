import smtplib

sender_email = "youraddress@gmail.com"
receiver_email = "youraddress@gmail.com"
password = "password"

message = """Subject: Test Email

This is a test email sent from Python."""

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    print("Email sent!")
except Exception as e:
    print(f"Something went wrong... {e}")
finally:
    server.quit()
