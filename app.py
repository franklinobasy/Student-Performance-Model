import pickle
import sys
import numpy as np
import pandas as pd


from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QComboBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class PerformanceApp(QWidget):
    def __init__(self, parent= None):
        super().__init__(parent)

        self.setFixedSize(300, 500)
        self.setWindowTitle("Test App")
        self.setupUI()

    def setupUI(self):
        gender = ['male', 'female']
        ethnicity = ['group A', 'group B', 'group C', 'group D', 'group E']
        loe = ["associate's degree", "bachelor's degree", "high school", "master's degree", "some college", "some high school"]
        lunch = ["free/reduces", "standard"]
        test_prep_course = ["completed", "none"]

        g_label = QLabel("Gender: ")
        self.g_list = QComboBox()
        self.g_list.addItems(gender)
        g_box = QHBoxLayout()
        g_box.addWidget(g_label, alignment=Qt.AlignLeft)
        g_box.addWidget(self.g_list)

        eth_label = QLabel("Ethnicity: ")
        self.eth_list = QComboBox()
        self.eth_list.addItems(ethnicity)
        eth_box = QHBoxLayout()
        eth_box.addWidget(eth_label, alignment=Qt.AlignLeft)
        eth_box.addWidget(self.eth_list)

        loe_label = QLabel("Level of Parent's Education: ")
        self.loe_list = QComboBox()
        self.loe_list.addItems(loe)
        loe_box = QHBoxLayout()
        loe_box.addWidget(loe_label, alignment=Qt.AlignLeft)
        loe_box.addWidget(self.loe_list)

        lunch_label = QLabel("Lunch: ")
        self.lunch_list = QComboBox()
        self.lunch_list.addItems(lunch)
        lunch_box = QHBoxLayout()
        lunch_box.addWidget(lunch_label, alignment=Qt.AlignLeft)
        lunch_box.addWidget(self.lunch_list)

        test_label = QLabel("Test Preparation Course: ")
        self.test_list = QComboBox()
        self.test_list.addItems(test_prep_course)
        test_box = QHBoxLayout()
        test_box.addWidget(test_label, alignment=Qt.AlignLeft)
        test_box.addWidget(self.test_list)

        check = QPushButton("Analyze")
        check.clicked.connect(self.process)

        self.Performance = QLabel()
        self.Performance.setMinimumSize(100, 30)
        self.Performance.setFrameStyle(2)
        self.Performance.setFont(QFont("Tahoma", 18, 3))
        self.Performance

        layout = QVBoxLayout()
        layout.addSpacing(70)
        layout.addLayout(g_box, Qt.AlignLeft)
        layout.addSpacing(20)
        layout.addLayout(eth_box, Qt.AlignLeft)
        layout.addSpacing(20)
        layout.addLayout(loe_box, Qt.AlignLeft)
        layout.addSpacing(20)
        layout.addLayout(lunch_box, Qt.AlignLeft)
        layout.addSpacing(20)
        layout.addLayout(test_box, Qt.AlignLeft)
        layout.addSpacing(20)
        layout.addWidget(check)
        layout.addSpacing(40)
        layout.addWidget(self.Performance, alignment= Qt.AlignCenter)

        self.setLayout(layout)
    
    def analyze(self):

        input_ = [0,  # female             0
                  0,  # male               1
                  0,  # group A            2
                  0,  # group B            3
                  0,  # group C            4
                  0,  # group D            5
                  0,  # group E            6
                  0,  # associate's degree 7
                  0,  # bachelor's degree  8
                  0,  # high school        9
                  0,  # some college       10
                  0,  # some high school   11
                  0,  # free/reduced       12
                  0,  # standard           13
                  0,  # completed          14
                  0   # none               15
                  ]
        if self.g_list.currentText() == 'female':
             input_[0] = 1
        else:
              input_[1] = 1
        
        if self.eth_list.currentText() == 'group A':
            input_[2] = 1
        elif self.eth_list.currentText() == 'group B':
            input_[3] = 1
        elif self.eth_list.currentText() == 'group C':
            input_[4] = 1
        elif self.eth_list.currentText() == 'group D':
            input_[5] = 1
        elif self.eth_list.currentText() == 'group E':
            input_[6] = 1

        if self.loe_list.currentText() == "associate's degree": 
            input_[7] = 1
        elif self.loe_list.currentText() == "bachelor's degree":
            input_[8] = 1
        elif self.loe_list.currentText() == "high school":
            input_[9] = 1
        elif self.loe_list.currentText() == "master's degree":
            input_[10] = 1
        elif self.loe_list.currentText() == "some college":
            input_[11] = 1
        
        if self.lunch_list.currentText() == "free/reduced":
            input_[12] = 1
        else:
            input_[13] = 1
        
        if self.test_list.currentText() == "completed":
            input_[14] = 1
        else:
            input_[15] = 1

        return input_

    def process(self):
        input_ = np.array(self.analyze())
        X = input_.reshape(1, -1)
        

        with open("C:\RESERVOIR\AI_ML\student\model.pkl", "rb") as file_object:
            classifier = pickle.load(file_object)

        prediction = classifier.predict(X)
        display_raw = str(prediction[0])
        output = ""
        if display_raw == "1":
            output = "True"
        elif display_raw == "0":
            output = "False"

        self.Performance.setText(output)
        print(output)

        




if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = PerformanceApp()
    window.show()

    sys.exit(app.exec_())
