import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

"""
def main(): 
    app = QtGui.QApplication(sys.argv)
    
    w = QtGui.QWidget()
    w.resize(250, 250)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
"""

class Button(QtGui.QPushButton):

    def __init__(self, title, parent):
        super(Button, self).__init__(title, parent)

        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):

        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, QDropEvent):
        self.setText(QDropEvent.mimeData().text())


class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()

        self._initui()

    def _initui(self):

        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        # menubar
        exitAction = QtGui.QAction(QtGui.QIcon('Program.jpg'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.closeEvent)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        btn = QtGui.QPushButton('Quit', self)
        btn.clicked.connect(self.closeEvent)
        btn.setStatusTip('Quit Program')
        btn.setToolTip('This is a <u>Quit</u> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        # self.setGeometry(300, 300, 250, 150)

        # textEdit = QtGui.QTextEdit()
        # self.setCentralWidget(textEdit)\

        wid = QtGui.QWidget(self)
        self.setCentralWidget(wid)
        # okbutten = QtGui.QPushButton('OK')
        # cancelbutton = QtGui.QPushButton('Cancel')

        hbox = QtGui.QHBoxLayout()
        # hbox.addStretch(3)
        # hbox.addWidget(okbutten)
        hbox.addStretch(1)
        pmp = QtGui.QPixmap("Program.jpg")
        lbl = QtGui.QLabel(self)
        lbl.setPixmap(pmp)
        hbox.addWidget(lbl)

        edit = QtGui.QLineEdit('', self)
        edit.setDragEnabled(True)
        edit.move(30,65)

        button = Button("Button", self)
        button.move(190, 65)

        # hbox.addWidget(button)
        # hbox.addWidget(edit)
        hbox.addWidget(btn)
        wid.setLayout(hbox)
        #
        # vbox = QtGui.QVBoxLayout()
        # vbox.addStretch(5)
        # vbox.addLayout(hbox)
        # vbox.addStretch(5)
        # vbox.addWidget(cancelbutton)
        #
        # wid.setLayout(vbox)

        # grid = QtGui.QGridLayout()
        #
        # title = QtGui.QLabel('Title')
        # author = QtGui.QLabel('Author')
        # review = QtGui.QLabel('Review')
        #
        # titleEdit = QtGui.QLineEdit()
        # authorEdit = QtGui.QLineEdit()
        # reviewEdit = QtGui.QTextEdit()
        #
        # grid = QtGui.QGridLayout()
        # grid.setSpacing(3)
        #
        # grid.addWidget(title, 1, 0)
        # grid.addWidget(titleEdit, 1, 1)
        #
        # grid.addWidget(author, 2, 0)
        # grid.addWidget(authorEdit, 2, 1)
        #
        # grid.addWidget(reviewEdit, 3, 1, 7, 1)
        # grid.addWidget(review, 3, 0)
        #
        # wid.setLayout(grid)

        # col = QtGui.QColor(0, 0, 0)
        # col_btn = QtGui.QPushButton('Dialog', self)
        # col_btn.move(20, 20)
        #
        # col_btn.clicked.connect(self.showDialog)
        #
        # self.frm = QtGui.QFrame(self)
        # self.frm.setStyleSheet("QWidget {background-color: %s}" % col.name())
        # self.frm.setGeometry(130, 22, 100, 100)
        #
        # hbox.addWidget(col_btn)

        # self.col = QtGui.QColor(0, 0, 0)
        #
        # redb = QtGui.QPushButton('Red', self)
        # redb.setCheckable(True)
        # redb.move(10, 10)
        #
        # redb.clicked[bool].connect(self.setColor)
        #
        # greenb = QtGui.QPushButton('Green', self)
        # greenb.setCheckable(True)
        # greenb.move(10, 60)
        #
        # greenb.clicked[bool].connect(self.setColor)
        #
        # blueb = QtGui.QPushButton('Blue', self)
        # blueb.setCheckable(True)
        # blueb.move(10, 110)
        #
        # blueb.clicked[bool].connect(self.setColor)
        #
        # self.square = QtGui.QFrame(self)
        # self.square.setGeometry(150, 20, 100, 100)
        # self.square.setStyleSheet("QWidget { background-color: %s }" % self.col.name())
        #
        # self.cb = QtGui.QCheckBox('Show title', self)
        # # self.cb.toggle()
        # self.cb.stateChanged.connect(self.changeTitle)
        # print(self.cb.stateChanged)

        self.resize(100, 100)
        self.center()
        self.setWindowTitle("User Interface")

        self.setWindowIcon(QtGui.QIcon('Program.jpg'))
        self.statusBar().showMessage('Ready')
        self.show()

    def closeEvent(self, event):
        self.statusBar().showMessage('Quit')
        reply = QtGui.QMessageBox.question(self, 'Message', "Are you sure to quit",
                                           QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        # event = QtCore.QCoreApplication.instance().quit
        # self.statusBar().showMessage('Quit')
        if reply == QtGui.QMessageBox.Yes:
            # event.accept()
            QtCore.QCoreApplication.instance().quit()  # What difference between this two expression ?
            # QtGui.qApp.quit()
        else:
            # self.statusBar().showMessage('Ready')
            event.ignore()

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def keyPressEvent(self, i):

        if i.key() == QtCore.Qt.Key_Escape:
            self.close()

    def showDialog(self):

        col = QtGui.QColorDialog.getColor()

        if col.isValid():
            self.frm.setStyleSheet("QWidget {background-color: %s}" % col.name())

    def changeTitle(self, state):

        print(state)
        if state == QtCore.Qt.Checked:
            self.setWindowTitle('Programme')
        else:
            self.setWindowTitle('')

    def setColor(self, pressed):

        source = self.sender()

        if pressed:
            val = 255
        else:
            val = 0

        if source.text() == "Red":
            self.col.setRed(val)
        elif source.text() == "Green":
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)

        self.square.setStyleSheet("QFrame { background-color: %s }" % self.col.name())


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
