#!/usr/bin/env python3

#file defining two funcitons to be used by report_email.py to send emails

import email.message
import mimetypes
import os.path
import smtplib

#creates a message object
def generate_email(sender, recipient, subject, body, attachment):
  message = email.message.EmailMessage()
  message["From"] = sender
  message["To"] = recipient
  message["Subject"] = subject
  message.set_content(body)

  afile_name = os.path.basename(attachment)
  mime_type, _ = mimetypes.guess_type(attachment)
  mime_type, mime_subtype = mime_type.split('/',1)

  with open(attachment, 'rb') as ap:
    message.add_attachment(ap.read(),maintype=mime_type,subtype=mime_subtype,filename=afile_name)

  return message

#sends a message object using SMTP protocal
def send_email(message):
  mail_server = smtplib.SMTP('localhost')
  mail_server.send_message(message)
  mail_server.quit()

