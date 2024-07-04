# -*- coding: utf-8 -*-



################################################################################

## Form generated from reading UI file 'window.ui'

##

## Created by: Qt User Interface Compiler version 6.7.1

##

## WARNING! All changes made in this file will be lost when recompiling UI file!

################################################################################



from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,

    QMetaObject, QObject, QPoint, QRect,

    QSize, QTime, QUrl, Qt)

from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,

    QFont, QFontDatabase, QGradient, QIcon,

    QImage, QKeySequence, QLinearGradient, QPainter,

    QPalette, QPixmap, QRadialGradient, QTransform)

from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGroupBox,

    QHBoxLayout, QLabel, QMainWindow, QPushButton,

    QSizePolicy, QSpacerItem, QStackedWidget, QTextEdit,

    QVBoxLayout, QWidget)

import ui.resource_rc



class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        if not MainWindow.objectName():

            MainWindow.setObjectName(u"MainWindow")

        MainWindow.resize(750, 600)

        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        sizePolicy.setHorizontalStretch(0)

        sizePolicy.setVerticalStretch(0)

        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())

        MainWindow.setSizePolicy(sizePolicy)

        MainWindow.setMinimumSize(QSize(750, 600))

        MainWindow.setMaximumSize(QSize(750, 600))

        icon = QIcon()

        icon.addFile(u":/icon/icon/GITSIM.png", QSize(), QIcon.Normal, QIcon.Off)

        MainWindow.setWindowIcon(icon)

        self.centralwidget = QWidget(MainWindow)

        self.centralwidget.setObjectName(u"centralwidget")

        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())

        self.centralwidget.setSizePolicy(sizePolicy)

        self.centralwidget.setMinimumSize(QSize(750, 600))

        self.centralwidget.setMaximumSize(QSize(750, 600))

        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)

        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.icon_only_widget = QWidget(self.centralwidget)

        self.icon_only_widget.setObjectName(u"icon_only_widget")

        sizePolicy.setHeightForWidth(self.icon_only_widget.sizePolicy().hasHeightForWidth())

        self.icon_only_widget.setSizePolicy(sizePolicy)

        self.verticalLayout = QVBoxLayout(self.icon_only_widget)

        self.verticalLayout.setSpacing(0)

        self.verticalLayout.setObjectName(u"verticalLayout")

        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.menu_button_1 = QPushButton(self.icon_only_widget)

        self.menu_button_1.setObjectName(u"menu_button_1")

        self.menu_button_1.setCursor(QCursor(Qt.PointingHandCursor))

        icon1 = QIcon()

        icon1.addFile(u":/icon/icon/menu-4-32.ico", QSize(), QIcon.Normal, QIcon.Off)

        self.menu_button_1.setIcon(icon1)

        self.menu_button_1.setIconSize(QSize(20, 20))

        self.menu_button_1.setCheckable(True)



        self.verticalLayout.addWidget(self.menu_button_1)



        self.verticalSpacer = QSpacerItem(20, 413, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)



        self.verticalLayout.addItem(self.verticalSpacer)



        self.connection_button_1 = QPushButton(self.icon_only_widget)

        self.connection_button_1.setObjectName(u"connection_button_1")

        self.connection_button_1.setCursor(QCursor(Qt.PointingHandCursor))

        icon2 = QIcon()

        icon2.addFile(u":/icon/icon/home-4-32.ico", QSize(), QIcon.Normal, QIcon.Off)

        self.connection_button_1.setIcon(icon2)

        self.connection_button_1.setIconSize(QSize(20, 20))

        self.connection_button_1.setCheckable(True)

        self.connection_button_1.setAutoExclusive(True)



        self.verticalLayout.addWidget(self.connection_button_1)



        self.measurement_button_1 = QPushButton(self.icon_only_widget)

        self.measurement_button_1.setObjectName(u"measurement_button_1")

        self.measurement_button_1.setCursor(QCursor(Qt.PointingHandCursor))

        icon3 = QIcon()

        icon3.addFile(u":/icon/icon/dashboard-32.ico", QSize(), QIcon.Normal, QIcon.Off)

        self.measurement_button_1.setIcon(icon3)

        self.measurement_button_1.setIconSize(QSize(20, 20))

        self.measurement_button_1.setCheckable(True)

        self.measurement_button_1.setAutoExclusive(True)



        self.verticalLayout.addWidget(self.measurement_button_1)



        self.curve_button_1 = QPushButton(self.icon_only_widget)

        self.curve_button_1.setObjectName(u"curve_button_1")

        self.curve_button_1.setCursor(QCursor(Qt.PointingHandCursor))

        icon4 = QIcon()

        icon4.addFile(u":/icon/icon/graph-32.ico", QSize(), QIcon.Normal, QIcon.Off)

        self.curve_button_1.setIcon(icon4)

        self.curve_button_1.setIconSize(QSize(20, 20))

        self.curve_button_1.setCheckable(True)

        self.curve_button_1.setAutoExclusive(True)



        self.verticalLayout.addWidget(self.curve_button_1)



        self.error1_button_1 = QPushButton(self.icon_only_widget)

        self.error1_button_1.setObjectName(u"error1_button_1")

        self.error1_button_1.setCursor(QCursor(Qt.PointingHandCursor))

        icon5 = QIcon()

        icon5.addFile(u":/icon/icon/multiply-2-32.ico", QSize(), QIcon.Normal, QIcon.Off)

        self.error1_button_1.setIcon(icon5)

        self.error1_button_1.setIconSize(QSize(20, 20))

        self.error1_button_1.setCheckable(True)

        self.error1_button_1.setAutoExclusive(True)



        self.verticalLayout.addWidget(self.error1_button_1)



        self.error2_button_1 = QPushButton(self.icon_only_widget)

        self.error2_button_1.setObjectName(u"error2_button_1")

        self.error2_button_1.setCursor(QCursor(Qt.PointingHandCursor))

        icon6 = QIcon()

        icon6.addFile(u":/icon/icon/elevator-32.ico", QSize(), QIcon.Normal, QIcon.Off)

        self.error2_button_1.setIcon(icon6)

        self.error2_button_1.setIconSize(QSize(20, 20))

        self.error2_button_1.setCheckable(True)

        self.error2_button_1.setAutoExclusive(True)



        self.verticalLayout.addWidget(self.error2_button_1)





        self.horizontalLayout_2.addWidget(self.icon_only_widget)



        self.full_menu_widget = QWidget(self.centralwidget)

        self.full_menu_widget.setObjectName(u"full_menu_widget")

        sizePolicy.setHeightForWidth(self.full_menu_widget.sizePolicy().hasHeightForWidth())

        self.full_menu_widget.setSizePolicy(sizePolicy)

        self.full_menu_widget.setAutoFillBackground(False)

        self.verticalLayout_2 = QVBoxLayout(self.full_menu_widget)

        self.verticalLayout_2.setSpacing(0)

        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.menu_button_2 = QPushButton(self.full_menu_widget)

        self.menu_button_2.setObjectName(u"menu_button_2")

        font = QFont()

        font.setPointSize(11)

        font.setBold(True)

        self.menu_button_2.setFont(font)

        self.menu_button_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.menu_button_2.setIcon(icon1)

        self.menu_button_2.setIconSize(QSize(14, 14))

        self.menu_button_2.setCheckable(True)



        self.verticalLayout_2.addWidget(self.menu_button_2)



        self.verticalSpacer_2 = QSpacerItem(20, 437, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)



        self.verticalLayout_2.addItem(self.verticalSpacer_2)



        self.connection_button_2 = QPushButton(self.full_menu_widget)

        self.connection_button_2.setObjectName(u"connection_button_2")

        self.connection_button_2.setFont(font)

        self.connection_button_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.connection_button_2.setIcon(icon2)

        self.connection_button_2.setIconSize(QSize(14, 14))

        self.connection_button_2.setCheckable(True)

        self.connection_button_2.setAutoExclusive(True)



        self.verticalLayout_2.addWidget(self.connection_button_2)



        self.measurement_button_2 = QPushButton(self.full_menu_widget)

        self.measurement_button_2.setObjectName(u"measurement_button_2")

        self.measurement_button_2.setFont(font)

        self.measurement_button_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.measurement_button_2.setIcon(icon3)

        self.measurement_button_2.setIconSize(QSize(14, 14))

        self.measurement_button_2.setCheckable(True)

        self.measurement_button_2.setAutoExclusive(True)



        self.verticalLayout_2.addWidget(self.measurement_button_2)



        self.curve_button_2 = QPushButton(self.full_menu_widget)

        self.curve_button_2.setObjectName(u"curve_button_2")

        self.curve_button_2.setFont(font)

        self.curve_button_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.curve_button_2.setIcon(icon4)

        self.curve_button_2.setIconSize(QSize(14, 14))

        self.curve_button_2.setCheckable(True)

        self.curve_button_2.setAutoExclusive(True)



        self.verticalLayout_2.addWidget(self.curve_button_2)



        self.error1_button_2 = QPushButton(self.full_menu_widget)

        self.error1_button_2.setObjectName(u"error1_button_2")

        self.error1_button_2.setFont(font)

        self.error1_button_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.error1_button_2.setIcon(icon5)

        self.error1_button_2.setIconSize(QSize(14, 14))

        self.error1_button_2.setCheckable(True)

        self.error1_button_2.setAutoExclusive(True)



        self.verticalLayout_2.addWidget(self.error1_button_2)



        self.error2_button_2 = QPushButton(self.full_menu_widget)

        self.error2_button_2.setObjectName(u"error2_button_2")

        self.error2_button_2.setFont(font)

        self.error2_button_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.error2_button_2.setIcon(icon6)

        self.error2_button_2.setIconSize(QSize(14, 14))

        self.error2_button_2.setCheckable(True)

        self.error2_button_2.setAutoExclusive(True)



        self.verticalLayout_2.addWidget(self.error2_button_2)





        self.horizontalLayout_2.addWidget(self.full_menu_widget)



        self.widget_3 = QWidget(self.centralwidget)

        self.widget_3.setObjectName(u"widget_3")

        self.verticalLayout_3 = QVBoxLayout(self.widget_3)

        self.verticalLayout_3.setSpacing(0)

        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.status_bar_widget = QWidget(self.widget_3)

        self.status_bar_widget.setObjectName(u"status_bar_widget")

        self.horizontalLayout = QHBoxLayout(self.status_bar_widget)

        self.horizontalLayout.setSpacing(0)

        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.horizontalLayout.setContentsMargins(5, 6, 5, 5)

        self.temporary_message_label = QLabel(self.status_bar_widget)

        self.temporary_message_label.setObjectName(u"temporary_message_label")

        font1 = QFont()

        font1.setFamilies([u"Segoe UI Emoji"])

        font1.setPointSize(12)

        self.temporary_message_label.setFont(font1)

        self.temporary_message_label.setCursor(QCursor(Qt.ArrowCursor))

        self.temporary_message_label.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.temporary_message_label.setAutoFillBackground(False)



        self.horizontalLayout.addWidget(self.temporary_message_label)



        self.horizontalSpacer = QSpacerItem(377, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)



        self.horizontalLayout.addItem(self.horizontalSpacer)



        self.permanent_message_label = QLabel(self.status_bar_widget)

        self.permanent_message_label.setObjectName(u"permanent_message_label")

        self.permanent_message_label.setFont(font1)



        self.horizontalLayout.addWidget(self.permanent_message_label)





        self.verticalLayout_3.addWidget(self.status_bar_widget)



        self.stackedWidget = QStackedWidget(self.widget_3)

        self.stackedWidget.setObjectName(u"stackedWidget")

        self.stackedWidget.setCursor(QCursor(Qt.ArrowCursor))

        self.page = QWidget()

        self.page.setObjectName(u"page")

        self.horizontalLayout_3 = QHBoxLayout(self.page)

        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.textEdit = QTextEdit(self.page)

        self.textEdit.setObjectName(u"textEdit")

        self.textEdit.setEnabled(True)

        self.textEdit.setReadOnly(True)

        self.textEdit.setTabStopDistance(0.000000000000000)

        self.textEdit.setAcceptRichText(False)

        self.textEdit.setCursorWidth(1)

        self.textEdit.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)



        self.horizontalLayout_3.addWidget(self.textEdit)



        self.serial_box = QGroupBox(self.page)

        self.serial_box.setObjectName(u"serial_box")

        self.serial_box.setEnabled(True)

        font2 = QFont()

        font2.setKerning(True)

        self.serial_box.setFont(font2)

        self.serial_box.setFlat(True)

        self.verticalLayout_5 = QVBoxLayout(self.serial_box)

        self.verticalLayout_5.setObjectName(u"verticalLayout_5")

        self.com_connect_button = QPushButton(self.serial_box)

        self.com_connect_button.setObjectName(u"com_connect_button")

        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        sizePolicy1.setHorizontalStretch(0)

        sizePolicy1.setVerticalStretch(0)

        sizePolicy1.setHeightForWidth(self.com_connect_button.sizePolicy().hasHeightForWidth())

        self.com_connect_button.setSizePolicy(sizePolicy1)

        font3 = QFont()

        font3.setFamilies([u"Segoe UI"])

        font3.setPointSize(11)

        font3.setBold(False)

        font3.setKerning(True)

        self.com_connect_button.setFont(font3)

        self.com_connect_button.setCursor(QCursor(Qt.PointingHandCursor))



        self.verticalLayout_5.addWidget(self.com_connect_button)



        self.com_disconnect_button = QPushButton(self.serial_box)

        self.com_disconnect_button.setObjectName(u"com_disconnect_button")

        self.com_disconnect_button.setEnabled(False)

        sizePolicy1.setHeightForWidth(self.com_disconnect_button.sizePolicy().hasHeightForWidth())

        self.com_disconnect_button.setSizePolicy(sizePolicy1)

        self.com_disconnect_button.setFont(font3)

        self.com_disconnect_button.setCursor(QCursor(Qt.PointingHandCursor))



        self.verticalLayout_5.addWidget(self.com_disconnect_button)



        self.verticalLayout_4 = QVBoxLayout()

        self.verticalLayout_4.setSpacing(0)

        self.verticalLayout_4.setObjectName(u"verticalLayout_4")

        self.label_2 = QLabel(self.serial_box)

        self.label_2.setObjectName(u"label_2")

        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())

        self.label_2.setSizePolicy(sizePolicy)

        font4 = QFont()

        font4.setPointSize(11)

        font4.setKerning(True)

        self.label_2.setFont(font4)



        self.verticalLayout_4.addWidget(self.label_2)



        self.com_available_combo = QComboBox(self.serial_box)

        self.com_available_combo.setObjectName(u"com_available_combo")

        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        sizePolicy2.setHorizontalStretch(10)

        sizePolicy2.setVerticalStretch(10)

        sizePolicy2.setHeightForWidth(self.com_available_combo.sizePolicy().hasHeightForWidth())

        self.com_available_combo.setSizePolicy(sizePolicy2)

        self.com_available_combo.setMinimumSize(QSize(100, 0))

        self.com_available_combo.setMaximumSize(QSize(9999, 16777215))

        font5 = QFont()

        font5.setFamilies([u"Consolas"])

        font5.setPointSize(11)

        font5.setBold(False)

        font5.setKerning(True)

        self.com_available_combo.setFont(font5)

        self.com_available_combo.setCursor(QCursor(Qt.PointingHandCursor))



        self.verticalLayout_4.addWidget(self.com_available_combo)





        self.verticalLayout_5.addLayout(self.verticalLayout_4)



        self.line = QFrame(self.serial_box)

        self.line.setObjectName(u"line")

        self.line.setFrameShape(QFrame.Shape.HLine)

        self.line.setFrameShadow(QFrame.Shadow.Sunken)



        self.verticalLayout_5.addWidget(self.line)



        self.label = QLabel(self.serial_box)

        self.label.setObjectName(u"label")

        self.label.setEnabled(True)

        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())

        self.label.setSizePolicy(sizePolicy)

        self.label.setMinimumSize(QSize(135, 100))

        self.label.setMaximumSize(QSize(135, 100))

        self.label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.label.setPixmap(QPixmap(u":/icon/icon/unibo.png"))

        self.label.setScaledContents(True)

        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)



        self.verticalLayout_5.addWidget(self.label)





        self.horizontalLayout_3.addWidget(self.serial_box)



        self.verticalLayout_7 = QVBoxLayout()

        self.verticalLayout_7.setObjectName(u"verticalLayout_7")



        self.horizontalLayout_3.addLayout(self.verticalLayout_7)



        self.stackedWidget.addWidget(self.page)

        self.page_2 = QWidget()

        self.page_2.setObjectName(u"page_2")

        self.stackedWidget.addWidget(self.page_2)

        self.page_3 = QWidget()

        self.page_3.setObjectName(u"page_3")

        self.stackedWidget.addWidget(self.page_3)

        self.page_4 = QWidget()

        self.page_4.setObjectName(u"page_4")

        self.stackedWidget.addWidget(self.page_4)

        self.page_5 = QWidget()

        self.page_5.setObjectName(u"page_5")

        self.stackedWidget.addWidget(self.page_5)



        self.verticalLayout_3.addWidget(self.stackedWidget)





        self.horizontalLayout_2.addWidget(self.widget_3)



        MainWindow.setCentralWidget(self.centralwidget)



        self.retranslateUi(MainWindow)

        self.menu_button_2.toggled.connect(self.icon_only_widget.setVisible)

        self.menu_button_2.toggled.connect(self.full_menu_widget.setHidden)

        self.menu_button_1.toggled.connect(self.full_menu_widget.setHidden)

        self.menu_button_1.toggled.connect(self.icon_only_widget.setVisible)

        self.menu_button_1.toggled.connect(self.menu_button_2.setChecked)

        self.menu_button_2.toggled.connect(self.menu_button_1.setChecked)

        self.connection_button_1.toggled.connect(self.connection_button_2.setChecked)

        self.connection_button_2.toggled.connect(self.connection_button_1.setChecked)

        self.measurement_button_1.toggled.connect(self.measurement_button_2.setChecked)

        self.measurement_button_2.toggled.connect(self.measurement_button_1.setChecked)

        self.curve_button_1.toggled.connect(self.curve_button_2.setChecked)

        self.curve_button_2.toggled.connect(self.curve_button_1.setChecked)

        self.error1_button_1.toggled.connect(self.error1_button_2.setChecked)

        self.error1_button_2.toggled.connect(self.error1_button_1.setChecked)

        self.error2_button_1.toggled.connect(self.error2_button_2.setChecked)

        self.error2_button_2.toggled.connect(self.error2_button_1.setChecked)



        self.stackedWidget.setCurrentIndex(1)





        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi



    def retranslateUi(self, MainWindow):

        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"GITSIM", None))

        self.menu_button_1.setText("")

        self.connection_button_1.setText("")

        self.measurement_button_1.setText("")

        self.curve_button_1.setText("")

        self.error1_button_1.setText("")

        self.error2_button_1.setText("")

        self.menu_button_2.setText(QCoreApplication.translate("MainWindow", u"Minimize", None))

        self.connection_button_2.setText(QCoreApplication.translate("MainWindow", u"Home", None))

        self.measurement_button_2.setText(QCoreApplication.translate("MainWindow", u"Measurement", None))

        self.curve_button_2.setText(QCoreApplication.translate("MainWindow", u"Curve emulation", None))

        self.error1_button_2.setText(QCoreApplication.translate("MainWindow", u"Error 1", None))

        self.error2_button_2.setText(QCoreApplication.translate("MainWindow", u"Error 2", None))

        self.temporary_message_label.setText(QCoreApplication.translate("MainWindow", u"Messaggio temporaneo", None))

        self.permanent_message_label.setText(QCoreApplication.translate("MainWindow", u"Messaggio permanente", None))

        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"

