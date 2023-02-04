# import the libs for the project
from PyQt5 import uic, QtWidgets
import mysql.connector

#connect the mysql database
banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="cadastro_pessoa",
)

#qt designer imports
app=QtWidgets.QApplication([])
formulario=uic.loadUi(".ui import here")
segunda_tela=uic.loadUi(".ui import here")
formulario.pushButton.clicked.connect("def here")
formulario.pushButton_2.clicked.connect("def here")
formulario.show()
app.exec()