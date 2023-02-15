import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import *
import random
from random import randint
import pandas as pd
from brainflow.board_shim import BoardShim, BrainFlowInputParams,BoardIds



     
class WindowClass(QMainWindow):
    def __init__(self) :
        super().__init__()
        self.setGeometry(1100, 300,1200, 800)
        self.setWindowTitle('Set Protocol')
        
        self.timer = QTimer(self)
        self.time=0
        #label
        self.label = QLabel("실험을 시작하려면 시작하기 버튼을 눌러주세요", self)
        font1 = self.label.font()
        font1.setBold(True)
        font1.setPointSize(20)
        self.label.setFont(font1)
        self.label.setGeometry(300,300,700,50)
        #button
        self.btn_1= QPushButton("시작하기",self)
        self.btn_1.setGeometry(550,500,100,50)
        self.btn_1.clicked.connect(self.btn_1_clicked)
        
    
    def btn_1_clicked(self):
        
        global last
        self.label.clear()
        self.btn_1.hide()
        ref = 0
        last=0
        r_num=0
        for i in range(5):
            
            randtime=[1000,2000]
            
            ref += r_num
            QTimer.singleShot(ref, self.point)
            QTimer.singleShot(ref+1000, self.close1)
            QTimer.singleShot(ref+1000, self.random)
            QTimer.singleShot(ref+1500, self.close2)
            QTimer.singleShot(ref+1500, self.point1)
            QTimer.singleShot(ref+4000, self.close3)
            QTimer.singleShot(ref+4000,self.point_blue) 
            QTimer.singleShot(ref+5000,self.close4) 
            last=4500+1000
            r_num=last
            QTimer.singleShot(ref+r_num,self.pr_data) 
        QTimer.singleShot(ref+r_num,self.close)
        
            
    def pr_data(self):
        data = board.get_board_data()
        print(data.shape)
        data=pd.DataFrame(data)
        data.to_csv("result_01.csv")
        
            
    def p(self):
        print()
       
    def point (self):
        protocol.point(self)
        
    def random(self): 
        protocol.random(self)
        print(self.time,"e")
        
    def point1(self):   
        protocol.point1(self)
        print(self.time,"r")
      
    def point_blue(self):
        protocol.point_blue(self)
        
             
    def close1(self):
        label2.close()  
       
    def close2(self):
        label3.close() 
      
    def close3(self):
        label4.close()  
    def close4(self):
        label5.close() 
        
        
class protocol(WindowClass):
    def __init__(self) :
        super().__init__()
    
    def point(self):
        global label2
        label2 = QLabel("·",self)
        font2 = label2.font()
        font2.setBold(True)
        font2.setPointSize(200)
        label2.setFont(font2)
        label2.setGeometry(550,350,700,50)
        label2.show()
    
                
    def close1():
        label2.close()
                
    def random(self):
        target=["↑","←","↓","→"] 
        global label3   
        label3=QLabel(target[randint(0,3)],self)
        font2 = label3.font()
        font2.setBold(True)
        font2.setPointSize(100)
        label3.setFont(font2)
        label3.setGeometry(550,50,400,700)
        label3.show()
        
    def close2():
        label3.close()
        
    def point1(self):
        global label4
        label4 = QLabel("·",self)
        font2 = label4.font()
        font2.setBold(True)
        font2.setPointSize(200)
        label4.setFont(font2)
        label4.setGeometry(550,350,700,50)
        label4.show()
        
    def close3():
        label4.close() 
    def point_blue(self):
        global label5
        label5 = QLabel("·",self)
        font2 = label5.font()
        label5.setStyleSheet("color: blue")
        font2.setBold(True)
        font2.setPointSize(200)
        label5.setFont(font2)
        label5.setGeometry(550,350,700,50)
        label5.show()
        
    def close4():
        label5.close()
        
        
    
            
    
        

                
        
        
    
        
        

        
        
class fun:
    def start_board():
        serial_port="COM3"
        params = BrainFlowInputParams() 
        params.serial_port = serial_port 
        params.serial_number = '' 
        params.timeout = 0 
        params.other_info = '' 
        params.file = '' 
        params.mac_address = '' 
        params.ip_address = '' 
        params.ip_port = 0 
        params.ip_protocol = 0
        board = BoardShim(BoardIds.CYTON_BOARD, params) 
        board.prepare_session()
        #board.config_board('xU060100X') 
        board.start_stream()
        return board
            
    
        
        
if __name__ == "__main__" :
    board_id=2
    serial_port="COM3"
    board = fun.start_board()
    
    
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()
    
    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()

