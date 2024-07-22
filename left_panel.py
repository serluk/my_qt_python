from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QApplication


class LeftPanel(QWidget):
    def __init__(self, parent=None):
        super(LeftPanel, self).__init__(parent)
        self.qvb1 = QVBoxLayout()
        self.setMinimumSize(300, 300)
        self.button1 = QPushButton("Click Me")
        self.qvb1.addWidget(self.button1)
        self.setLayout(self.qvb1)


# if __name__ == "__main__":
#     app = QApplication([])
#     w = LeftPanel()
#     app.exec()