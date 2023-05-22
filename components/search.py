from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLineEdit, QLabel, QHBoxLayout, QFrame
import qtawesome as qta


class Search(QFrame):
    def __init__(self):
        super(Search, self).__init__()

        input_field = QLineEdit()
        input_field.setPlaceholderText("Type to search")

        input_label = QLabel()
        input_label.setFixedWidth(30)
        input_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_pixmap = qta.icon("ri.search-line", color="teal").pixmap(25)
        input_label.setPixmap(label_pixmap)

        layout = QHBoxLayout(self)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(input_label)
        layout.addWidget(input_field)

        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setMaximumWidth(600)
        self.setObjectName("search")
