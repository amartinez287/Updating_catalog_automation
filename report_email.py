#!/usr/bin/env python3

#script used to build a pdf file with fruits descriptions and send an email with the pdf

import os
import datetime
import reports
import emails

src = "/home/student-03-7ef7402584ed/supplier-data/descriptions"
attachment = "/tmp/processed.pdf"

# function loops through all txt files in src and builds the body of the pdf
def make_paragraph(path):
  files = os.listdir(path)
  paragraph = ""
  for file in files:
    with open(os.path.join(path,file)) as f:
      name = f.readline().strip()
      weight = f.readline().strip()
      paragraph += ("name: " + name + "<br/>")
      paragraph += ("weight: " + weight + "<br/><br/>")
  return(paragraph)

# function calls make paragraph to create contents of the pdf
# then gets and formats current date for the pdf title
# finally calls functions from emails.py to send the email and pdf
def main():
  p = make_paragraph(src)
  now = datetime.date.today()
  month = now.strftime("%B")
  day = now.strftime("%d")
  year = now.strftime("%Y")
  title =("Processed Update on " + month + " " + day + ", " + year)

  reports.generate_report(attachment,title,p)

  fr = "automation@example.com"
  to = "student-03-7ef7402584ed@example.com"
  sub = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

  message = emails.generate_email(fr,to,sub,body,attachment)
  emails.send_email(message)

if __name__ == "__main__":
  main()
