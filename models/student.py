from PySide6.QtSql import QSqlTableModel

from core.database import db


class StudentModel(QSqlTableModel):
    def __init__(self):
        super().__init__()

        db.open()
        self.setTable('learners')
        self.select()
        print(db.lastError())
