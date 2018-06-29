"""
@file: TestRunner.py
@copyright: laoZ
"""
import sys
import time
import unittest

from PublicPackage import HTMLTestRunnerCN, Email,Dingtalk

if __name__ == "__main__":

  # 自动化报告文字修改、# 饼状图字体修改、# 生产报告时间
  report_title = '自动化接口测试报告'
  desc = '右侧饼状图展示通过率、失败率、错误率'

  now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
  report_file_now = 'report/TestReport'+now+'.html'

  report_file = '/TestReport/TestReport.html'
  # 创建报告文件，打印报告数据

  '''with open(report_file_0, 'wb') as report:
    runner = HTMLTestRunnerCN.HTMLTestRunner(stream=report, title=report_title, description=desc)
    runner.run(discover1)'''

  with open(report_file, 'wb') as report:
      runner = HTMLTestRunnerCN.HTMLTestRunner(stream=report, title=report_title, description=desc)
      runner.run(discover)


  # 自动读取邮箱，发送邮件
  Email.email()

  # 钉钉群发消息
  Dingtalk.Send_Dingtalk()