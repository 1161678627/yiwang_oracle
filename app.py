# -*- coding: utf-8 -*-
from ywqs import Ui_Form as Ui_MainWindow
from PySide2.QtWidgets import QApplication, QMessageBox, QMainWindow
import cx_Oracle as cx

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
        # 否则继续加钱
        else:
            # con = cx.connect('v8netman', '12345678', '192.168.0.222:1521/netman')
            # cursor = con.cursor()  # 创建游标
            # cursor.execute("select * from TDER where ID='28'")  # 执行sql语句
            # data = cursor.fetchone()  # 获取一条数据
            # print(data)  # 打印数据
            # cursor.close()  # 关闭游标
            # con.close()  # 关闭数据库连接
            pass

if __name__ == '__main__':
    account = 'p0111'
    money_list = ['20', '50', '100']
    app = QApplication([])
    activate = display()
    activate.show()
    app.exec_()
