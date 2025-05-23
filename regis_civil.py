import sys
from PyQt5.QtWidgets import QLabel, QLineEdit, QApplication, QMainWindow, QPushButton, QMessageBox
from PyQt5.QtCore import Qt, QTimer, QPointF
from PyQt5.QtGui import QPixmap, QTransform
from administrativo import documentos

class REGISTRO_CIVIL(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("REGISTRO_CIVIL ")
        self.setGeometry(250, 250, 300, 450)
        self.setStyleSheet("background-color: #daf7a6;")

        # ------------------ IMAGEN GIRATORIA ------------------
        self.angulo = 0  # ángulo inicial
        self.original_pixmap = QPixmap("contra.png")
        self.rotating_label = QLabel(self)
        self.rotating_label.setGeometry(118, 100, 100, 100)

        # Temporizador para girar
        self.timer = QTimer()
        self.timer.timeout.connect(self.rotar_imagen)
        self.timer.start(50)  # cada 50 milisegundos
        # ------------------------------------------------------

        self.logo1 = QLabel(self)
        self.logo1.setPixmap(QPixmap("usur.png").scaled(105, 105, Qt.KeepAspectRatio))
        self.logo1.setGeometry(90, 0, 105, 105)

        self.logo2 = QLabel(self)
        self.logo2.setPixmap(QPixmap("regcivil.png").scaled(230, 310, Qt.KeepAspectRatio))
        self.logo2.setGeometry(20, 240, 230, 310)

        self.nombre = QLabel("USUARIO", self)
        self.nombre.setStyleSheet("border-radius: 6px; border: 1px solid gray;")
        self.nombre.setGeometry(100, 80, 100, 30)  # Asegúrate de definir tamaño (ancho/alto)
        self.nombre.setAlignment(Qt.AlignCenter) 
        self.nombre.move(100, 70)
        

        # self.usuario = QLineEdit(self)
        self.usuario = QLineEdit("admin")
        self.usuario.setStyleSheet("background-color: yellow; border-radius: 6px; border: 1px solid gray;")
        self.usuario.move(100, 100)

        self.codigo = QLabel("CONTRASEÑA", self)
        self.codigo.setStyleSheet("border-radius: 6px; border: 1px solid gray;")
        self.codigo.setGeometry(100, 180, 100, 30)  # (x, y, ancho, alto)
        self.codigo.setAlignment(Qt.AlignCenter)

        # self.contrasena = QLineEdit(self)
        self.contrasena = QLineEdit("admin")
        self.contrasena.setEchoMode(QLineEdit.Password)
        self.contrasena.setStyleSheet("background-color: yellow; border-radius: 6px; border: 1px solid gray;")
        self.contrasena.move(100, 210)

        self.btningresar = QPushButton("INGRESAR", self)
        self.btningresar.setStyleSheet("background-color: #007BFF; color: white; border-radius: 6px;")
        self.btningresar.setCursor(Qt.PointingHandCursor)
        self.btningresar.move(100, 270)
        self.btningresar.clicked.connect(self.iniciarsesion)

    def rotar_imagen(self):
        self.angulo = (self.angulo + 5) % 360
        center = QPointF(self.original_pixmap.width() / 2, self.original_pixmap.height() / 2)
        transform = QTransform().translate(center.x(), center.y()).rotate(self.angulo).translate(-center.x(), -center.y())
        rotated_pixmap = self.original_pixmap.transformed(transform, Qt.SmoothTransformation)
        self.rotating_label.setPixmap(rotated_pixmap.scaled(50, 50, Qt.KeepAspectRatio))

    def iniciarsesion(self):
        usuario_value = "admin"
        password_value = "admin"
        usuario = self.usuario.text().lower()
        contrasena = self.contrasena.text()
        if usuario != usuario_value:
            QMessageBox.critical(self, 'Error', 'DOÑA PILI SE FUMO LA MALA El usuario es incorrecto')
        elif contrasena != password_value:
            QMessageBox.critical(self, 'Error', 'DOÑA PILI ESTA HUASCA La contraseña es incorrecta')
        else:
            self.close()
            ventana = documentos(self)
            ventana.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = REGISTRO_CIVIL()
    ventana.show()
    sys.exit(app.exec_())
