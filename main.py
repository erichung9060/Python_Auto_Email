import smtplib
from email.mime.text import MIMEText

# 讀取郵件地址列表和信件內容
with open('email_list.txt', 'r') as file:
    email_list = file.read().splitlines()

with open('password.txt', 'r') as file:
    passwords = file.read().splitlines()

with open('account.txt', 'r') as file:
    accounts = file.read().splitlines()

with open('name.txt', 'r') as file:
    names = file.read().splitlines()

with open('content_template.txt', 'r') as file:
    content_template = file.read()

# SMTP服務器設置（以Gmail為例）
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'gmail account'
smtp_password = 'gmail app password'

# 創建SMTP連接
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(smtp_username, smtp_password)

# 發送郵件
for destination, account, name, password in zip(email_list, accounts, names, passwords):
    print("Sending to " + destination + " ...")
    content = content_template + '\n'
    content += "\nName : " + name + "\nUsername : " + account + "\nPassword : " + password
    msg = MIMEText(content)
    msg['Subject'] = 'PD1 Midterm Judge Account and Password'
    msg['From'] = smtp_username
    msg['To'] = destination

    print(content + '\n')
    server.send_message(msg)

# 關閉連接
server.quit()
