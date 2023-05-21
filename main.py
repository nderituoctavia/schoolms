import sys

from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtWidgets import QStackedWidget, QHBoxLayout, QVBoxLayout, QWidget, QLabel, \
    QToolBar, QApplication, QMainWindow

import qtawesome as qta

from clc.academics.enrollment.enrollment import Enrollment
from clc.academics.enrollment.enrollment_form import EnrollmentForm


class CentralWidget(QWidget):
    def __init__(self):
        super(CentralWidget, self).__init__()

        layout = QVBoxLayout(self)

        self.page_title = QLabel()
        self.page_title.setObjectName("title")
        self.page_title.setFont(QFont("Arial Mt", 16))

        self.page_footer = QLabel("Created by Octavia for St Cecilia Community Learning Center @ 2023")
        self.page_footer.setFont(QFont("Arial mt", 9))
        self.page_footer.setObjectName("footer")
        self.page_footer.setFixedHeight(30)
        self.page_footer.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.page_icon = QPixmap(qta.icon("fa.user").pixmap(40))
        self.page_icon_lbl = QLabel()
        self.page_icon_lbl.setFixedSize(40, 40)
        self.page_icon_lbl.setPixmap(self.page_icon)

        self.page_header = QWidget()
        self.page_header.setObjectName("header")
        header_layout = QHBoxLayout(self.page_header)
        header_layout.addWidget(self.page_icon_lbl)
        header_layout.addWidget(self.page_title)

        self.content_area = QStackedWidget()
        self.content_area.setObjectName("content")

        pages = [QLabel('Dashboards'), Enrollment(), QLabel('Academics'), QLabel('Medical'), QLabel('Finance'),
                 QLabel('Inventory'), QLabel('Library'), QLabel('Calendar'), QLabel('Addresses'), QLabel('Reports')]

        for page in pages:
            self.content_area.addWidget(page)

        layout.addWidget(self.page_header)
        layout.addWidget(self.content_area)
        layout.addWidget(self.page_footer)

        layout.setAlignment(Qt.AlignLeft)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setStyleSheet(
            """
				#content { background: #fff; border-top: 1px solid #dfdfdf; } 
				#footer { color: teal;border-top: 1px solid #dfdfdf; }
				#header QLabel { color: #0f93b8; } 
			""")


class Menu(QToolBar):
    def __init__(self, parent):
        super(Menu, self).__init__(parent)

        self.setMovable(False)
        self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.actionTriggered.connect(self.set_active_page)

        self.setFixedWidth(180)
        self.setIconSize(QSize(45, 30))

        self.logo_lbl = QLabel()
        self.logo_lbl.setContentsMargins(30, 0, 30, 30)
        self.logo_lbl.setScaledContents(True)
        self.logo_lbl.setFixedHeight(160)
        self.logo_lbl.setPixmap(QPixmap("resources/images/logo.png"))
        self.addWidget(self.logo_lbl)

        menu_actions = {
            'Dashboard': 'ph.windows-logo',
            'Enrollment': 'ph.user-list',
            'Academics': 'ph.student',
            'Medical': 'ph.first-aid-kit',
            'Finance': 'ph.currency-circle-dollar',
            'Inventory': 'ph.book-bookmark',
            'Library': 'ph.books',
            'Calendar': 'ph.calendar',
            'Address': 'ph.address-book',
            'Reports': 'ph.chart-line-up'
        }

        for action in menu_actions:
            self.addAction(qta.icon(menu_actions[action], color="turquoise"), action)

        actions = self.actions()
        actions[1].trigger()
        self.widgetForAction(actions[1]).setStyleSheet("""
            color: #0f93b8;
            background: #fefefe;
            border: 1px solid silver;
            border-radius: 5px;
        """)
        for action in actions:
            self.widgetForAction(action).setFixedWidth(180)


    def set_active_page(self, action):
        self.parent().central_widget.page_title.setText(action.text())
        self.parent().central_widget.page_icon_lbl.setPixmap(action.icon().pixmap(40))
        for q in self.actions():
            self.widgetForAction(q).setStyleSheet("""
                color: #caf0f8;
                background-color: transparent;
            """)
        self.widgetForAction(action).setStyleSheet("""
            color: #0f93b8;
            background: #fefefe;
            border: 1px solid silver;
            border-radius: 5px;
        """)
        index = self.actions().index(action)
        self.parent().central_widget.content_area.setCurrentIndex(index - 1)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("ST CECILIA COMMUNITY LEARNING CENTRE")

        self.central_widget = CentralWidget()
        self.setCentralWidget(self.central_widget)

        self.menu = Menu(self)
        self.addToolBar(Qt.ToolBarArea.LeftToolBarArea, self.menu)

        with open('resources/stylesheets/styles.qss') as stylesheet:
            self.setStyleSheet(stylesheet.read())


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.resize(1280, 768)
    window.show()
    sys.exit(app.exec())
