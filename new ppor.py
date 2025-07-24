from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QTextEdit, QFileDialog, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys
import webbrowser

class PortfolioApp(QMainWindow):
    def _init_(self):
        super()._init_()

        # Window Configuration
        self.setWindowTitle("Urvashi's Portfolio")
        self.setGeometry(100, 100, 600, 700)
        self.setStyleSheet("background-color: #1e1e2d; color: white;")

        # Main Widget
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        # Layout
        layout = QVBoxLayout()
        self.main_widget.setLayout(layout)

        # Title
        title_label = QLabel("Urvashi Tiwari")
        title_label.setFont(QFont("Arial", 20, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        subtitle_label = QLabel("BCA Student | Python & ML Enthusiast")
        subtitle_label.setFont(QFont("Arial", 12))
        subtitle_label.setAlignment(Qt.AlignCenter)
        subtitle_label.setStyleSheet("color: #b0b0b0;")
        layout.addWidget(subtitle_label)

        # Buttons
        self.create_button(layout, "About Me", self.show_about, "#3498DB")
        self.create_button(layout, "Projects", self.show_projects, "#4CAF50")
        self.create_button(layout, "LinkedIn Profile", self.open_linkedin, "#0077b5")
        self.create_button(layout, "GitHub Profile", self.open_github, "#24292e")
        self.create_button(layout, "Contact Me", self.show_contact, "#FF9800")
        self.create_button(layout, "Open Calculator", self.open_calculator, "#FF5733")
        self.create_button(layout, "Open Notebook", self.open_notebook, "#3498DB")

    def create_button(self, layout, text, function, color):
        button = QPushButton(text)
        button.setFont(QFont("Arial", 12))
        button.setStyleSheet(f"background-color: {color}; color: white; padding: 10px; border-radius: 10px;")
        button.clicked.connect(function)
        layout.addWidget(button)

    # ---------- ABOUT ME ----------
    def show_about(self):
        QMessageBox.information(self, "About Me",
            "Hi, I'm Urvashi Tiwari! 🎓\n"
            "Currently pursuing my *BCA* at *University of Allahabad*.\n\n"
            "🔹 *Skills*: Python, Java, Flask, MySQL, AI & ML\n"
            "🔹 *Projects*: Chatbot, QR Code Generator, Calculator, Notebook & more\n"
            "🔹 *Achievements*: Topped BCA Batch in Sem 1 & 2\n"
            "🔹 *Goal*: To innovate and explore in the tech industry\n\n"
            "📩 Contact: priyatiwari0425@gmail.com"
        )

    # ---------- PROJECTS ----------
    def show_projects(self):
        QMessageBox.information(self, "Projects",
            "• Hangman Game (Python)\n"
            "• QR Code Generator\n"
            "• Secret Code Language\n"
            "• Chatbot\n"
            "• Calculator (PyQt5)\n"
            "• Notebook (PyQt5)\n"
        )

    # ---------- OPEN LINKEDIN & GITHUB ----------
    def open_linkedin(self):
        webbrowser.open("https://www.linkedin.com/in/urvashi-tiwari2208")

    def open_github(self):
        webbrowser.open("https://github.com/urvashitiwari2522")

    # ---------- CONTACT ----------
    def show_contact(self):
        QMessageBox.information(self, "Contact Me",
            "Email: priyatiwari0425@gmail.com\n"
            "Phone: +91XXXXXXXXXX")

    # ---------- CALCULATOR ----------
    def open_calculator(self):
        self.calc_window = Calculator()
        self.calc_window.show()

    # ---------- NOTEBOOK ----------
    def open_notebook(self):
        self.notebook_window = Notebook()
        self.notebook_window.show()


# ---------- CALCULATOR CLASS ----------
class Calculator(QWidget):
    def _init_(self):
        super()._init_()
        self.setWindowTitle("Calculator")
        self.setGeometry(200, 200, 300, 400)
        self.setStyleSheet("background-color: #222; color: white;")

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.display = QTextEdit()
        self.display.setFont(QFont("Arial", 18))
        self.display.setStyleSheet("background-color: #333; color: white; padding: 10px;")
        layout.addWidget(self.display)

        buttons = [
            "7", "8", "9", "/", "4", "5", "6", "*",
            "1", "2", "3", "-", "0", ".", "=", "+"
        ]

        btn_layout = QVBoxLayout()
        for i in range(0, len(buttons), 4):
            row = QWidget()
            row_layout = QVBoxLayout()
            for btn_text in buttons[i:i+4]:
                btn = QPushButton(btn_text)
                btn.setFont(QFont("Arial", 14))
                btn.setStyleSheet("background-color: #444; color: white; padding: 10px;")
                btn.clicked.connect(lambda _, text=btn_text: self.on_click(text))
                row_layout.addWidget(btn)
            row.setLayout(row_layout)
            btn_layout.addWidget(row)

        layout.addLayout(btn_layout)

    def on_click(self, text):
        if text == "=":
            try:
                result = eval(self.display.toPlainText())
                self.display.setText(str(result))
            except:
                self.display.setText("Error")
        else:
            self.display.insertPlainText(text)


# ---------- NOTEBOOK CLASS ----------
class Notebook(QWidget):
    def _init_(self):
        super()._init_()
        self.setWindowTitle("Notebook")
        self.setGeometry(200, 200, 500, 500)
        self.setStyleSheet("background-color: #282c3c; color: white;")

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.text_area = QTextEdit()
        self.text_area.setFont(QFont("Arial", 12))
        self.text_area.setStyleSheet("background-color: #333; color: white; padding: 10px;")
        layout.addWidget(self.text_area)

        save_button = QPushButton("Save")
        save_button.setFont(QFont("Arial", 12))
        save_button.setStyleSheet("background-color: #3498DB; color: white; padding: 10px;")
        save_button.clicked.connect(self.save_file)
        layout.addWidget(save_button)

    def save_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (.txt);;All Files ()")
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.toPlainText())

# Run App
if __name__ == "_main_":
    app = QApplication(sys.argv)
    window = PortfolioApp()
    window.show()
    sys.exit(app.exec_())Microsoft.QuickAction.WiFi