from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableView, QHBoxLayout, QComboBox, QPushButton, QLabel, QSpacerItem

from components.search import Search
from models.student import StudentModel

import qtawesome as qta


class Learners(QWidget):
    def __init__(self):
        super(Learners, self).__init__()

        layout = QVBoxLayout(self)
        search = Search()

        learners_model = StudentModel()
        learners_table = QTableView()
        learners_table.setModel(learners_model)

        self.grade_combo = QComboBox()
        self.grade_combo.addItems(['Play Group',
                                   'PP1',
                                   'PP2',
                                   'Grade 1',
                                   'Grade 2',
                                   'Grade 3',
                                   'Grade 4',
                                   'Grade 5',
                                   'Grade 6',
                                   'Grade 7',
                                   'Grade 8',
                                   'Grade 9'])

        self.grade_combo.currentIndexChanged.connect(print)
        self.border_combo = QComboBox()
        self.border_combo.addItems(['border', 'day scholar', 'day scholar - transport'])

        header_layout = QHBoxLayout()
        header_layout.addWidget(search)
        # header_layout.addStretch(2)
        header_layout.addItem(QSpacerItem(120, 20))
        header_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header_layout.addWidget(self.grade_combo)

        self.enroll_btn = QPushButton(qta.icon('ph.plus', color='green'), "Enroll")
        self.enroll_btn.setIconSize(QSize(27, 27))
        self.download_btn = QPushButton(qta.icon('ph.download', color='grey'), "")
        self.download_btn.setIconSize(QSize(27, 27))
        self.print_btn = QPushButton(qta.icon('ph.printer', color='blue'), "")
        self.print_btn.setIconSize(QSize(27, 27))
        self.transfer_btn = QPushButton(qta.icon('fa5s.people-arrows', color='skyblue'), "")
        self.transfer_btn.setIconSize(QSize(27, 27))

        actions_layout = QHBoxLayout()
        # actions_layout.addWidget(self.grade_combo)
        actions_layout.addStretch()
        actions_layout.addWidget(self.enroll_btn)
        actions_layout.addWidget(self.download_btn)
        actions_layout.addWidget(self.print_btn)
        actions_layout.addWidget(self.transfer_btn)

        layout.addLayout(header_layout)
        layout.addLayout(actions_layout)
        layout.addWidget(learners_table)

