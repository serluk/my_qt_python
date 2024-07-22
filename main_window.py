from PyQt6.QtWidgets import QApplication, QGridLayout, QWidget
from left_panel import LeftPanel
from right_panel import RightPanel


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.qg = QGridLayout()
        self.qg.addWidget(LeftPanel(), 1, 0)
        self.qg.addWidget(RightPanel(), 1, 1)

        self.setLayout(self.qg)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


