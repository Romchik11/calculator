from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QAction


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(293, 287)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 251, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.label_2 = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 200, 251, 61))
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Пов'язуємо кнопку з обробником події
        self.pushButton.clicked.connect(self.calculate_cost)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Калькулятор комуналки"))
        self.comboBox.setItemText(0, _translate("Form", "Газ"))
        self.comboBox.setItemText(1, _translate("Form", "Світло"))
        self.comboBox.setItemText(2, _translate("Form", "Вода"))
        self.label_2.setText(_translate("Form", "Введіть ціну"))
        self.label.setText(_translate("Form", "Введіть кількість"))
        self.pushButton.setText(_translate("Form", "Розрахувати вартість"))
        self.label_3.setText(_translate("Form", "Твоя ціна"))

    def calculate_cost(self):
        try:
            price = float(self.label_2.toPlainText())
            quantity = float(self.label.toPlainText())


            service = self.comboBox.currentText()


            if service == "Газ":
                total_cost = price * quantity
            elif service == "Світло":
                total_cost = price * quantity
            elif service == "Вода":
                total_cost = price * quantity
            else:
                total_cost = 0

            self.label_3.setText(f"Твоя ціна: {total_cost} грн")
        except ValueError:
            self.label_3.setText("Невірний формат ціни або кількості")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
