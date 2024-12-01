# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'boletasNsblDk.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDateEdit, QFormLayout,
    QGroupBox, QHBoxLayout, QLineEdit, QListView,
    QMainWindow, QMenuBar, QPushButton, QScrollArea,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1015, 817)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalMainLayout = QVBoxLayout()
        self.verticalMainLayout.setObjectName(u"verticalMainLayout")
        self.verticalMainLayout.setContentsMargins(10, 10, 10, 10)
        self.pathHorizontalLayout = QHBoxLayout()
        self.pathHorizontalLayout.setObjectName(u"pathHorizontalLayout")
        self.folderPathLineEdit = QLineEdit(self.centralwidget)
        self.folderPathLineEdit.setObjectName(u"folderPathLineEdit")
        self.folderPathLineEdit.setEnabled(False)

        self.pathHorizontalLayout.addWidget(self.folderPathLineEdit)

        self.folderPathButton = QPushButton(self.centralwidget)
        self.folderPathButton.setObjectName(u"folderPathButton")

        self.pathHorizontalLayout.addWidget(self.folderPathButton)


        self.verticalMainLayout.addLayout(self.pathHorizontalLayout)

        self.pathVerticalLayout = QVBoxLayout()
        self.pathVerticalLayout.setObjectName(u"pathVerticalLayout")
        self.pathVerticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.applyButtonsHorizontalLayout = QHBoxLayout()
        self.applyButtonsHorizontalLayout.setObjectName(u"applyButtonsHorizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.fechaEventoDateEdit = QDateEdit(self.centralwidget)
        self.fechaEventoDateEdit.setObjectName(u"fechaEventoDateEdit")

        self.verticalLayout.addWidget(self.fechaEventoDateEdit)

        self.rutEmpleadorEditText = QLineEdit(self.centralwidget)
        self.rutEmpleadorEditText.setObjectName(u"rutEmpleadorEditText")

        self.verticalLayout.addWidget(self.rutEmpleadorEditText)


        self.applyButtonsHorizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.generateScrapTableButton = QPushButton(self.centralwidget)
        self.generateScrapTableButton.setObjectName(u"generateScrapTableButton")

        self.verticalLayout_2.addWidget(self.generateScrapTableButton)

        self.changeNamesButton = QPushButton(self.centralwidget)
        self.changeNamesButton.setObjectName(u"changeNamesButton")

        self.verticalLayout_2.addWidget(self.changeNamesButton)


        self.applyButtonsHorizontalLayout.addLayout(self.verticalLayout_2)


        self.pathVerticalLayout.addLayout(self.applyButtonsHorizontalLayout)


        self.verticalMainLayout.addLayout(self.pathVerticalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pdfsListView = QListView(self.centralwidget)
        self.pdfsListView.setObjectName(u"pdfsListView")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pdfsListView.sizePolicy().hasHeightForWidth())
        self.pdfsListView.setSizePolicy(sizePolicy)
        self.pdfsListView.setMinimumSize(QSize(250, 0))
        self.pdfsListView.setAutoFillBackground(False)
        self.pdfsListView.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.horizontalLayout_3.addWidget(self.pdfsListView)

        self.pdfImageViewScrollArea = QScrollArea(self.centralwidget)
        self.pdfImageViewScrollArea.setObjectName(u"pdfImageViewScrollArea")
        self.pdfImageViewScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 711, 467))
        self.pdfImageViewScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_3.addWidget(self.pdfImageViewScrollArea)


        self.verticalMainLayout.addLayout(self.horizontalLayout_3)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.groupBox.setMinimumSize(QSize(0, 150))
        self.horizontalLayoutWidget_4 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(10, 29, 961, 111))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayoutLeft = QFormLayout()
        self.formLayoutLeft.setObjectName(u"formLayoutLeft")
        self.formLayoutLeft.setLabelAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.formLayoutLeft.setFormAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addLayout(self.formLayoutLeft)

        self.formLayoutRight = QFormLayout()
        self.formLayoutRight.setObjectName(u"formLayoutRight")
        self.formLayoutRight.setFormAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addLayout(self.formLayoutRight)


        self.verticalMainLayout.addWidget(self.groupBox)


        self.horizontalLayout.addLayout(self.verticalMainLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1015, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(statustip)
        self.folderPathLineEdit.setStatusTip(QCoreApplication.translate("MainWindow", u"Path de los archivos PDFs", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.folderPathButton.setStatusTip(QCoreApplication.translate("MainWindow", u"Seleccione carpeta con los archivos PDFs", None))
#endif // QT_CONFIG(statustip)
        self.folderPathButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.fechaEventoDateEdit.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.fechaEventoDateEdit.setStatusTip(QCoreApplication.translate("MainWindow", u"Inserte fecha del evento", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.rutEmpleadorEditText.setStatusTip(QCoreApplication.translate("MainWindow", u"Inserte RUT del empleador", None))
#endif // QT_CONFIG(statustip)
        self.rutEmpleadorEditText.setInputMask(QCoreApplication.translate("MainWindow", u"99.999.999-9", None))
        self.rutEmpleadorEditText.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Inserte RUT del empleador...", None))
        self.generateScrapTableButton.setText(QCoreApplication.translate("MainWindow", u"Genera CSV con los datos de las boletas", None))
        self.changeNamesButton.setText(QCoreApplication.translate("MainWindow", u"Renombrar PDFs por nombre persona", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Datos del PDF leidos con python", None))
    # retranslateUi

