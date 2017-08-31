#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 学習するための画像を用意したいが、分類は手動でやらなければならない
# めんどくさい分類をより簡単に行うためにこのプログラムを作成した
# ここでは画像を３種類に分けることを想定している
# キー AとSとDをタイプして画像を３種類に分類する
# 画像はwindowに表示されるので、表示された画像を見て画像の種類と一致するキーをタイプすればよい。


import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QLabel
from PyQt5.QtGui import QPixmap
from PIL import Image
import shutil
import os 

class ImageClassify(QWidget):
    
    def __init__(self):
        super().__init__()
        self.dir_name = "./image_dir/"
        self.count = 0;
        self.files = os.listdir(self.dir_name) # ディレクトリ内の全ファイル名を取得

        if not os.path.exists("./a"):
            os.mkdir("./a");

        if not os.path.exists("./b"):
            os.mkdir("./b");

        if not os.path.exists("./c"):
            os.mkdir("./c");

        self.initUI()
    
    # 初期UI設定    
    def initUI(self):      
        self.hbox = QHBoxLayout(self)
        self.file_name = self.files[self.count]
        #img = Image.open(self.dir_name + self.file_name)
        self.pixmap = QPixmap(self.dir_name + self.file_name)

        self.lbl = QLabel(self)
        #lbl.setPixmap(self.pixmap)

        self.hbox.addWidget(self.lbl)
        self.lbl.move(100,100)
        self.lbl.setPixmap(self.pixmap)

        self.setGeometry(300, 300, 1000, 500)
        self.setWindowTitle('Event handler')
    
        self.show()
        
        
    # 次のスライドに遷移するための関数
    def image_renew(self):
        self.count += 1
        self.file_name = self.files[self.count]
        self.pixmap = QPixmap(self.dir_name + self.file_name)
        self.lbl.setPixmap(self.pixmap)

    # key イベント
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_A:
           shutil.copy(self.dir_name + self.file_name, "./a/" + self.file_name)
           self.image_renew()
        if e.key() == Qt.Key_S:
           shutil.copy(self.dir_name + self.file_name, "./b/" + self.file_name)
           self.image_renew()
        if e.key() == Qt.Key_D:
           shutil.copy(self.dir_name + self.file_name, "./c/" + self.file_name)
           self.image_renew() # keyを押したら次の画像にスライド
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = ImageClassify()
    sys.exit(app.exec_())