"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><title>Welcome to GITSIM</title><style type=\"text/css\">\n"

"p, li { white-space: pre-wrap; }\n"

"hr { height: 1px; border-width: 0; }\n"

"li.unchecked::marker { content: \"\\2610\"; }\n"

"li.checked::marker { content: \"\\2612\"; }\n"

"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"

"<h1 style=\" margin-top:18px; margin-bottom:12px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:'Arial','sans-serif'; font-size:xx-large; font-weight:700; color:#2c3e50;\">Welcome to GITSIM</span><span style=\" font-family:'Arial','sans-serif'; font-size:xx-large; font-weight:700; color:#333333;\"> </span></h1>\n"

"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:37px; margin-right:37px; -qt-block-inden"

                        "t:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:'Arial','sans-serif'; color:#333333;\">GITSIM is an ecosystem (board + application) for the emulation of Incremental Encoder signals, commonly used in railway infrastructure. </span></p>\n"

"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:'Arial','sans-serif'; font-size:large; font-weight:700; color:#333333;\">Purpose </span></h3>\n"

"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:'Arial','sans-serif'; color:#333333;\">The primary purpose of GITSIM is to provide a user-friendly interface for engineers, technicians and researchers to: </span></p>\n"

"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"

"<li style=\" font-family:'Arial','sans-se"

                        "rif'; color:#333333;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\">Generate realistic Incremental Encoder signals </li>\n"

