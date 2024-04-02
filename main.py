import convert
import requests
import sys
import re
from PyQt5 import QtWidgets, uic

result = ''

with open("text.txt", encoding="utf-8") as file:
    for item in file:
        result += item

class ExampleApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('mywindow.ui', self)
        self.show() 

        self.pushButton.clicked.connect(self.start)
        self.pushButton_2.clicked.connect(self.search)
        self.textEdit.setReadOnly(True)

    def search(self):
        self.question = self.textEdit_2.toPlainText()
        self.textEdit.append(f"Вы: {self.question}")
        answer = requests.request_gpt(f"{result} /n Найди в этом тексте ответ на этот вопрос: {self.question}")
        answer = re.sub(r'\.[^./]+?$', '', answer)
        self.textEdit.append(f"Ответ: {answer}")
        self.textEdit_2.clear()  

    def start(self):
        self.question = convert.record_volume()
        self.textEdit.append(f"Вы: {self.question}")
        answer = requests.request_gpt(f"{result} /n Найди в этом тексте ответ на этот вопрос: {self.question}")
        answer = re.sub(r'\.[^./]+?$', '', answer)
        self.textEdit.append(f"Ответ: {answer}")    

def main():
    app = QtWidgets.QApplication(sys.argv) 
    window = ExampleApp()  
    app.exec_() 

if __name__ == '__main__': 
    main() 
