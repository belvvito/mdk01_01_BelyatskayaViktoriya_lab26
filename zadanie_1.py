import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox

class KvadratAndKubChisla(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.prilozhenie()

    def prilozhenie(self):

        self.layout = QtWidgets.QVBoxLayout()

        self.resultLabel = QtWidgets.QTextEdit('')
        self.layout.addWidget(self.resultLabel)

        self.label = QtWidgets.QLabel('Введите значение для вычислений')
        self.layout.addWidget(self.label)

        self.inputField = QtWidgets.QLineEdit()
        self.layout.addWidget(self.inputField)

        self.kvadratButton = QtWidgets.QPushButton('Вычислить квадрат')
        self.kvadratButton.clicked.connect(self.vichislenie_kvadrata)

        self.kubButton = QtWidgets.QPushButton('Вычислить куб')
        self.kubButton.clicked.connect(self.vichislenie_kuba)

        self.layout.addWidget(self.kvadratButton)
        self.layout.addWidget(self.kubButton)

        self.setLayout(self.layout)

    def vichislenie_kvadrata(self):
        try:
            a = float(self.inputField.text())
            kvadrat = a ** 2
            self.resultLabel.setText(f'Квадрат: {kvadrat}')
        except ValueError:
            QMessageBox.warning(self, 'Некорректное значение.', 'Введите другое значение.')

    def vichislenie_kuba(self):
        try:
            a = float(self.inputField.text())
            kub = a ** 3
            self.resultLabel.setText(f'Куб: {kub}')
        except ValueError:
            QMessageBox.warning(self, 'Некорректное значение.', 'Введите другое значение.')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    calculator = KvadratAndKubChisla()
    calculator.resize(350, 500)
    calculator.show()
    sys.exit(app.exec())