"<li style=\" font-family:'Arial','sans-serif'; color:#333333;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\">Simulate various train movement scenarios </li>\n"

"<li style=\" font-family:'Arial','sans-serif'; color:#333333;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\">Test and validate train odometry systems </li></ol>\n"

"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:'Arial','sans-serif'; font-size:large; font-weight:700; color:#333333;\">Key Features </span></h3>\n"

"<ul style=\"margin-"

                        "top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"

"<li style=\" font-family:'Arial','sans-serif'; color:#333333;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-weight:700;\">Scenario Simulation:</span> Pre-programmed and custom scenarios for comprehensive testing </li>\n"

"<li style=\" font-family:'Arial','sans-serif'; color:#333333;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-weight:700;\">Customizable Parameters:</span> Adjust speed, direction, and other signal characteristics </li>\n"

"<li style=\" font-family:'Arial','sans-serif'; color:#333333;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-weight:700;\">Visual Feedback:</span"

                        "> Monitor generated signals through intuitive graphical representations </li>\n"

"<li style=\" font-family:'Arial','sans-serif'; color:#333333;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-weight:700;\">Data Logging:</span> Record and export simulation data for further analysis </li></ul>\n"

"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:'Arial','sans-serif'; font-size:large; font-weight:700; color:#333333;\">Getting Started </span></h3>\n"

