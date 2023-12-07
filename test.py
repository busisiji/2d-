import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtGui import QPixmap

class ImageWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建一个标签控件
        self.imageLabel = QLabel(self)
        self.setCentralWidget(self.imageLabel)

        # 加载图片并缩放
        pixmap = QPixmap('1.jpg')
        pixmap = pixmap.scaledToHeight(200)
        self.imageLabel.setPixmap(pixmap)

        # 调整窗口大小以适应图片
        self.resize(pixmap.width(), 200)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ImageWindow()
    window.show()
    sys.exit(app.exec_())
