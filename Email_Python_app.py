import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration
sender_email = "dularasenavirathne321@gmail.com"
receiver_email = "chamodilakshika650@gmail.com"
password = "yrgy fwiv ewsl scwa"  # Replace with your email password

# Create the email content
subject = "Automated Email from Python"
body = "onna balaganna. python walin karana weda.. meka automate kare python walin mn vedio ekak dannmko.. saasdjadsh ahdssdh  "

# Create a multipart message
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# Attach the email body to the message
message.attach(MIMEText(body, "plain"))

# Send the email
try:
    # Establish a secure session with the SMTP server
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)  # Login to the email account
        server.sendmail(sender_email, receiver_email, message.as_string())  # Send the email
    print("Email sent successfully!")
except Exception as e:
    print(f"Error occurred: {e}")
