from PyQt5 import QtCore, QtGui, QtWidgets
from AddStudent import Ui_AddStudent
from ViewStudents import  Ui_ViewStudents
from Reports import Ui_Reports
class Ui_AdminHome(object):

    def __init__(self, Dialog,unm):
        self.dialog = Dialog
        self.unm = unm

    def addstdnts(self, event):
        try:
            self.adstdnt = QtWidgets.QDialog()
            self.ui1 = Ui_AddStudent()
            self.ui1.setupUi(self.adstdnt)
            self.adstdnt.show()
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
        event.accept()

    def viewstdents(self, event):
        try:
            self.viewstdnt = QtWidgets.QDialog()
            self.ui1 = Ui_ViewStudents()
            self.ui1.setupUi(self.viewstdnt)
            self.ui1.studentdetails()
            self.viewstdnt.show()

        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
        event.accept()

    def reports(self, event):
        try:
            self.reprts = QtWidgets.QDialog()
            self.ui1 = Ui_Reports(self.reprts, self.unm)
            self.ui1.setupUi(self.reprts)
            self.reprts.show()
            event.accept()

        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(740, 560)
        Dialog.setStyleSheet("background-color: rgb(155, 200, 70);")
        self.addstdnt = QtWidgets.QLabel(Dialog)
        self.addstdnt.setGeometry(QtCore.QRect(10, 200, 221, 201))
        self.addstdnt.setStyleSheet("image: url(../AttendanceSystem/images/addstudent.png);")
        self.addstdnt.setText("")
        self.addstdnt.setObjectName("addstdnt")
        self.addstdnt.mousePressEvent = self.addstdnts
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(300, 220, 211, 181))
        self.label_2.setStyleSheet("image: url(../AttendanceSystem/images/students.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_2.mousePressEvent = self.viewstdents
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 410, 181, 31))
        self.label.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Vani\";")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(340, 410, 181, 31))
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Vani\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(530, 210, 201, 211))
        self.label_4.setStyleSheet("image: url(../AttendanceSystem/images/attendance.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_4.mousePressEvent = self.reports
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(610, 400, 181, 51))
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Vani\";")
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(90, 40, 661, 91))
        self.label_6.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 16pt \"Franklin Gothic Heavy\";")
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "AdminHome"))
        self.label.setText(_translate("Dialog", "Add Students"))
        self.label_3.setText(_translate("Dialog", "View Students"))
        self.label_5.setText(_translate("Dialog", "Reports"))
        self.label_6.setText(_translate("Dialog", "Classroom Attendance System based on Face Recognition"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
