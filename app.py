# -*- coding: utf-8 -*-
from ywqs import Ui_Form as Ui_MainWindow
from PySide2.QtWidgets import QApplication, QMessageBox, QMainWindow
import cx_Oracle as cx
import base64 as bbbqqq

# 需要先查询当前剩余的余额，然后再对新增余额和剩余余额 进行相加更新
select_banlance_sql = "SELECT LastName FROM Persons WHERE LastName = 'Wilson'"
update_banlance_sql = "UPDATE Person SET FirstName = 'Fred' WHERE LastName = 'Wilson'"


class display(QMainWindow):
    def __init__(self):
        super(display, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.process_add)
        # 禁止拉伸窗口大小
        self.setFixedSize(self.width(), self.height())
        self.ui.textBrowser.setText(account)


    def process_add(self):
        add_money = self.ui.lineEdit.text()
        print(add_money)
        # 如果加钱金额不合法，则弹窗警告
        if add_money not in money_list:
            QMessageBox.about(self, '警告', '非法加钱输入！')
            self.ui.lineEdit.setText('')
        # 否则继续加钱
        else:
            add_money = int(add_money)
            # 连接数据库
            # con = cx.connect('v8netman', '12345678', '192.168.0.222:1521/netman')
            # cursor = con.cursor()  # 创建游标
            # 执行查询余额代码
            # cursor.execute("select * from TDER where ID='28'")  # 执行sql语句
            # data = cursor.fetchone()  # 获取一条数据
            # print(data)  # 打印数据
            # 执行余额和剩余金额相加
            # final_money = add_money + data
            # 执行余额更新
            # cursor.execute("select * from TDER where ID='28'")  # 执行sql语句
            # con.commit()
            # 收尾
            # cursor.close()  # 关闭游标
            # con.close()  # 关闭数据库连接
            QMessageBox.about(self, '提示', '操作成功！')
            exit()

if __name__ == '__main__':
    account = 'cDAxMTE' + '='
    account = bbbqqq.decodebytes(account.encode('utf-8')).decode()
    password = 'Y' + 'm' + 'FyNjA0NjE' + '='
    password = bbbqqq.decodebytes(password.encode('utf-8')).decode()
    money_list = ['50', '100', '200']
    app = QApplication([])
    activate = display()
    activate.show()
    app.exec_()