from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import ui.design as design


class MyApp(QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.button_clicked)

    def button_clicked(self):
        self.label.setText('Button was clicked!!!')


def main():
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
