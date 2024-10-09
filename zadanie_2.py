import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit

class TablicaUmnozheniya(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(500, 500, 500, 500)

        self.layout = QVBoxLayout()

        self.label = QLabel('Введите значение для вычислений')
        self.layout.addWidget(self.label)

        self.input_field = QLineEdit()
        self.layout.addWidget(self.input_field)

        self.calculate_button = QPushButton("Таблица")
        self.calculate_button.clicked.connect(self.sozdanie_tablici)
        self.layout.addWidget(self.calculate_button)

        self.result_area = QTextEdit()
        self.result_area.setReadOnly(True)
        self.layout.addWidget(self.result_area)

        self.setLayout(self.layout)

    def sozdanie_tablici(self):
        try:
            a = int(self.input_field.text())
            table = '\n'.join([f'{a} x {i} = {a * i}' for i in range(1, 11)])
            self.result_area.setPlainText(table)
        except ValueError:
            self.result_area.setPlainText("Пожалуйста, введите корректное число.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TablicaUmnozheniya()
    window.show()
    sys.exit(app.exec())
