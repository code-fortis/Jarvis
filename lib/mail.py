#!/usr/bin/env python
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def mailer(SUBJECT, BODY, TO, FROM):
    """With this function we send out our html email"""
 
    # Create message container - the correct MIME type is multipart/alternative here!
    MESSAGE = MIMEMultipart('alternative')
    MESSAGE['subject'] = SUBJECT
    MESSAGE['To'] = TO
    MESSAGE['From'] = FROM
 
    # Record the MIME type text/html.
    HTML_BODY = MIMEText(BODY, 'html')
 
    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    MESSAGE.attach(HTML_BODY)
 
    # The actual sending of the e-mail
    server = smtplib.SMTP('smtp.xilinx.com')
 
    # Print debugging output when testing
    if __name__ == "__main__":
        server.set_debuglevel(1)
 
    # Credentials (if needed) for sending the mail
    #password = "mypassword"
 
    #server.starttls()
    #server.login(FROM,password)
    server.sendmail(FROM, [TO], MESSAGE.as_string())
    server.quit()
 
if __name__ == "__main__":
    """Executes if the script is run as main script (for testing purposes)"""
 
    email_content = """
 
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>html title</title>
  <style type="text/css" media="screen">
    table{
        background-color: #AAD373;
        empty-cells:hide;
    }
    td.cell{
        background-color: white;
    }
  </style>
 
 
 
<table style="border: blue 1px solid;">
 
<tbody>
<tr>
<td class="cell">Cell 1.1</td>
<td class="cell">Cell 1.2</td>
</tr>
 
 
<tr>
<td class="cell">Cell 2.1</td>
<td class="cell"></td>
</tr>
 
</tbody>
</table>
 
 
"""
 
    TO = 'akshayag@xilinx.com'
    FROM ='sender@mysite.com'
 
    mailer("Test email subject", email_content, TO, FROM)