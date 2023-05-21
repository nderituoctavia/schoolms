from PySide6.QtGui import QPixmap
from PySide6.QtSql import QSqlTableModel, QSqlDatabase
from PySide6.QtWidgets import QStackedWidget, QWidget, QLineEdit, QLabel, QHBoxLayout, QTableView

import qtawesome as qta

from models.student import StudentModel


class Enrollment(QStackedWidget):
    def __init__(self):
        super(Enrollment, self).__init__()

        learners_model = StudentModel()
        learners_table = QTableView()
        learners_table.setModel(learners_model)

        self.addWidget(learners_table)
