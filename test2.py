import sys

from PySide6.QtGui import QTextDocument, QFont
from PySide6.QtWidgets import QApplication, QTextEdit, QSplitter, QPushButton
from PySide6.QtPrintSupport import QPrinter, QPrintDialog

# Create a QTextDocument instance
receipt_document = QTextDocument()
receipt_document.setDefaultFont(QFont("Helvetica", 20))

# Generate the fee receipt HTML content
fee_receipt_html = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Test Project</title>
            <style>
                
            </style>
        </head>
        <body>
            <header>
                <h1>Numbers</h1>
                <h2>Decimals</h2>
                <h3>Place values of decimal numbers</h3>
            </header>
            <main>
                <section>
                    {student_name} fee {fee_amount}
                </section>
                <p>Place value is the value of each digit in a number. For example, the 5 in 350 represents 5 tens, or 50; however, the 5 in 5,006 represents 5 thousands, or 5,000. It is important that children understand that while a digit can be the same, its value depends on where it is in the number.</p>
            </main>
            <footer>
                <small>Copywrite Ngene @2023</small>
            </footer>
        </body>
    </html>
    """

# Populate the fee receipt HTML content with dynamic data
generated_html = fee_receipt_html.format(student_name="John Doe", fee_amount="1000")

# Set the generated HTML content to the QTextDocument
receipt_document.setHtml(generated_html)

# Create a QTextEdit widget for preview

# Set the generated fee receipt QTextDocument as the content of the QTextEdit

def start_print():
    printer = QPrinter(QPrinter.HighResolution)
    # Create a QPrinter instance

    # Create a print dialog for the printer
    printer.setPrintProgram("")

    receipt_document.print_(printer)


if __name__ == "__main__":
    app = QApplication([])
    preview_widget = QTextEdit()
    preview_widget.setFontPointSize(16)
    preview_widget.setFixedSize(400, 700)
    btn = QPushButton("Print")
    btn.clicked.connect(start_print)
    window = QSplitter()
    window.addWidget(preview_widget)
    window.addWidget(btn)
    # Show the preview widget
    preview_widget.setDocument(receipt_document)
    window.show()
    sys.exit(app.exec())

