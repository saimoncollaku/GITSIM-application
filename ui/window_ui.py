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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDoubleSpinBox,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QSpinBox, QStackedWidget,
    QTextEdit, QVBoxLayout, QWidget)

from ui.gaugemeter import GaugeMeter
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
        self.full_menu_widget.setStyleSheet(u"")
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
        font2 = QFont()
        font2.setPointSize(10)
        self.stackedWidget.setFont(font2)
        self.stackedWidget.setCursor(QCursor(Qt.ArrowCursor))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout_3 = QHBoxLayout(self.page)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.textEdit = QTextEdit(self.page)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy1)
        self.textEdit.setReadOnly(True)
        self.textEdit.setTabStopDistance(0.000000000000000)
        self.textEdit.setAcceptRichText(False)
        self.textEdit.setCursorWidth(1)
        self.textEdit.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.horizontalLayout_3.addWidget(self.textEdit)

        self.serial_box = QGroupBox(self.page)
        self.serial_box.setObjectName(u"serial_box")
        self.serial_box.setEnabled(True)
        font3 = QFont()
        font3.setPointSize(10)
        font3.setKerning(True)
        self.serial_box.setFont(font3)
        self.serial_box.setFlat(False)
        self.verticalLayout_5 = QVBoxLayout(self.serial_box)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_9 = QLabel(self.serial_box)
        self.label_9.setObjectName(u"label_9")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setKerning(True)
        self.label_9.setFont(font4)
        self.label_9.setStyleSheet(u"		background-color:#bb2e29;\n"
"		color: #fff;")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_9.setMargin(2)

        self.verticalLayout_5.addWidget(self.label_9)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.serial_box)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font5 = QFont()
        font5.setPointSize(11)
        font5.setKerning(True)
        self.label_2.setFont(font5)

        self.verticalLayout_4.addWidget(self.label_2)

        self.com_available_combo = QComboBox(self.serial_box)
        self.com_available_combo.setObjectName(u"com_available_combo")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(10)
        sizePolicy3.setVerticalStretch(10)
        sizePolicy3.setHeightForWidth(self.com_available_combo.sizePolicy().hasHeightForWidth())
        self.com_available_combo.setSizePolicy(sizePolicy3)
        self.com_available_combo.setMinimumSize(QSize(100, 0))
        self.com_available_combo.setMaximumSize(QSize(9999, 16777215))
        font6 = QFont()
        font6.setFamilies([u"Consolas"])
        font6.setPointSize(11)
        font6.setBold(False)
        font6.setKerning(True)
        self.com_available_combo.setFont(font6)
        self.com_available_combo.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.com_available_combo)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.label_13 = QLabel(self.serial_box)
        self.label_13.setObjectName(u"label_13")
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMinimumSize(QSize(200, 40))
        self.label_13.setMaximumSize(QSize(200, 40))
        self.label_13.setFont(font5)
        self.label_13.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.label_13)

        self.com_connect_button = QPushButton(self.serial_box)
        self.com_connect_button.setObjectName(u"com_connect_button")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.com_connect_button.sizePolicy().hasHeightForWidth())
        self.com_connect_button.setSizePolicy(sizePolicy4)
        font7 = QFont()
        font7.setFamilies([u"Segoe UI"])
        font7.setPointSize(11)
        font7.setBold(False)
        font7.setKerning(True)
        self.com_connect_button.setFont(font7)
        self.com_connect_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.com_connect_button)

        self.com_disconnect_button = QPushButton(self.serial_box)
        self.com_disconnect_button.setObjectName(u"com_disconnect_button")
        self.com_disconnect_button.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.com_disconnect_button.sizePolicy().hasHeightForWidth())
        self.com_disconnect_button.setSizePolicy(sizePolicy4)
        self.com_disconnect_button.setFont(font7)
        self.com_disconnect_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.com_disconnect_button)

        self.line_2 = QFrame(self.serial_box)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_5.addWidget(self.line_2)

        self.label_12 = QLabel(self.serial_box)
        self.label_12.setObjectName(u"label_12")
        sizePolicy2.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy2)
        self.label_12.setFont(font4)
        self.label_12.setStyleSheet(u"		background-color:#bb2e29;\n"
"		color: #fff;")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_12.setMargin(2)

        self.verticalLayout_5.addWidget(self.label_12)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(1)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_5 = QLabel(self.serial_box)
        self.label_5.setObjectName(u"label_5")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy5)
        self.label_5.setFont(font5)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.label_5.setWordWrap(False)

        self.verticalLayout_10.addWidget(self.label_5)

        self.ppr1_spinbox = QSpinBox(self.serial_box)
        self.ppr1_spinbox.setObjectName(u"ppr1_spinbox")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.ppr1_spinbox.sizePolicy().hasHeightForWidth())
        self.ppr1_spinbox.setSizePolicy(sizePolicy6)
        font8 = QFont()
        font8.setFamilies([u"Cascadia Code"])
        font8.setPointSize(10)
        font8.setKerning(True)
        self.ppr1_spinbox.setFont(font8)
        self.ppr1_spinbox.setCursor(QCursor(Qt.IBeamCursor))
        self.ppr1_spinbox.setToolTipDuration(2)
        self.ppr1_spinbox.setWrapping(False)
        self.ppr1_spinbox.setFrame(True)
        self.ppr1_spinbox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.ppr1_spinbox.setCorrectionMode(QAbstractSpinBox.CorrectionMode.CorrectToNearestValue)
        self.ppr1_spinbox.setMinimum(80)
        self.ppr1_spinbox.setMaximum(128)
        self.ppr1_spinbox.setValue(128)
        self.ppr1_spinbox.setDisplayIntegerBase(10)

        self.verticalLayout_10.addWidget(self.ppr1_spinbox)


        self.verticalLayout_5.addLayout(self.verticalLayout_10)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(1)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_10 = QLabel(self.serial_box)
        self.label_10.setObjectName(u"label_10")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy7)
        self.label_10.setFont(font5)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.verticalLayout_9.addWidget(self.label_10)

        self.ppr2_spinbox = QSpinBox(self.serial_box)
        self.ppr2_spinbox.setObjectName(u"ppr2_spinbox")
        sizePolicy6.setHeightForWidth(self.ppr2_spinbox.sizePolicy().hasHeightForWidth())
        self.ppr2_spinbox.setSizePolicy(sizePolicy6)
        self.ppr2_spinbox.setFont(font8)
        self.ppr2_spinbox.setCursor(QCursor(Qt.IBeamCursor))
        self.ppr2_spinbox.setToolTipDuration(2)
        self.ppr2_spinbox.setWrapping(False)
        self.ppr2_spinbox.setFrame(True)
        self.ppr2_spinbox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.ppr2_spinbox.setCorrectionMode(QAbstractSpinBox.CorrectionMode.CorrectToNearestValue)
        self.ppr2_spinbox.setMinimum(80)
        self.ppr2_spinbox.setMaximum(128)
        self.ppr2_spinbox.setValue(128)
        self.ppr2_spinbox.setDisplayIntegerBase(10)

        self.verticalLayout_9.addWidget(self.ppr2_spinbox)


        self.verticalLayout_5.addLayout(self.verticalLayout_9)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(1)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_11 = QLabel(self.serial_box)
        self.label_11.setObjectName(u"label_11")
        sizePolicy7.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy7)
        self.label_11.setFont(font5)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.verticalLayout_7.addWidget(self.label_11)

        self.diameter_spinbox = QDoubleSpinBox(self.serial_box)
        self.diameter_spinbox.setObjectName(u"diameter_spinbox")
        sizePolicy6.setHeightForWidth(self.diameter_spinbox.sizePolicy().hasHeightForWidth())
        self.diameter_spinbox.setSizePolicy(sizePolicy6)
        self.diameter_spinbox.setFont(font8)
        self.diameter_spinbox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.diameter_spinbox.setCorrectionMode(QAbstractSpinBox.CorrectionMode.CorrectToNearestValue)
        self.diameter_spinbox.setDecimals(3)
        self.diameter_spinbox.setMinimum(0.800000000000000)
        self.diameter_spinbox.setMaximum(1.250000000000000)
        self.diameter_spinbox.setValue(1.000000000000000)

        self.verticalLayout_7.addWidget(self.diameter_spinbox)


        self.verticalLayout_5.addLayout(self.verticalLayout_7)


        self.horizontalLayout_3.addWidget(self.serial_box)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout = QGridLayout(self.page_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.data_encoder1_title = QLabel(self.page_2)
        self.data_encoder1_title.setObjectName(u"data_encoder1_title")
        sizePolicy2.setHeightForWidth(self.data_encoder1_title.sizePolicy().hasHeightForWidth())
        self.data_encoder1_title.setSizePolicy(sizePolicy2)
        font9 = QFont()
        font9.setPointSize(12)
        font9.setBold(True)
        self.data_encoder1_title.setFont(font9)
        self.data_encoder1_title.setAutoFillBackground(False)
        self.data_encoder1_title.setStyleSheet(u"		background-color:#bb2e29;\n"
"		color: #fff;")
        self.data_encoder1_title.setFrameShape(QFrame.Shape.NoFrame)
        self.data_encoder1_title.setFrameShadow(QFrame.Shadow.Plain)
        self.data_encoder1_title.setMidLineWidth(0)
        self.data_encoder1_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.data_encoder1_title.setMargin(2)
        self.data_encoder1_title.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout_6.addWidget(self.data_encoder1_title)

        self.gauge_meter_1 = GaugeMeter(self.page_2)
        self.gauge_meter_1.setObjectName(u"gauge_meter_1")

        self.verticalLayout_6.addWidget(self.gauge_meter_1)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(-1, -1, -1, 6)
        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy8)
        font10 = QFont()
        font10.setPointSize(11)
        self.label_4.setFont(font10)
        self.label_4.setMargin(14)

        self.horizontalLayout_17.addWidget(self.label_4)

        self.distance_encoder1_label = QLabel(self.page_2)
        self.distance_encoder1_label.setObjectName(u"distance_encoder1_label")
        sizePolicy8.setHeightForWidth(self.distance_encoder1_label.sizePolicy().hasHeightForWidth())
        self.distance_encoder1_label.setSizePolicy(sizePolicy8)
        font11 = QFont()
        font11.setFamilies([u"7-Segment"])
        font11.setPointSize(23)
        font11.setItalic(False)
        self.distance_encoder1_label.setFont(font11)
        self.distance_encoder1_label.setStyleSheet(u"QLabel {\n"
"        border: 1px solid black;\n"
"        border-radius: 5px;\n"
"        padding: 5px;\n"
"}\n"
"")
        self.distance_encoder1_label.setMargin(1)

        self.horizontalLayout_17.addWidget(self.distance_encoder1_label)


        self.verticalLayout_6.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_14 = QLabel(self.page_2)
        self.label_14.setObjectName(u"label_14")
        sizePolicy8.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy8)
        self.label_14.setFont(font10)
        self.label_14.setMargin(14)

        self.horizontalLayout_19.addWidget(self.label_14)

        self.pulses_encoder1_label = QLabel(self.page_2)
        self.pulses_encoder1_label.setObjectName(u"pulses_encoder1_label")
        sizePolicy8.setHeightForWidth(self.pulses_encoder1_label.sizePolicy().hasHeightForWidth())
        self.pulses_encoder1_label.setSizePolicy(sizePolicy8)
        self.pulses_encoder1_label.setFont(font11)
        self.pulses_encoder1_label.setStyleSheet(u"QLabel {\n"
"        border: 1px solid black;\n"
"        border-radius: 5px;\n"
"        padding: 5px;\n"
"}\n"
"")
        self.pulses_encoder1_label.setFrameShape(QFrame.Shape.NoFrame)
        self.pulses_encoder1_label.setFrameShadow(QFrame.Shadow.Plain)
        self.pulses_encoder1_label.setLineWidth(1)
        self.pulses_encoder1_label.setMargin(1)

        self.horizontalLayout_19.addWidget(self.pulses_encoder1_label)


        self.verticalLayout_6.addLayout(self.horizontalLayout_19)


        self.horizontalLayout_8.addLayout(self.verticalLayout_6)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.data_encoder1_title_3 = QLabel(self.page_2)
        self.data_encoder1_title_3.setObjectName(u"data_encoder1_title_3")
        sizePolicy2.setHeightForWidth(self.data_encoder1_title_3.sizePolicy().hasHeightForWidth())
        self.data_encoder1_title_3.setSizePolicy(sizePolicy2)
        self.data_encoder1_title_3.setFont(font9)
        self.data_encoder1_title_3.setAutoFillBackground(False)
        self.data_encoder1_title_3.setStyleSheet(u"		background-color:#bb2e29;\n"
"		color: #fff;")
        self.data_encoder1_title_3.setFrameShape(QFrame.Shape.NoFrame)
        self.data_encoder1_title_3.setFrameShadow(QFrame.Shadow.Plain)
        self.data_encoder1_title_3.setMidLineWidth(0)
        self.data_encoder1_title_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.data_encoder1_title_3.setMargin(2)
        self.data_encoder1_title_3.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout_11.addWidget(self.data_encoder1_title_3)

        self.gauge_meter_2 = GaugeMeter(self.page_2)
        self.gauge_meter_2.setObjectName(u"gauge_meter_2")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.gauge_meter_2.sizePolicy().hasHeightForWidth())
        self.gauge_meter_2.setSizePolicy(sizePolicy9)

        self.verticalLayout_11.addWidget(self.gauge_meter_2)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(-1, -1, -1, 6)
        self.label_18 = QLabel(self.page_2)
        self.label_18.setObjectName(u"label_18")
        sizePolicy8.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy8)
        self.label_18.setFont(font10)
        self.label_18.setMargin(14)

        self.horizontalLayout_18.addWidget(self.label_18)

        self.distance_encoder2_label = QLabel(self.page_2)
        self.distance_encoder2_label.setObjectName(u"distance_encoder2_label")
        sizePolicy8.setHeightForWidth(self.distance_encoder2_label.sizePolicy().hasHeightForWidth())
        self.distance_encoder2_label.setSizePolicy(sizePolicy8)
        self.distance_encoder2_label.setFont(font11)
        self.distance_encoder2_label.setStyleSheet(u"QLabel {\n"
"        border: 1px solid black;\n"
"        border-radius: 5px;\n"
"        padding: 5px;\n"
"}\n"
"")
        self.distance_encoder2_label.setMargin(1)

        self.horizontalLayout_18.addWidget(self.distance_encoder2_label)


        self.verticalLayout_11.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_15 = QLabel(self.page_2)
        self.label_15.setObjectName(u"label_15")
        sizePolicy8.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy8)
        self.label_15.setFont(font10)
        self.label_15.setMargin(14)

        self.horizontalLayout_20.addWidget(self.label_15)

        self.pulses_encoder2_label = QLabel(self.page_2)
        self.pulses_encoder2_label.setObjectName(u"pulses_encoder2_label")
        sizePolicy8.setHeightForWidth(self.pulses_encoder2_label.sizePolicy().hasHeightForWidth())
        self.pulses_encoder2_label.setSizePolicy(sizePolicy8)
        font12 = QFont()
        font12.setFamilies([u"7-Segment"])
        font12.setPointSize(23)
        font12.setItalic(False)
        font12.setStrikeOut(False)
        self.pulses_encoder2_label.setFont(font12)
        self.pulses_encoder2_label.setStyleSheet(u"QLabel {\n"
"        border: 1px solid black;\n"
"        border-radius: 5px;\n"
"        padding: 5px;\n"
"}\n"
"")
        self.pulses_encoder2_label.setMargin(1)

        self.horizontalLayout_20.addWidget(self.pulses_encoder2_label)


        self.verticalLayout_11.addLayout(self.horizontalLayout_20)


        self.horizontalLayout_8.addLayout(self.verticalLayout_11)


        self.gridLayout.addLayout(self.horizontalLayout_8, 0, 0, 1, 2)

        self.line_5 = QFrame(self.page_2)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setStyleSheet(u"color: #0066a4;")
        self.line_5.setFrameShadow(QFrame.Shadow.Plain)
        self.line_5.setLineWidth(2)
        self.line_5.setMidLineWidth(1)
        self.line_5.setFrameShape(QFrame.Shape.HLine)

        self.gridLayout.addWidget(self.line_5, 1, 0, 1, 2)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label = QLabel(self.page_2)
        self.label.setObjectName(u"label")
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setMinimumSize(QSize(0, 26))
        self.label.setMaximumSize(QSize(16777215, 26))
        self.label.setFont(font9)
        self.label.setStyleSheet(u"		background-color:#bb2e29;\n"
"		color: #fff;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_15.addWidget(self.label)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_7 = QLabel(self.page_2)
        self.label_7.setObjectName(u"label_7")
        sizePolicy8.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy8)
        self.label_7.setFont(font10)
        self.label_7.setWordWrap(True)

        self.verticalLayout_17.addWidget(self.label_7)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.radioButton_3 = QRadioButton(self.page_2)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setFont(font10)

        self.horizontalLayout_9.addWidget(self.radioButton_3)

        self.radioButton_2 = QRadioButton(self.page_2)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setFont(font10)

        self.horizontalLayout_9.addWidget(self.radioButton_2)

        self.radioButton = QRadioButton(self.page_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setFont(font10)

        self.horizontalLayout_9.addWidget(self.radioButton)


        self.verticalLayout_17.addLayout(self.horizontalLayout_9)


        self.horizontalLayout_5.addLayout(self.verticalLayout_17)

        self.line = QFrame(self.page_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_5.addWidget(self.line)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(8)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_8 = QLabel(self.page_2)
        self.label_8.setObjectName(u"label_8")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy10)
        self.label_8.setFont(font10)
        self.label_8.setWordWrap(True)

        self.verticalLayout_16.addWidget(self.label_8)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy5.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy5)
        font13 = QFont()
        font13.setFamilies([u"Segoe UI"])
        font13.setPointSize(11)
        self.label_3.setFont(font13)

        self.horizontalLayout_6.addWidget(self.label_3)

        self.doubleSpinBox = QDoubleSpinBox(self.page_2)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox.setSizePolicy(sizePolicy2)
        font14 = QFont()
        font14.setFamilies([u"Cascadia Code"])
        font14.setPointSize(10)
        self.doubleSpinBox.setFont(font14)
        self.doubleSpinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)

        self.horizontalLayout_6.addWidget(self.doubleSpinBox)

        self.pushButton = QPushButton(self.page_2)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setFont(font13)

        self.horizontalLayout_6.addWidget(self.pushButton)


        self.verticalLayout_16.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, -1, -1, 5)
        self.label_6 = QLabel(self.page_2)
        self.label_6.setObjectName(u"label_6")
        sizePolicy5.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy5)
        self.label_6.setFont(font10)

        self.horizontalLayout_7.addWidget(self.label_6)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.page_2)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_2.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_2.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_2.setFont(font14)
        self.doubleSpinBox_2.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)

        self.horizontalLayout_7.addWidget(self.doubleSpinBox_2)

        self.pushButton_2 = QPushButton(self.page_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setFont(font10)

        self.horizontalLayout_7.addWidget(self.pushButton_2)


        self.verticalLayout_16.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_5.addLayout(self.verticalLayout_16)


        self.verticalLayout_15.addLayout(self.horizontalLayout_5)


        self.gridLayout.addLayout(self.verticalLayout_15, 2, 0, 1, 2)

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
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<h1 style=\" margin-top:18px; margin-bottom:12px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:'Arial','sans-serif'; font-size:9pt; font-weight:700; color:#2c3e50;\">Welcome to GITSIM</span><span style=\" font-family:'Arial','sans-serif'; font-size:9pt; font-weight:700; color:#333333;\"> </span></h1>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text"
                        "-indent:0px; line-height:150%;\"><span style=\" font-family:'Arial','sans-serif'; font-size:9pt; color:#333333;\">GITSIM is an ecosystem (board + application) for the emulation of Incremental Encoder signals, commonly used in railway infrastructure. </span></p>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:'Arial','sans-serif'; font-size:9pt; font-weight:700; color:#333333;\">Purpose </span></h3>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:'Arial','sans-serif'; font-size:9pt; color:#333333;\">The primary purpose of GITSIM is to provide a user-friendly interface for engineers, technicians and researchers to: </span></p>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" font-fami"
                        "ly:'Arial','sans-serif'; font-size:9pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\">Generate realistic Incremental Encoder signals </li>\n"
"<li style=\" font-family:'Arial','sans-serif'; font-size:9pt; color:#333333;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\">Simulate various train movement scenarios </li>\n"
"<li style=\" font-family:'Arial','sans-serif'; font-size:9pt; color:#333333;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\">Test and validate train odometry systems </li></ol>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:'Arial','sans-serif'; font-size:9pt; font-weight:700; colo"
                        "r:#333333;\">Key Features </span></h3>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" font-family:'Arial','sans-serif'; font-size:9pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-weight:700;\">Scenario Simulation:</span> Pre-programmed and custom scenarios for comprehensive testing </li>\n"
"<li style=\" font-family:'Arial','sans-serif'; font-size:9pt; color:#333333;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-weight:700;\">Customizable Parameters:</span> Adjust speed, direction, and other signal characteristics </li>\n"
"<li style=\" font-family:'Arial','sans-serif'; font-size:9pt; color:#333333;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:37px; margin-right:37px; -qt-bl"
                        "ock-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-weight:700;\">Visual Feedback:</span> Monitor generated signals through intuitive graphical representations </li>\n"
"<li style=\" font-family:'Arial','sans-serif'; font-size:9pt; color:#333333;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-weight:700;\">Data Logging:</span> Record and export simulation data for further analysis </li></ul>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:'Arial','sans-serif'; font-size:9pt; font-weight:700; color:#333333;\">Getting Started </span></h3>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:'Arial','sans-serif'; font-size:9pt; color:#3333"
                        "33;\">To begin using GITSIM: </span></p>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" font-family:'Arial','sans-serif'; font-size:9pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\">Ensure your GITSIM board is properly connected </li>\n"
"<li style=\" font-family:'Arial','sans-serif'; font-size:9pt; color:#333333;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\">Launch the GITSIM application </li>\n"
"<li style=\" font-family:'Arial','sans-serif'; font-size:9pt; color:#333333;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\">Establish the application-board connection </li>\n"
"<li style=\" font-family:'Arial','sans-serif'; font-size:9pt; col"
                        "or:#333333;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\">Configure your simulation parameters </li>\n"
"<li style=\" font-family:'Arial','sans-serif'; font-size:9pt; color:#333333;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\">Start the signal generation </li>\n"
"<li style=\" font-family:'Arial','sans-serif'; font-size:9pt; color:#333333;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\">Monitor and analyze the results </li></ol>\n"
"<hr />\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:'Arial','sans-serif'; font-size:9pt; font-style:italic; color:#333333;\">Made by Saimon Collaku</span><span style=\" font-fam"
                        "ily:'Arial','sans-serif'; font-size:9pt; color:#333333;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:'Arial','sans-serif'; font-size:9pt; font-style:italic; color:#333333;\">ARCES - Advanced Research Center on Electronic Systems &quot;Ercole de Castro&quot; of University of Bologna</span></p></body></html>", None))
        self.serial_box.setTitle("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Select serial port", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Available ports:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Connect to the chosen port  with the constants set below.", None))
        self.com_connect_button.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.com_disconnect_button.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Set constants ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"PPR setting for Encoder 1 ", None))
