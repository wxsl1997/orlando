import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(sender, receiver, subject, content, authorization, attachments=None):
    msg = MIMEMultipart()
    text = MIMEText(content)
    msg.attach(text)

    if attachments:
        docFile = attachments
        payload = MIMEApplication(open(docFile, 'rb').read())
        payload.add_header('Content-Disposition', 'attachment', filename=docFile)
        msg.attach(payload)
        print(f'attach file: {attachments}')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    smtp = None
    try:
        print(f"start to send mail, sender: {sender}, receiver:{receiver}, subject:{subject}")
        smtp = smtplib.SMTP_SSL("smtp.163.com", 465)
        smtp.login(sender, authorization)
        smtp.sendmail(sender, receiver, msg.as_string())
        print(f"mail send success, sender:{sender}, receiver:{receiver}, subject:{subject}")
    except smtplib.SMTPException as e:
        print(f"mail  send failed, sender:{sender}, receiver:{receiver}, subject:{subject}, error:{e}")
    finally:
        smtp.quit()


if __name__ == '__main__':
    mail_sender = 'wxsl1997@163.com'
    mail_receiver = 'xiusen1997@163.com'
    mail_subject = 'mail case subject'
    mail_content = "this is mail content !!!"
    attachments_path = '图片-英文.png'
    authorization = 'xxx'
    send_email(mail_sender, mail_receiver, mail_subject, mail_content, authorization, attachments_path)
