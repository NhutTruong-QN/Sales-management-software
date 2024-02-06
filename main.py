import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5 import QtCore, QtGui, QtWidgets
from BVTNN import Ui_MainWindow

class MainWindow:
    dem = 0
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        self.uic.stackedWidget.setCurrentWidget(self.uic.mot_page)

        self.uic.thoat_bt.clicked.connect(self.main_win.close)
        self.uic.tieptuc_bt.clicked.connect(self.ThanhToanPage)
        self.uic.thanhtoan_bt.clicked.connect(self.ThanhToan)
        self.uic.trove_bt.clicked.connect(self.Home)

        dem1 = self.dem
        for c in self.uic.mot_page.children():
            if type(c) == QCheckBox:
                dem1 += 1
                c.stateChanged.connect(self.Check)
        self.dem = dem1

    def show(self):
        self.main_win.show()
    def Home(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.mot_page)
    def ThanhToanPage(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.hai_page)
    def Check(self):
        model = QtGui.QStandardItemModel()
        self.uic.dsdachon_lv.setModel(model)
        for c in self.uic.mot_page.children():
            if type(c) == QCheckBox and c.isChecked():
                item = QtGui.QStandardItem(c.text())
                model.appendRow(item)
    def ThanhToan(self):
        tong = self.dem
        self.uic.tong_tb.setText(str(tong * 100000))
        self.uic.tb_lb.setText("Thanh toán thành công!")
        self.uic.tb2_lb.setText("✓")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())