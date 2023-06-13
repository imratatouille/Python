from PySide6 import QtCore, QtGui, QtWidgets

class AnalogClock(QtWidgets.QWidget):
    p_hour = QtGui.QPolygon([
        QtCore.QPoint(5, 8),
        QtCore.QPoint(-5, 8),
        QtCore.QPoint(0, -40)
    ])

    p_min = QtGui.QPolygon([
        QtCore.QPoint(5, 8),
        QtCore.QPoint(-5, 8),
        QtCore.QPoint(0, -70)
    ])

    p_sec = QtGui.QPolygon([
        QtCore.QPoint(2, 8),
        QtCore.QPoint(-2, 8),
        QtCore.QPoint(0, -90)
    ])

    hourColor = QtGui.QColor(127, 0, 127)
    minuteColor = QtGui.QColor(127, 127, 191)
    secColor = QtGui.QColor(255, 0, 0)

    def __init__(self, parent=None):
        super(AnalogClock, self).__init__(parent)

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(1000)

        quitAction = QtGui.QAction("E&xit", self, shortcut="Ctrl+Q",
                triggered=QtWidgets.QApplication.instance().quit)
        self.addAction(quitAction)
        self.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        
        self.setWindowTitle("아날로그 시계")
        self.resize(200, 200)
        self.old_pos = 0

        self.setWindowFlags(
            QtCore.Qt.FramelessWindowHint
            | QtCore.Qt.WindowStaysOnTopHint
            | QtCore.Qt.SplashScreen
        )
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

    def mousePressEvent(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            self.old_pos = e.globalPosition().toPoint() - self.frameGeometry().topLeft()

    def mouseMoveEvent(self, e):
        if e.buttons() & QtCore.Qt.LeftButton:
            self.move(e.globalPosition().toPoint()-self.old_pos)

    def paintEvent(self, event):
        time = QtCore.QTime.currentTime()
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.translate(self.width() / 2, self.height() / 2)

        painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(QtCore.Qt.white)
        painter.drawEllipse(QtCore.QPoint(0, 0), 98, 98)

        painter.setPen(self.hourColor)
        for i in range(12):
            painter.drawLine(88, 0, 96, 0)
            painter.rotate(30.0)

        painter.setPen(self.minuteColor)
        for j in range(60):
            if (j % 5) != 0:
                painter.drawLine(92, 0, 96, 0)
            painter.rotate(6.0)

        painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(self.hourColor)
        painter.save()
        painter.rotate(30.0 * ((time.hour() + time.minute() / 60.0)))
        painter.drawConvexPolygon(self.p_hour)
        painter.restore()

        painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(self.minuteColor)
        painter.save()
        painter.rotate(6.0 * (time.minute() + time.second() / 60.0))
        painter.drawConvexPolygon(self.p_min)
        painter.restore()

        painter.setBrush(self.secColor)
        painter.save()
        painter.rotate(time.second() * 6.0)
        painter.drawConvexPolygon(self.p_sec)
        painter.restore()
        
        painter.end()

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    clock = AnalogClock()
    clock.show()
    app.exec()