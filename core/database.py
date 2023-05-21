from PySide6.QtSql import QSqlDatabase


db = QSqlDatabase.addDatabase("QMYSQL")
db.setDatabaseName("stceciliaclc")
db.setHostName("localhost")
db.setUserName("admin")
db.setPassword("admin")