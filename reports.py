#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Spacer, Table, Image


def generate_report(attachment,title,paragraph)
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(attachment)
  report_title = Paragraph(title, styles["h1"])
  report_body = Paragraph(paragraph, styles["BodyText"])
  report.build([report_title,report_body])
