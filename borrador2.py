from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QDateEdit
from PyQt5.QtCore import QDate
import sys

app = QApplication(sys.argv)
window = QWidget()
layout = QVBoxLayout()

date_edit = QDateEdit()
date_edit.setCalendarPopup(True)
date_edit.setDate(QDate.currentDate())
layout.addWidget(date_edit)

window.setLayout(layout)
window.setWindowTitle("Selector de Fecha")
window.show()
sys.exit(app.exec_())

