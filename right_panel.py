from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QApplication


class RightPanel(QWidget):
    def __init__(self, parent=None):
        super(RightPanel, self).__init__(parent)
        self.setMinimumSize(300, 300)
        self.qvb1 = QVBoxLayout()
        self.ledit = QLineEdit("Click Me")
        self.qvb1.addWidget(self.ledit)
        self.setLayout(self.qvb1)

# if __name__ == "__main__":
#     app = QApplication([])
#     w = RightPanel()
#     print(type(w))
#     app.exec()
