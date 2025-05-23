from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QComboBox
import sys

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Crear el layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Crear el QComboBox
        self.combobox = QComboBox()
        self.combobox.addItems(['Opción 1', 'Opción 2', 'Opción 3'])
        layout.addWidget(self.combobox)

        # Crear el QLineEdit
        self.lineedit = QLineEdit()
        layout.addWidget(self.lineedit)

        # Conectar la señal del QComboBox al slot
        self.combobox.currentTextChanged.connect(self.update_line_edit)

    def update_line_edit(self, text):
        # Actualizar el texto del QLineEdit
        self.lineedit.setText(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())
