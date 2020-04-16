from PyQt5 import QtCore, QtGui, QtWidgets
from Admin import Ui_Admin
from Faculty import Ui_Faculty
class Ui_Main(object):
    def adminlogin(self, event):
        try:
            self.admn = QtWidgets.QDialog()
            self.ui = Ui_Admin(self.admn)
            self.ui.setupUi(self.admn)
            self.admn.show()
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
        event.accept()

    def facultylogin(self, event):
        try:
            self.faclty = QtWidgets.QDialog()
            self.ui = Ui_Faculty(self.faclty)
            self.ui.setupUi(self.faclty)
            self.faclty.show()
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
        event.accept()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(778, 565)
        Dialog.setStyleSheet("background-color: rgb(167, 55, 0);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 20, 771, 81))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 20pt \"Vani\";")
        self.label.setObjectName("label")
        self.faculty = QtWidgets.QLabel(Dialog)
        self.faculty.setGeometry(QtCore.QRect(250, 330, 231, 141))
        self.faculty.setStyleSheet("image: url(../AttendanceSystem/images/facultyy.png);")
        self.faculty.setText("")
        self.faculty.setObjectName("faculty")
        self.faculty.mousePressEvent = self.facultylogin
        self.admin = QtWidgets.QLabel(Dialog)
        self.admin.setGeometry(QtCore.QRect(240, 100, 271, 151))
        self.admin.setStyleSheet("image: url(../AttendanceSystem/images/adminn.png);")
        self.admin.setText("")
        self.admin.setObjectName("admin")
        self.admin.mousePressEvent = self.adminlogin
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(340, 240, 131, 61))
        self.label_2.setStyleSheet("font: 16pt \"Vani\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(330, 460, 131, 61))
        self.label_3.setStyleSheet("font: 16pt \"Vani\";\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Main"))
        self.label.setText(_translate("Dialog", "      Classroom Attendance System based on Face Recognition"))
        self.label_2.setText(_translate("Dialog", "Admin"))
        self.label_3.setText(_translate("Dialog", "Faculty"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Main()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
