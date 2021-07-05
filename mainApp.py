import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QFileDialog, QWidget)
import shutil
import os
import integrationMethods#, gui_demo
import json
global count
count = 0
class HomeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Counting Tiger Population Using Computer Vision"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.pushButton1 = QPushButton("View", self)
        self.pushButton1.move(275, 200)
        self.pushButton1.setToolTip("<h3>Click To View Tiger Database</h3>")
        # self.pushButton.clicked.connect(self.window2)
        self.pushButton2 = QPushButton("Count", self)
        self.pushButton2.move(275, 300)
        self.pushButton2.setToolTip("<h3>Click To Count Tigers</h3>")
        self.pushButton2.clicked.connect(self.window2)
        self.main_window()
    def main_window(self):
        self.label = QLabel("View Tiger Data", self)
        self.label.move(285, 175)
        self.label = QLabel("Count Tigers", self)
        self.label.move(285, 275)
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()
    def window2(self):
        self.w = CountWindow()
        self.w.show()
        self.hide()
class CountWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Welcome To Tiger Counting"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.selectButton = QPushButton("Select", self)
        self.selectButton.move(275, 200)
        self.selectButton.setToolTip("<h3>Select json file</h3>")
        
        self.selectButton.clicked.connect(self.selectFile)
        self.pushButton2 = QPushButton("Run", self)
        self.pushButton2.move(275, 300)
        self.pushButton2.setToolTip("<h3>Run Tiger Counting</h3>")
        self.pushButton2.clicked.connect(self.window3)
        self.pushButton3 = QPushButton("Back", self)
        self.pushButton3.move(50, 430)
        self.pushButton3.setToolTip("<h3>Back</h3>")
        self.pushButton3.clicked.connect(self.Window)
        self.main_window()
    def main_window(self):
        self.label = QLabel("Select File", self)
        self.label.move(285, 175)
        self.label = QLabel("Run Counting", self)
        self.label.move(285, 275)
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()
    def window3(self):
        self.w = RunWindow()
        self.w.show()
        self.hide()
    def Window(self):
        self.w = HomeWindow()
        self.w.show()
        self.hide()
        
    def selectFile(self):
        # intMethods = integrationMethods.Selector()
        # source_dir = intMethods.pick_new()
        # print(source_dir)
        # target_dir = "C:/Users/Gaurav/Dev/Tiger-Reidentification/src/data/AmurTiger/reid_test"
        # file_names = os.listdir(source_dir)
        # for file_name in file_names:
        #     shutil.copy(os.path.join(source_dir, file_name), target_dir)
        # os.system('python demo.py')
        self.open_dialog_box()
        
    def open_dialog_box(self):
        global count
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        print(path)
        with open(path) as json_file: 
            data = json.load(json_file)
        #print(data)
        # print("Type:", type(data))
        # print(type(data) is list)
        list_of_result=[]
        for datas in data:
            for values in datas.values():
                if type(values) is list:
                    list_of_result.append(values[0])
        # print(list_of_result)
        print (len(list_of_result))
        l1 = [] 
          
        # taking an counter 
        count = 0
          
        # travesing the array 
        for item in list_of_result: 
            if item not in l1: 
                count += 1
                l1.append(item) 
        print(count)  
        
class RunWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        global count
        self.resize(680, 500)
        self.move(100, 100)
        self.setWindowTitle("Counting Tigers .....")
        print(count)
        self.label = QLabel(str(count)+"TigersFound", self)
        self.label.move(285, 175)
        self.pushButton1 = QPushButton("Update", self)
        self.pushButton1.move(275, 300)
        self.pushButton1.setToolTip("<h3>Update To Database</h3>")
        self.pushButton2 = QPushButton("Back", self)
        self.pushButton2.move(50, 430)
        self.pushButton2.setToolTip("<h3>Back</h3>")
        self.pushButton2.clicked.connect(self.window2)
        self.main_window()
    def main_window(self):
        self.show()
    def window2(self):
        self.w = CountWindow()
        self.w.show()
        self.hide()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HomeWindow()
    window.show() #?
    sys.exit(app.exec())