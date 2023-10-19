from sys import exit
from threading import Thread
from time import sleep
from stayl import *
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout
class Windows1(Window):
    def __init__(self):
        super().__init__()
        self.box_v = QVBoxLayout()
        self.box_h = QHBoxLayout()
        self.btn = Button("Send")
        self.Lb_edit = Edit()
        self.Lb_edit.setPlaceholderText("Your name...")
        self.thread = Thread(target=self.updete)
        self.thread.start()

        self.lbl = QLW()
        self.Lb_edit_message = Edit1()
        self.Lb_edit_message.setPlaceholderText("Enter your message...")

        self.box_h.addWidget(self.Lb_edit_message)
        self.box_h.addWidget(self.btn)

        self.box_v.addWidget(self.Lb_edit)
        self.box_v.addWidget(self.lbl)
        self.box_v.addLayout(self.box_h)

        self.setLayout(self.box_v)

        self.btn.clicked.connect(self.btn_send)

    def btn_send(self):
        if len(self.Lb_edit.text()) != 0 and 0 != len(self.Lb_edit_message.text())  \
        and self.Lb_edit.text().isalpha() and self.Lb_edit_message.text().isalpha():
            with open("name.txt", "a") as h:
                m = self.Lb_edit.text()+"|"+self.Lb_edit_message.text()+"\n"
                h.write(m)
                self.Lb_edit_message.clear()


    def updete(self):
        while True:
            sleep(1)
            self.lbl.clear()
            with open("name.txt", "r") as h:
                txt = h.readlines()
                for i in range(len(txt)):
                    txt[i] = txt[i].split("|")
                for i in range(len(txt)):
                    txt_message = txt[i][0] +" message: " + txt[i][1]

                    self.lbl.addItem(txt_message)


app = QApplication([])
menu = Windows1()
menu.show()
exit(app.exec_())