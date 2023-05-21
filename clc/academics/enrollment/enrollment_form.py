"""
This module provides a students enrollment form. It Provides a user-friendly interface where learners can be
registered and all basic information collected.
************** Students Enrollment Information
**************************
*** Bio information
*** Parent / Guardian information
*** Medical information
*** Religious information
"""
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QGridLayout, QTabWidget, QLabel, QFormLayout, QHBoxLayout, QLineEdit, \
    QComboBox, QDateEdit, QGroupBox, QRadioButton, QButtonGroup, QVBoxLayout

from clc.share.search import Search


class FormInput(QWidget):
    def __init__(self, label, input_field):
        super(FormInput, self).__init__()

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel(label))
        layout.addWidget(input_field)


class BiodataForm(QWidget):
    def __init__(self):
        super(BiodataForm, self).__init__()

        self.name_lineedit = QLineEdit()
        self.dob_date_edit = QDateEdit()
        self.adm_date_edit = QDateEdit()
        self.adm_grade_combo = QComboBox()
        self.adm_no_edit = QLineEdit()

        self.gender_group_box = QGroupBox("Gender")
        gb_layout = QHBoxLayout(self.gender_group_box)
        self.male = QRadioButton("Male")
        self.female = QRadioButton("Female")
        self.other = QRadioButton("Other")

        gb_layout.addWidget(self.male)
        gb_layout.addWidget(self.female)
        gb_layout.addWidget(self.other)

        self.gender_btn_group = QButtonGroup(self.gender_group_box)
        self.gender_btn_group.addButton(self.male)
        self.gender_btn_group.addButton(self.female)
        self.gender_btn_group.addButton(self.other)

        row_1 = QHBoxLayout()
        row_1.addWidget(self.gender_group_box)
        row_1.addWidget(FormInput("Date of birth", self.dob_date_edit))

        layout = QFormLayout(self)
        layout.addRow("Fullname", Search())
        layout.addRow("", row_1)
        # layout.addRow()
        # layout.addRow()


class ImageUpload(QLabel):
    def __init__(self, width, height):
        super(ImageUpload, self).__init__()

        self.setFixedSize(width, height)
        self.setObjectName("image_upload")


class EnrollmentForm(QWidget):
    def __init__(self):
        super(EnrollmentForm, self).__init__()

        layout = QGridLayout(self)

        self.info_tab_widget = QTabWidget()
        self.info_tab_widget.addTab(QLabel("Parents info"), "Parents / Guardians")
        self.info_tab_widget.addTab(QLabel("Medical info"), "Medical")
        self.info_tab_widget.addTab(QLabel("Religious info"), "Religion")

        layout.addWidget(ImageUpload(200, 200), 0, 0)
        layout.addWidget(BiodataForm(), 0, 1)
        layout.addWidget(self.info_tab_widget, 1, 0, 1, 2)
