# Form implementation generated from reading ui file '.\boxscore.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_BoxScoreWindow(object):
    def setupUi(self, checkbox_home_3daf):
        checkbox_home_3daf.setObjectName("checkbox_home_3daf")
        checkbox_home_3daf.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=checkbox_home_3daf)
        self.centralwidget.setObjectName("centralwidget")
        self.timer_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.timer_label.setGeometry(QtCore.QRect(340, 20, 81, 51))
        self.timer_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.timer_label.setObjectName("timer_label")
        self.team_home_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.team_home_label.setGeometry(QtCore.QRect(120, 30, 141, 41))
        self.team_home_label.setObjectName("team_home_label")
        self.team_away_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.team_away_label.setGeometry(QtCore.QRect(520, 30, 131, 41))
        self.team_away_label.setObjectName("team_away_label")
        self.quarter_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.quarter_label.setGeometry(QtCore.QRect(370, 70, 61, 21))
        self.quarter_label.setObjectName("quarter_label")
        self.checkbox_home_1 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkbox_home_1.setGeometry(QtCore.QRect(20, 100, 76, 20))
        self.checkbox_home_1.setObjectName("checkbox_home_1")
        self.checkbox_home_2 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkbox_home_2.setGeometry(QtCore.QRect(20, 140, 76, 20))
        self.checkbox_home_2.setObjectName("checkbox_home_2")
        self.checkbox_home_3 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkbox_home_3.setGeometry(QtCore.QRect(20, 180, 76, 20))
        self.checkbox_home_3.setObjectName("checkbox_home_3")
        self.checkbox_home_4 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkbox_home_4.setGeometry(QtCore.QRect(20, 220, 76, 20))
        self.checkbox_home_4.setObjectName("checkbox_home_4")
        self.checkbox_home_5 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkbox_home_5.setGeometry(QtCore.QRect(20, 260, 76, 20))
        self.checkbox_home_5.setObjectName("checkbox_home_5")
        self.checkbox_away_2 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkbox_away_2.setGeometry(QtCore.QRect(630, 140, 76, 20))
        self.checkbox_away_2.setObjectName("checkbox_away_2")
        self.checkbox_away_3 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkbox_away_3.setGeometry(QtCore.QRect(630, 180, 76, 20))
        self.checkbox_away_3.setObjectName("checkbox_away_3")
        self.checkbox_away_1 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkbox_away_1.setGeometry(QtCore.QRect(630, 100, 76, 20))
        self.checkbox_away_1.setObjectName("checkbox_away_1")
        self.checkbox_away_5 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkbox_away_5.setGeometry(QtCore.QRect(630, 260, 76, 20))
        self.checkbox_away_5.setObjectName("checkbox_away_5")
        self.checkbox_away_4 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkbox_away_4.setGeometry(QtCore.QRect(630, 220, 76, 20))
        self.checkbox_away_4.setObjectName("checkbox_away_4")
        self.start_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(330, 110, 75, 24))
        self.start_button.setObjectName("start_button")
        self.free_throw_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.free_throw_button.setGeometry(QtCore.QRect(280, 150, 75, 24))
        self.free_throw_button.setObjectName("free_throw_button")
        self.layup_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.layup_button.setGeometry(QtCore.QRect(390, 150, 75, 24))
        self.layup_button.setObjectName("layup_button")
        self.three_point_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.three_point_button.setGeometry(QtCore.QRect(280, 180, 75, 24))
        self.three_point_button.setObjectName("three_point_button")
        self.missed_shot_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.missed_shot_button.setGeometry(QtCore.QRect(390, 180, 75, 24))
        self.missed_shot_button.setObjectName("missed_shot_button")
        self.rebound_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.rebound_button.setGeometry(QtCore.QRect(280, 210, 75, 24))
        self.rebound_button.setObjectName("rebound_button")
        self.assist_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.assist_button.setGeometry(QtCore.QRect(390, 210, 75, 24))
        self.assist_button.setObjectName("assist_button")
        self.steal_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.steal_button.setGeometry(QtCore.QRect(280, 240, 75, 24))
        self.steal_button.setObjectName("steal_button")
        self.turnover_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.turnover_button.setGeometry(QtCore.QRect(390, 240, 75, 24))
        self.turnover_button.setObjectName("turnover_button")
        self.home_score = QtWidgets.QLabel(parent=self.centralwidget)
        self.home_score.setGeometry(QtCore.QRect(150, 70, 41, 51))
        self.home_score.setObjectName("home_score")
        self.away_score = QtWidgets.QLabel(parent=self.centralwidget)
        self.away_score.setGeometry(QtCore.QRect(550, 70, 41, 51))
        self.away_score.setObjectName("away_score")
        checkbox_home_3daf.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=checkbox_home_3daf)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        checkbox_home_3daf.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=checkbox_home_3daf)
        self.statusbar.setObjectName("statusbar")
        checkbox_home_3daf.setStatusBar(self.statusbar)

        self.retranslateUi(checkbox_home_3daf)
        QtCore.QMetaObject.connectSlotsByName(checkbox_home_3daf)

    def retranslateUi(self, checkbox_home_3daf):
        _translate = QtCore.QCoreApplication.translate
        checkbox_home_3daf.setWindowTitle(_translate("checkbox_home_3daf", "MainWindow"))
        self.timer_label.setText(_translate("checkbox_home_3daf", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">10.00</span></p></body></html>"))
        self.team_home_label.setText(_translate("checkbox_home_3daf", "<html><head/><body><p><span style=\" font-size:16pt;\">Team Home</span></p></body></html>"))
        self.team_away_label.setText(_translate("checkbox_home_3daf", "<html><head/><body><p><span style=\" font-size:16pt;\">Team Away</span></p></body></html>"))
        self.quarter_label.setText(_translate("checkbox_home_3daf", "<html><head/><body><p><span style=\" font-size:12pt;\">Q1</span></p></body></html>"))
        self.checkbox_home_1.setText(_translate("checkbox_home_3daf", "CheckBox"))
        self.checkbox_home_2.setText(_translate("checkbox_home_3daf", "CheckBox"))
        self.checkbox_home_3.setText(_translate("checkbox_home_3daf", "CheckBox"))
        self.checkbox_home_4.setText(_translate("checkbox_home_3daf", "CheckBox"))
        self.checkbox_home_5.setText(_translate("checkbox_home_3daf", "CheckBox"))
        self.checkbox_away_2.setText(_translate("checkbox_home_3daf", "CheckBox"))
        self.checkbox_away_3.setText(_translate("checkbox_home_3daf", "CheckBox"))
        self.checkbox_away_1.setText(_translate("checkbox_home_3daf", "CheckBox"))
        self.checkbox_away_5.setText(_translate("checkbox_home_3daf", "CheckBox"))
        self.checkbox_away_4.setText(_translate("checkbox_home_3daf", "CheckBox"))
        self.start_button.setText(_translate("checkbox_home_3daf", "Start"))
        self.free_throw_button.setText(_translate("checkbox_home_3daf", "+1"))
        self.layup_button.setText(_translate("checkbox_home_3daf", "+2"))
        self.three_point_button.setText(_translate("checkbox_home_3daf", "+3"))
        self.missed_shot_button.setText(_translate("checkbox_home_3daf", "Missed shot"))
        self.rebound_button.setText(_translate("checkbox_home_3daf", "Rebound"))
        self.assist_button.setText(_translate("checkbox_home_3daf", "Assist"))
        self.steal_button.setText(_translate("checkbox_home_3daf", "Steal"))
        self.turnover_button.setText(_translate("checkbox_home_3daf", "Turnover"))
        self.home_score.setText(_translate("checkbox_home_3daf", "<html><head/><body><p><span style=\" font-size:24pt;\">00</span></p></body></html>"))
        self.away_score.setText(_translate("checkbox_home_3daf", "<html><head/><body><p><span style=\" font-size:24pt;\">00</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    checkbox_home_3daf = QtWidgets.QMainWindow()
    ui = Ui_BoxScoreWindow()
    ui.setupUi(checkbox_home_3daf)
    checkbox_home_3daf.show()
    sys.exit(app.exec())
