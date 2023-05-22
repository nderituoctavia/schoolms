from PySide6.QtGui import QPixmap
from PySide6.QtSql import QSqlTableModel, QSqlDatabase
from PySide6.QtWidgets import QStackedWidget, QWidget, QLineEdit, QLabel, QHBoxLayout, QTableView

import qtawesome as qta

from clc.academics.enrollment.enrollment_form import EnrollmentForm
from clc.academics.enrollment.learners import Learners
from models.student import StudentModel


class Enrollment(QStackedWidget):
    def __init__(self):
        super(Enrollment, self).__init__()
        self.e_form = EnrollmentForm()
        self.learners_view = Learners()
        self.addWidget(self.learners_view)
        self.addWidget(self.e_form)

        self.event_listener()

    def event_listener(self):
        self.learners_view.enroll_btn.clicked.connect(lambda: self.setCurrentIndex(1))
        self.e_form.back_btn.clicked.connect(lambda: self.setCurrentIndex(0))
