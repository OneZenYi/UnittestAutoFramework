"""
@file: Email.py
@copyright: laoZ
"""
import os,time,smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from Config.EmailConfig import mail_host,mail_pass,mail_user,sender,receivers

def email():

    # 附件一：路径
    report_filen = os.path.dirname(os.path.dirname(__file__)) + '/report/TestReport.html'

    # 创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = Header("自动化测试组", 'utf-8')
    message['To'] = Header("测试", 'utf-8')
    subject = '【自动化测试】接口测试报告 ' + time.strftime('%Y-%m-%d', time.localtime(time.time()))
    message['Subject'] = Header(subject, 'utf-8')

    # 邮件正文内容
    message.attach(MIMEText('Hi ALL' + '</br></br>'
                                       '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;自动化接口测试结果，请查收附件阅读详细。谢谢！' +
                            '</br></br></br></br>' + '<div style = "float:right" >自动化测试组&nbsp;&nbsp;&nbsp;&nbsp;</ div >',
                            'HTML', 'utf-8'))
    # 上传个附件
    report = MIMEText(open(report_filen, 'rb').read(), 'base64', 'utf-8')
    report["Content-Type"] = 'application/octet-stream'
    report["Content-Disposition"] = 'attachment; filename="TestReport.html"'
    message.attach(report)
    print("附件1 上传成功！")

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")
