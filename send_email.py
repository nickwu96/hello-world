import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


def send(subject='邮件主题', text='空'):
    my_sender = '****'
    my_pass = '****'
    my_user = '****'

    msg = MIMEText(text, 'plain', 'utf-8')
    msg['From'] = formataddr(["服务器通知", my_sender])
    msg['To'] = formataddr(["收件人姓名", my_user])
    msg['Subject'] = subject

    try:
        server = smtplib.SMTP_SSL("smtp.***.com", port=465)  # 发件人邮箱中的SMTP服务器，SSL端口是465
        server.login(my_sender, my_pass)
        server.sendmail(my_sender, [my_user, ], msg.as_string())
        server.quit()  # 关闭连接
        print("邮件发送成功！")
    except:
        print("邮件发送失败！")