#if QT_CONFIG(tooltip)
        self.ppr1_spinbox.setToolTip(QCoreApplication.translate("MainWindow", u"Acceptable values range: 80 \u00f7 128", None))
#endif // QT_CONFIG(tooltip)
        self.ppr1_spinbox.setSpecialValueText("")
        self.ppr1_spinbox.setPrefix("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"PPR setting for Encoder 2 ", None))
#if QT_CONFIG(tooltip)
        self.ppr2_spinbox.setToolTip(QCoreApplication.translate("MainWindow", u"Acceptable values range: 80 \u00f7 128", None))
#endif // QT_CONFIG(tooltip)
        self.ppr2_spinbox.setSpecialValueText("")
        self.ppr2_spinbox.setPrefix("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Wheel diameter [m] ", None))
        self.data_encoder1_title.setText(QCoreApplication.translate("MainWindow", u"Encoder 1 measurement", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Distance [m]:", None))
        self.distance_encoder1_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Pulses [x4]:", None))
        self.pulses_encoder1_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.data_encoder1_title_3.setText(QCoreApplication.translate("MainWindow", u"Encoder 2 measurement", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Distance [m]:", None))
        self.distance_encoder2_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Pulses [x4]:", None))
        self.pulses_encoder2_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Set single kinematic values", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Choose to which Encoder you wish to assign the value: ", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Both", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Choose the value you want to set:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Speed [m/s]: ", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Acceleration [m/s<span style=\" vertical-align:super;\">2</span>]: </p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Set", None))
    # retranslateUi

