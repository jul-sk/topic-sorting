# -*- coding: utf-8 -*-

import sys
from PyQt5.QtGui import QIcon, QPainter, QColor, QPen, QPalette, QBrush
from PyQt5.QtWidgets import (QWidget, QLabel, QPushButton, QSlider, QFrame,
    QHBoxLayout, QVBoxLayout, QApplication, QLineEdit, QFileDialog)
from PyQt5.QtCore import Qt

from sorting_algorithm import paper_assign

class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()

    def initUI(self):
        
        browseButton = QPushButton("Browse")
        browseButton.setAutoFillBackground(True)
        browseButton.setMaximumHeight(43)
        saveButton = QPushButton("Browse")
        sortButton = QPushButton("Sort")
        cancelButton = QPushButton("Cancel")
        prefButton = QPushButton("Advanced Options")
        textbox_in = QLineEdit()
        textbox_in.setTextMargins(5, 5, 6, 6)
        textbox_out = QLineEdit()
        textbox_out.setTextMargins(5, 5, 6, 6)
        cat1_num = QLineEdit()
        cat2_num = QLineEdit()
        cat3_num = QLineEdit()
        
        popSlider= QSlider(orientation = Qt.Horizontal)
        popSlider.setTickInterval(20)
        popSlider.setTickPosition(QSlider.TicksBelow)
        popReadout = QLabel('100')
        def updatePopulationSize(n): 
            popReadout.setText(str(n))
        popSlider.valueChanged[int].connect(updatePopulationSize)
        popSlider.setMaximum(500)
        popSlider.setMinimum(50)
        popSlider.setValue(100)
        
        rptSlider= QSlider(orientation = Qt.Horizontal)
        rptSlider.setTickInterval(10)
        rptSlider.setTickPosition(QSlider.TicksBelow)
        rptReadout = QLabel('50')
        def updateRpts(n): 
            rptReadout.setText(str(n))
        rptSlider.valueChanged[int].connect(updateRpts)
        rptSlider.setMaximum(200)
        rptSlider.setMinimum(1)
        rptSlider.setValue(50)
        
        iterSlider= QSlider(orientation = Qt.Horizontal)
        iterSlider.setTickInterval(30)
        iterSlider.setTickPosition(QSlider.TicksBelow)
        iterReadout = QLabel('50')
        def updateIterations(n): 
            iterReadout.setText(str(n))
        iterSlider.valueChanged[int].connect(updateIterations)
        iterSlider.setMaximum(500)
        iterSlider.setMinimum(10)
        iterSlider.setValue(50)
        
        # Set window background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(50, 40, 60))
                
        brush = QBrush(QColor(200, 200, 200))
        p.setBrush(QPalette.Active, QPalette.WindowText, brush)
        
        brush = QBrush(QColor(0, 100, 0))
        brush.setStyle(Qt.SolidPattern)
        p.setBrush(QPalette.Inactive, QPalette.Button, brush)
        self.setPalette(p)
        
        def selectFile():     
            textbox_in.setText(QFileDialog.getOpenFileName()[0])
            
        def saveFile():     
            textbox_out.setText(QFileDialog.getSaveFileName()[0])        
            
        def runSort():
            input_file = textbox_in.text()
            output_file = textbox_out.text()
            n1 = int(cat1_num.text())
            n2 = int(cat2_num.text())
            n3 = int(cat3_num.text())
            section_counts = [n1,n2,n3]
            
            f = open(input_file, "r")
            lines = f.readlines()
            if sum(section_counts) != len(lines[0].split(',')[5:]):
                print('category counts do not sum up to total options from input file')
                return
            paper_assign(str(input_file), str(output_file), section_counts,
                         population_size=int(popReadout.text()), 
                         num_iterations=int(iterReadout.text()),
                         repeat_all=int(rptReadout.text()))
                
        def showPrefs():
            prefFrame.setHidden(not prefFrame.isHidden())
            self.setFixedSize(self.sizeHint())

        browseButton.clicked.connect(selectFile)
        saveButton.clicked.connect(saveFile)
        sortButton.clicked.connect(runSort)
        prefButton.clicked.connect(showPrefs)
        hboxinst = QHBoxLayout()
        hboxinst.addStretch(2)
        hboxinst.addWidget(QLabel('Number of papers in each category (in order):'))
        hboxinst.addStretch(8)       

        hcatbox1 = QHBoxLayout()
        hcatbox1.addStretch(2)       
        hcatbox1.addWidget(QLabel('1st: '))
        hcatbox1.addWidget(cat1_num,2)
        hcatbox1.addStretch(8)       
        
        hcatbox2 = QHBoxLayout()
        hcatbox2.addStretch(2)       
        hcatbox2.addWidget(QLabel('2nd:'))
        hcatbox2.addWidget(cat2_num,2)
        hcatbox2.addStretch(8)       
        
        hcatbox3 = QHBoxLayout()
        hcatbox3.addStretch(2)       
        hcatbox3.addWidget(QLabel('3rd: '))
        hcatbox3.addWidget(cat3_num,2)
        hcatbox3.addStretch(8)       

        hbox = QHBoxLayout()
        hbox.addWidget(QLabel('Input file:'))
        hbox.addWidget(browseButton,1)
        hbox.addWidget(textbox_in, 10)
        
        hbox1 = QHBoxLayout()
        hbox1.addWidget(QLabel('Output file:'))
        hbox1.addWidget(saveButton,1)
        hbox1.addWidget(textbox_out, 10)
        hbox1.addWidget(sortButton, 2)
   
        hbox2 = QHBoxLayout()
        hbox2.addWidget(QLabel('Population size:'))
        hbox2.addWidget(popSlider)
        hbox2.addWidget(popReadout)
        
        hbox3 = QHBoxLayout()
        hbox3.addWidget(QLabel('Number of iterations:'))
        hbox3.addWidget(iterSlider)
        hbox3.addWidget(iterReadout)
        
        hbox4 = QHBoxLayout()
        hbox4.addWidget(QLabel('Number of repeats:'))
        hbox4.addWidget(rptSlider)
        hbox4.addWidget(rptReadout)
        
      
        vbox1 = QVBoxLayout()
        vbox1.addLayout(hboxinst)
        vbox1.addLayout(hcatbox1)
        vbox1.addLayout(hcatbox2)    
        vbox1.addLayout(hcatbox3)    
        vbox1.addLayout(hbox)    
        vbox1.addLayout(hbox1)   
        vbox1.addWidget(prefButton)
        
        vbox2 = QVBoxLayout()
        vbox2.addLayout(hbox2)  
        vbox2.addLayout(hbox3)  
        vbox2.addLayout(hbox4)  
        prefFrame = QFrame()
        prefFrame.setLayout(vbox2)
        
        vbox = QVBoxLayout()
        vbox.addLayout(vbox1)
        vbox.addWidget(prefFrame)

        prefFrame.setHidden(1)
        self.setLayout(vbox)
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('HKT Paper Sorting')
        self.setWindowIcon(QIcon('sort-hat.ico'))        
        self.show()

if __name__ == '__main__':
        
    app = QApplication(sys.argv)
    
    ex = MainWindow()
    sys.exit(app.exec_())  