import sys
from PyQt5.QtWidgets import  QPushButton, QLabel, QMainWindow, QComboBox, QListWidget, QLineEdit, QMessageBox
from PyQt5.QtCore import Qt
from proceso import tramite

class documentos(QMainWindow):
    def __init__(self, parent=None):
        super(documentos, self).__init__(parent)

        self.setWindowTitle("Datos del Administrado")
        self.setGeometry(250, 250, 650, 400)
        self.setStyleSheet("background-color: #F0E68C;")

        self.cambio()  # ← llamada corregida
        

        self.label = QLabel("TIPO DE DOCUMENTO A REGISTRAR", self)
        self.label.setGeometry(50, 20, 550, 40)
        self.label.setStyleSheet("color: blue; font-family: 'Times New Roman'; font-size: 25px;")
        self.label.setAlignment(Qt.AlignCenter)

        self.label1 = QLabel("I.Cod. de la lista", self)
        self.label1.setStyleSheet("color: blue; font-family: 'Times New Roman'; font-size: 12px;")
        self.label1.move(210, 90)

        self.line1 = QLineEdit("", self)
        self.line1.setGeometry(200, 60, 100, 30)
        self.line1.setStyleSheet("""
            color: blue;
            font-family: 'Arial';  
            font-size: 15px;
            background-color: #FFFFE0;
        """)
        self.line1.setAlignment(Qt.AlignCenter)
        self.line1.editingFinished.connect(self.ingresar)


        self.line2 = QLineEdit("", self)
        self.line2.setGeometry(30, 180, 100, 80)
        self.line2.setStyleSheet("""
            color: blue;
            font-family: 'Arial';  
            font-size: 25px;
            background-color: #FFFFE0;
        """)
        self.line2.setAlignment(Qt.AlignCenter)

        self.btnconsulta = QPushButton("Cargar Datos", self)
        self.btnconsulta.move(360, 320)
        self.btnconsulta.resize(130,30)
        self.btnconsulta.clicked.connect(self.cargar_tabla)
        self.btnconsulta.setStyleSheet("background-color: yellow; color: black; font-size: 15px; font-family: 'ALGERIAN';")

    def cambio(self): 
        #self.ingresar()
        #self.line1 = QLineEdit() # ← ahora correctamente dentro de la clase
        self.combo = QComboBox(self)
        self.combo.setGeometry(30, 60, 150, 30)
        self.combo.addItems([" (seleccionar)", "Nacimiento", "Matrimonio", "Defuncion"])
        self.combo.currentIndexChanged.connect(self.mostrar_lista)

        # Lista de nacimiento
        self.naci = QListWidget(self)
        self.naci.setGeometry(310, 60, 300, 230)
        self.naci.addItems([
            "109 Inscripción de nacimiento ordinario", "110 Inscripción de nacimiento extraordinario", "111 Inscripción de nacimiento judicial",
            "112 Inscripcion de nacimiento de menores de edad hijos de peruanos y nacidos en el extranjero(inscripcion ordinaria o extenporanea)",
            "113 Reconocimiento directo, de escritura publica o por testamento",
            "115 Inscripcion de adopcion judicial notarial o administrativo(MIMP)",
            "116 Inscripcion de impugnacion de paternidad","132 Copia certificada de documentos archivados",
            "133 Constancia positiva o negativa de inscripcion de nacimiento, matrimonio o defuncion",
            "134 Copia certificada de partida o actas de nacimiento, matrimonio y defuncion",
            "135 Copia certificada de partida o actas de nacimiento,matrimonio y defuncion para el extranjero",
            "136 Rectificacion de acta o partida de nacimiento, matrimonio o defuncion por mandato judicial o notarial",
            "137 Cambio, adicion o supresion de nombre por mandato judicial","138 Rectificacion administrativa de acta o partida por error u omisionno atribuible al registrador",
            "139 Rectificacion administrativa de acta o partida por error u omision atribuible al registrador",
            "140 Reposicion de actas de nacimiento, matrimonio o defuncion con participacion del ciudadano",
            "141 Reconstruccion de acta o partida de nacimiento, matrimonio o defuncion"])
        self.naci.setStyleSheet("""
            color: blue;
            font-family: 'Arial';  
            font-size: 12px;
            background-color: #FFFFE0;
        """)

        # Lista de matrimonio
        self.matri = QListWidget(self)
        self.matri.setGeometry(310, 60, 300, 230)
        self.matri.addItems([
            "114 filiacion extramatrimonial","117 M.Civil(matrimonio ordinario 7 am-3pm)","117-1 M.C(matrimonio extraordinario fuera local municipal)",
            "117-2 M.C (matrimonio ordinario 5pm-8pm)","117-3 M.C (matrimonio extraordinario 5pm-8pm)", "118 Constancia de tramite de matrimonio"
            "119 Retiro  de expediente matrimonio","120 Postergacion de matrimonio",
            "121 Dispersa de publicacion de edicto matrimonial(dentro de local municipal)",
            "122 Publicacion de edicto matrimonial de otras municipalidades","123 Inscripcion de matrimonio",
            "124 Inscripcion de divoricio nulidad o invalidez de matrimonio via administrativa",
            "125 Inscripcion de divorcio notarial","126 certificado de solteria","132 Copia certificada de documentos archivados",
            "133 Constancia positiva o negativa de inscripcion de nacimiento, matrimonio o defuncion",
            "134 Copia certificada de partida o actas de nacimiento, matrimonio y defuncion",
            "135 Copia certificada de partida o actas de nacimiento, matrimonio y defuncion para el extranjero",
            "136 Rectificacion de acta o partida de nacimiento, matrimonio o defuncion por mandato judicial o notarial",
            "138 Rectificacion administrativa de acta o partida por error u omision no atribuible al registrador",
            "139 Rectificacion administrativa de acta o partida por error u omision atribuible al registrador",
            "140 Reposicion de actas de nacimiento, matrimonio o defuncion con participacion del ciudadano",
            "141 Reconstitucion de acta o partida de nacimiento, matrimonio o defuncion" ])
        self.matri.setStyleSheet("""
            color: green;
            font-family: 'Arial';  
            font-size: 12px;
            background-color: #FFFFE0;
        """)

        # Lista de defunción
        self.defun = QListWidget(self)
        self.defun.setGeometry(310, 60, 300, 230)
        self.defun.addItems([
            "127 Inscripción de defunción", "128 Inscripción de oficio por muerte violenta","129 Inscripcion de oficio, supletoria",
            "130 Inscripcion por declaracion judicial por muerte presunta, o ausencia por desaparicion forzada",
            "131 Cerificado de viudez","132 Copia certificada de documentos archivados",
            "133 Constancia positiva o negativa de inscripcion de nacimiento, matrimonio o defuncion",
            "134 Copia certificada de partida o actas de nacimiento, matrimonio y defuncion",
            "135 Copia certificada de partida o actas de nacimiento,matrimonio y defuncion para el extranjero",
            "136 Rectificacion de acta  o partida de nacimiento, matrimonio o defuncion por mandato judicial o notaria",
            "137 Cambio, adicion o supresion de nombre por mandato judicial",
            "138 Rectificacion administrativa de acta o partida por error u omisionno atribuible al registrador",
            "139 Rectificacion administrativa de acta o partida por error u omision atribuible al registrador",
            "140 Reposicion de actas de nacimiento, matrimonio o defuncion con participacion del ciudadano",
            "141 Reconstitucion de acta o partida de nacimiento, matrimonio o defuncion"])
        self.defun.setStyleSheet("""
            color: purple;
            font-family: 'Arial';  
            font-size: 12px;
            background-color: #FFFFE0;
        """)

        # Ocultar todas por defecto
        self.naci.hide()
        self.matri.hide()
        self.defun.hide()

    def mostrar_lista(self, index):
        self.naci.hide()
        self.matri.hide()
        self.defun.hide()

        if index == 1:
            self.naci.show()
        elif index == 2:
            self.matri.show()
        elif index == 3:
            self.defun.show()
    def ingresar(self):
        try:
            codigo = int(self.line1.text())  # ← obtener y convertir a entero
            if codigo == 109 and self.combo.currentIndex() == 1:
              self.line2.setText("gratuito")  # ← esta línea estaba mal: usaste '==' en vez de '='
             # ← obtener y convertir a entero
            elif codigo == 110 and self.combo.currentIndex() == 1:
              self.line2.setText("22")
            elif codigo == 111 and self.combo.currentIndex() == 1:
              self.line2.setText("34")
            elif codigo == 112 and self.combo.currentIndex() == 1:
              self.line2.setText("46")
            elif codigo == 113 and self.combo.currentIndex() == 1:
              self.line2.setText("54")
            elif codigo == 115 and self.combo.currentIndex() == 1:
              self.line2.setText("34")
            elif codigo == 116 and self.combo.currentIndex() == 1:
              self.line2.setText("54")
            elif codigo == 132 and self.combo.currentIndex() == 1:
              self.line2.setText("11")
            elif codigo == 133 and self.combo.currentIndex() == 1:
              self.line2.setText("20") 
            elif codigo == 134 and self.combo.currentIndex() == 1:
              self.line2.setText("15") 
            elif codigo == 135 and self.combo.currentIndex() == 1:
              self.line2.setText("30")  
            elif codigo == 136 and self.combo.currentIndex() == 1:
              self.line2.setText("50")  
            elif codigo == 137 and self.combo.currentIndex() == 1:
              self.line2.setText("50") 
            elif codigo == 138 and self.combo.currentIndex() == 1:
              self.line2.setText("50") 
            elif codigo == 139 and self.combo.currentIndex() == 1:
              self.line2.setText("gratuito") 
            elif codigo == 140 and self.combo.currentIndex() == 1:
              self.line2.setText("gratuito")
            elif codigo == 141 and self.combo.currentIndex() == 1:
              self.line2.setText("gratuito")
            elif codigo == 114 and self.combo.currentIndex() == 2:
              self.line2.setText("34")  
            elif codigo == 117 and self.combo.currentIndex() == 2:
              self.line2.setText("136") 
            elif codigo == 117-1 and self.combo.currentIndex() == 2:
              self.line2.setText("156")
            elif codigo == 117-2 and self.combo.currentIndex() == 2:
              self.line2.setText("166")
            elif codigo == 117-3 and self.combo.currentIndex() == 2:
              self.line2.setText("226")         
            elif codigo == 118 and self.combo.currentIndex() == 2:
              self.line2.setText("46") 
            elif codigo == 119 and self.combo.currentIndex() == 2:
              self.line2.setText("46") 
            elif codigo == 120 and self.combo.currentIndex() == 2:
              self.line2.setText("46")
            elif codigo == 121 and self.combo.currentIndex() == 2:
              self.line2.setText("46")
            elif codigo == 122 and self.combo.currentIndex() == 2:
              self.line2.setText("50")
            elif codigo == 123 and self.combo.currentIndex() == 2:
              self.line2.setText("34")
            elif codigo == 124 and self.combo.currentIndex() == 2:
              self.line2.setText("34")
            elif codigo == 125 and self.combo.currentIndex() == 2:
              self.line2.setText("34")
            elif codigo == 126 and self.combo.currentIndex() == 2:
              self.line2.setText("34")
            elif codigo == 132 and self.combo.currentIndex() == 2:
              self.line2.setText("11")
            elif codigo == 133 and self.combo.currentIndex() == 2:
              self.line2.setText("20")
            elif codigo == 134 and self.combo.currentIndex() == 2:
              self.line2.setText("15")
            elif codigo == 135 and self.combo.currentIndex() == 2:
              self.line2.setText("30") 
            elif codigo == 136 and self.combo.currentIndex() == 2:
              self.line2.setText("50")
            elif codigo == 138 and self.combo.currentIndex() == 2:
              self.line2.setText("50")
            elif codigo == 139 and self.combo.currentIndex() == 2:
              self.line2.setText("gratuito")
            elif codigo == 140 and self.combo.currentIndex() == 2:
              self.line2.setText("gratuito")
            elif codigo == 141 and self.combo.currentIndex() == 2:
              self.line2.setText("gratuito")                                                 
            elif codigo == 127 and self.combo.currentIndex() == 3:
              self.line2.setText("12.5")
            elif codigo == 128 and self.combo.currentIndex() == 3:
              self.line2.setText("23")
            elif codigo == 129 and self.combo.currentIndex() == 3:
              self.line2.setText("34")
            elif codigo == 130 and self.combo.currentIndex() == 3:
              self.line2.setText("34")
            elif codigo == 131 and self.combo.currentIndex() == 3:
              self.line2.setText("34")
            elif codigo == 132 and self.combo.currentIndex() == 3:
              self.line2.setText("11")
            elif codigo == 133 and self.combo.currentIndex() == 3:
              self.line2.setText("20")
            elif codigo == 134 and self.combo.currentIndex() == 3:
              self.line2.setText("15")
            elif codigo == 135 and self.combo.currentIndex() == 3:
              self.line2.setText("30")
            elif codigo == 136 and self.combo.currentIndex() == 3:
              self.line2.setText("50")
            elif codigo == 138 and self.combo.currentIndex() == 3:
              self.line2.setText("50")
            elif codigo == 139 and self.combo.currentIndex() == 3:
              self.line2.setText("gratuito")
            elif codigo == 140 and self.combo.currentIndex() == 3:
              self.line2.setText("gratuito")
            elif codigo == 141 and self.combo.currentIndex() == 3:
              self.line2.setText("gratuito")                                                                      
            else:
             QMessageBox.critical(self, 'Error', 'Doña Pili, mucho chuchuwasi, no perteneces a la lista')  
        except ValueError:
            QMessageBox.warning(self, 'Error', 'Por favor, ingresa un número válido en el campo de código.')

    def cargar_tabla(self):
      texto_seleccionado = self.combo.currentText()
      try: 
          codigo_seleccionado = int(self.line1.text())
          monto_seleccionado = self.line2.text()

          if texto_seleccionado != " (seleccionar)" and monto_seleccionado != "":
             self.ventana_tram = tramite(texto_seleccionado, codigo_seleccionado, monto_seleccionado)
             self.ventana_tram.show()
          else:
            QMessageBox.warning(self, 'Advertencia', 'Complete todos los campos antes de continuar.')

      except ValueError:
            QMessageBox.warning(self, 'Error', 'Código inválido o faltan datos.')
         

#def proceso(self):
 #       self.line1 == int
  #      if self.line1 != int:
   #        QMessageBox.critical(self, 'Error', 'Doña pili mucho chuchuwasi solo se puede ingresar numero')

    #    else:
     #       self.close()
            #ventana = platillos(self)
            #ventana.show()    
        


  