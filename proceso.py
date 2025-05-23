# proceso.py
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit,QComboBox,QDateEdit,QVBoxLayout
from PyQt5.QtCore import QDate
from PyQt5.QtCore import Qt

class tramite(QMainWindow):
    def __init__(self, texto_seleccionado,codigo,monto, parent=None):
        super(tramite, self).__init__(parent)

        self.setWindowTitle("Carga de la Orden")
        self.setGeometry(250, 250, 750, 450)
        self.setStyleSheet("background-color: #F0E68C;")

        # Label principal
        self.label = QLabel("REGISTRO ORDEN DE TRÁMITE", self)
        self.label.setGeometry(50, 10, 550, 40)
        self.label.setStyleSheet("color: blue; font-family: 'Times New Roman'; font-size: 25px;")
        self.label.setAlignment(Qt.AlignCenter)

        # Label explicativo
        self.label1 = QLabel("Trámite Corresponde a Partida De:", self)
        self.label1.setStyleSheet("color: Arial black; font-family: 'Times New Roman'; font-size: 15px;")
        self.label1.setGeometry(10, 50, 300, 40)
        
        self.label2=QLabel("Orden de pago de Registro Civil",self)
        self.label2.setGeometry(380,50,220,40)
        self.label2.setStyleSheet("color: black; font-family: 'Times New Roman'; font-size: 15px;")

        self.label3=QLabel("Numero de Procedimiento",self)
        self.label3.setGeometry(10,80,160,40)
        self.label3.setStyleSheet("color: black; font-family: 'Times New Roman'; font-size: 15px;")

        self.label4=QLabel("Monto de Pago",self)
        self.label4.setGeometry(10,110,100,40)
        self.label4.setStyleSheet("color: black; font-family: 'Times New Roman'; font-size: 15px;")

        self.label5=QLabel("Fecha de Registro",self)
        self.label5.setGeometry(10,140,110,40)
        self.label5.setStyleSheet("color: black; font-family: 'Times New Roman'; font-size: 15px;")

        self.label6=QLabel("Añadir otro Pto",self)
        self.label6.setGeometry(475,80,110,40)
        self.label6.setStyleSheet("color: black; font-family: 'Times New Roman'; font-size: 15px;")

    
        # Solo el QLineEdit, sin QComboBox
        self.line_edit = QLineEdit(self)
        self.line_edit.setGeometry(230, 50, 110, 30)
        self.line_edit.setReadOnly(True)
        self.line_edit.setAlignment(Qt.AlignCenter)
        self.line_edit.setStyleSheet("""
            font-size: 15px;
            color: blue;
            background-color: #FFFFE0;
        """)
        self.line_edit.setText(texto_seleccionado)


        self.line1=QLineEdit(self)
        self.line1.setGeometry(230,85,235,30)
        self.line1.setReadOnly(True)  
        self.line1.setStyleSheet("""
            font-size: 12px;
            color: blue;
            background-color: #FFFFE0;
        """)
        self.line1.setText(str(codigo))
    
        self.line2=QLineEdit(self)
        self.line2.setGeometry(600,50,100,30)
        self.line2.setStyleSheet("""
            font-size: 12px;
            color: blue;
            background-color: #FFFFE0;
        """)
        self.line2.setFocus()
        
        self.line3=QLineEdit(self)
        self.line3.setGeometry(230,115,100,30)
        self.line3.setReadOnly(True)
        self.line3.setStyleSheet("""
            font-size: 12px;
            color: blue;
            background-color: #FFFFE0;
        """)
        self.line3.setText(str(monto))


        self.date_edit = QDateEdit(self)
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setDate(QDate.currentDate())
        self.date_edit.setGeometry(230, 145, 110, 30)


        self.combo=QComboBox(self)
        self.combo.setGeometry(600,85,100,30)
        self.combo.setStyleSheet("""
            font-size: 12px;
            color: blue;
            background-color: #FFFFE0;
        """)

