from PySide6.QtWidgets import QWidget, QLineEdit, QLabel, QHBoxLayout

import qtawesome as qta


class Search(QWidget):
    def __init__(self):
        super(Search, self).__init__()

        input_field = QLineEdit()
        input_field.setPlaceholderText("Type to search")

        input_label = QLabel()
        label_pixmap = qta.icon("ri.search-line", color="teal").pixmap(30)
        input_label.setPixmap(label_pixmap)
        layout = QHBoxLayout(self)
        layout.addWidget(input_label)
        layout.addWidget(input_field)