"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:'Arial','sans-serif'; color:#333333;\">To begin using GITSIM: </span></p>\n"

"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-"

                        "list-indent: 1;\">\n"

"<li style=\" font-family:'Arial','sans-serif'; color:#333333;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\">Ensure your GITSIM board is properly connected </li>\n"

"<li style=\" font-family:'Arial','sans-serif'; color:#333333;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\">Launch the GITSIM application </li>\n"

"<li style=\" font-family:'Arial','sans-serif'; color:#333333;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\">Establish the application-board connection </li>\n"

"<li style=\" font-family:'Arial','sans-serif'; color:#333333;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\">Configure your simulation parameters </li>\n"

""

                        "<li style=\" font-family:'Arial','sans-serif'; color:#333333;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\">Start the signal generation </li>\n"

"<li style=\" font-family:'Arial','sans-serif'; color:#333333;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\">Monitor and analyze the results </li></ol>\n"

"<hr />\n"

"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:'Arial','sans-serif'; font-style:italic; color:#333333;\">Made by Saimon Collaku</span><span style=\" font-family:'Arial','sans-serif'; color:#333333;\"> </span></p>\n"

"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:'Arial','sans-"

                        "serif'; font-style:italic; color:#333333;\">ARCES - Advanced Research Center on Electronic Systems &quot;Ercole de Castro&quot; of University of Bologna</span></p></body></html>", None))

        self.serial_box.setTitle("")

        self.com_connect_button.setText(QCoreApplication.translate("MainWindow", u"Connect", None))

        self.com_disconnect_button.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Available ports:", None))

        self.label.setText("")

    # retranslateUi



