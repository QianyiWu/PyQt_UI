import sys
from PyQt4 import QtCore, QtGui


class MyWindow(QtGui.QMainWindow):
    """
        Mainwindow Class
    """

    def __init__(self):
        super(MyWindow, self).__init__()

        self._init_ui()

    def _init_ui(self):
        """
            UI initialization
        """
        # QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10, QtGui.QFont.Black))
        # QtGui.QToolTip.setPalette(QtGui.QPalette.)

        windows = QtGui.QWidget(self)  # MainWindows    CentralWidget
        self.setCentralWidget(windows)

        hbox = QtGui.QHBoxLayout()   # MainWindows layout: Left. Menu    Right. image
        image_box = QtGui.QVBoxLayout()   # Right Part Layout

        self.button_menu = QtGui.QVBoxLayout()  # Menu Button
        self.create_btn_menu()

        self.image_show_ = QtGui.QLabel()   # Displayed Image
        self.image_show_.setFrameStyle(QtGui.QFrame.StyledPanel)
        self.image_show_.setAlignment(QtCore.Qt.AlignCenter)

        select_image_frame = QtGui.QFrame()   # Select image, can add new image by 'Open Selection' button
        select_image_frame.setFrameStyle(QtGui.QFrame.WinPanel)
        self.select_image_layout = QtGui.QHBoxLayout()
        self.select_image_layout.setAlignment(QtCore.Qt.AlignLeft)
        select_image_frame.setLayout(self.select_image_layout)
        self.select_image_list = []   # A image list

        self.select_btn_gruop = QtGui.QButtonGroup()   # Group all selection button
        self.select_btn_gruop.exclusive()

        splitter = QtGui.QSplitter(QtCore.Qt.Vertical)   # Splitter
        splitter.addWidget(self.image_show_)
        splitter.addWidget(select_image_frame)
        splitter.setStretchFactor(0, 10)
        splitter.setStretchFactor(1, 1)

        image_box.addWidget(splitter)
        hbox.addLayout(self.button_menu)
        hbox.setStretchFactor(self.button_menu, 1)
        hbox.addLayout(image_box)
        hbox.setStretchFactor(image_box, 10)
        windows.setLayout(hbox)

        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('platinum'))

        self.resize(1000, 1000)
        # self.showFullScreen()
        # self.center()
        self.setWindowTitle("User Interface")

        self.setWindowIcon(QtGui.QIcon("Icon/Program.jpg"))
        self.statusBar().showMessage('User Interface')
        self.show()

    # def center(self):
    #     qr = self.frameGeometry()
    #     cp = QtGui.QDesktopWidget().availableGeometry().center()
    #     qr.moveCenter(cp)
    #     self.move(qr.topLeft())

    def create_btn_menu(self):
        open_btn = QtGui.QPushButton('Open File', self)
        QtCore.QObject.connect(open_btn, QtCore.SIGNAL('clicked()'), self.fileopen)

        sel_file_open = QtGui.QPushButton('Open Selection', self)
        sel_file_open.setToolTip("Open File and set as selectable button")
        QtCore.QObject.connect(sel_file_open, QtCore.SIGNAL('clicked()'), self.select_file_open)

        self.button_menu.addWidget(open_btn)
        self.button_menu.addWidget(sel_file_open)
        self.button_menu.addStretch(10)

    def fileopen(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '/home/wooqy',
                                                  self.tr("Images(*.bmp *.jpg *.png)"))
        f = open(fname, 'r')

        with f:
            img = QtGui.QPixmap(f.name)
            # scale
            # self.image_show_.setPixmap(img.resized(700, 700))

    def select_file_open(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '/home/wooqy',
                                                  self.tr("Images(*.bmp *.jpg *.png)"))
        f = open(fname, 'r')

        with f:
            img = QtGui.QPixmap(f.name)
            # Maybe need scale
            self.select_image_list.append(img)
            self.show_select_image(img)

    def show_select_image(self, img):
        if self.select_image_list.__len__() != 0:
            new_btn = QtGui.QPushButton()
            new_btn.setIcon(QtGui.QIcon(img))
            new_btn.setFixedSize(100, 100)
            new_btn.setIconSize(QtCore.QSize(100, 100))
            new_btn.setCheckable(True)
            new_btn.setStyleSheet("QPushButton::pressed{ border-style: inset}")
            self.select_image_layout.addWidget(new_btn)
            self.select_btn_gruop.addButton(new_btn)
            new_btn.clicked[bool].connect(self.func_select)

    def func_select(self, pressed):
        source = self.sender()
        if pressed:
            img = source.icon().pixmap(700, 700)
            self.image_show_.setPixmap(img)


def main():
    app = QtGui.QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
