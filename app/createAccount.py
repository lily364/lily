# coding:utf-8
from pywinauto import application
import subprocess
import os
os.environ.update({"__COMPAT_LAYER": "RUnAsInvoker"})
a = 'D:\\业务\\HsClient\\HSRCP.exe'
app = application.Application(backend='uia').start(a)
hs_win = app.window(title='客户账户集中管理系统V2.0')

