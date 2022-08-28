#!/usr/bin/env python3

import shutil
import psutil
import socket
import emails


fr = "automation@example.com"
to = "student-03-7ef7402584ed@example.com"
body = "Please check your system and resolve the issue as soon as possible."

cpu_usage = psutil.cpu_percent(1)
disk_usage = psutil.disk_usage("/")
hostname = socket.gethostbyname('localhost')
memory = dict(psutil.virtual_memory()._asdict())['available']

free_disk = disk_usage.free / disk_usage.total * 100
available_memory = (memory / 1024) / 1024

if cpu_usage > 80:
  subject = "Error - CPU usage is over 80%"
  mail = emails.generate_error_report(fr,to,subject,body)
  emails.send_email(mail)

if free_disk > 80:
  subject = "Error - Available disk space is less than 20%"
  mail = emails.generate_error_report(fr,to,subject,body)
  emails.send_email(mail)

if available_memory > 500:
  subject = "Error - Available memory is less than 500MB"
  mail = emails.generate_error_report(fr,to,subject,body)
  emails.send_email(mail)

if hostname != '127.0.0.1':
  subject = "Error - localhost cannot be resolved to 127.0.0.1"
  mail = emails.generate_error_report(fr,to,subject,body)
  emails.send_email(mail)

