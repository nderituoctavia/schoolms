import sys

from PySide6.QtCore import QUrl
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QApplication

# Create a QWebEngineView widget


# Show the preview widget
if __name__ == "__main__":
    app = QApplication([])
    preview = QWebEngineView()

    # Load the generated fee receipt HTML content
    preview.setHtml("""
    <!DOCTYPE html>
    <html>
        <head>
            <title>Test Project</title>
            <style>
                * {
                    font-family: Arial, Helvetica, sans-serif;
                }
                h1 {
                    color: blue;
                    text-align: center;
                    font-family: Z003;
                    font-size: 48pt;
                }
                h2, h3 {
                    color: gray;
                }
                p {
                    width: 500px;
                    margin: 0 auto;
                }
            </style>
        </head>
        <body>
            <header>
                <h1>Numbers</h1>
                <h2>Decimals</h2>
                <h3>Place values of decimal numbers</h3>
            </header>
            <main>
                <section></section>
                <p>Place value is the value of each digit in a number. For example, the 5 in 350 represents 5 tens, or 50; however, the 5 in 5,006 represents 5 thousands, or 5,000. It is important that children understand that while a digit can be the same, its value depends on where it is in the number.</p>
            </main>
            <footer>
                <small>Copywrite Ngene @2023</small>
            </footer>
        </body>
    </html>
    """, QUrl("about:blank"))
    preview.show()
    sys.exit(app.exec())
