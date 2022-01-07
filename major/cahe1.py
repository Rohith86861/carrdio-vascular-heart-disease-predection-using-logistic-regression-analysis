import sys
import os
from cahe import *
from PyQt5 import QtWidgets, QtGui, QtCore

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.casympts)
     self.ui.pushButton_2.clicked.connect(self.ptstrslts)
     self.ui.pushButton_3.clicked.connect(self.hesympts)
     self.ui.pushButton_4.clicked.connect(self.predict)
     self.ui.pushButton_5.clicked.connect(self.pdetails)


        

  def casympts(self):
    os.system("python casymptoms1.py")

  def pdetails(self):
    os.system("python patientdtls1.py")

  def ptstrslts(self):
    os.system("python ptests1.py")

  def hesympts(self):
    os.system("python hesymptoms1.py")    
    
  def predict(self):
    os.system("python clsfier.py")
    

#  def roboidn(self):
#	os.system("python roboidfn1.py")

#  def gnrep(self):
#	os.system("python genrep1.py")
       
          
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
