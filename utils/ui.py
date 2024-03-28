import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGroupBox, QComboBox, QPushButton, QLabel, QTextEdit
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Feedback Generator")
        self.setGeometry(100, 100, 600, 600)
        self.setStyleSheet("background-color: black; color: white;")
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Dropdown options
        option_groupbox = QGroupBox("Select Option")
        option_layout = QVBoxLayout()

        self.dropdown = QComboBox()
        self.dropdown.addItems(["Appreciated Abilities", "Potential Improvement Areas", "Tips and Advice"])
        self.dropdown.setFont(QFont("Arial", 14))  # Set font size to 14
        self.dropdown.setStyleSheet("QComboBox::item:hover {background-color: transparent;}")  # Remove hover color

        option_layout.addWidget(self.dropdown)
        option_groupbox.setLayout(option_layout)
        layout.addWidget(option_groupbox)

        # Text input
        input_groupbox = QGroupBox("Enter Text")
        input_layout = QVBoxLayout()

        self.input_text = QTextEdit()
        input_layout.addWidget(self.input_text)
        input_groupbox.setLayout(input_layout)
        layout.addWidget(input_groupbox)

        # Clear input text button
        self.clear_button = QPushButton("Clear")
        self.clear_button.setStyleSheet("background-color: red; color: white; width: 50px; height: 20px;")
        self.clear_button.clicked.connect(self.clearInputText)
        input_layout.addWidget(self.clear_button, alignment=Qt.AlignTop | Qt.AlignRight)  # Align button to top right

        # Generate and Save Buttons
        button_groupbox = QGroupBox()
        button_layout = QVBoxLayout()

        self.generate_button = QPushButton("Generate")
        self.generate_button.setStyleSheet("background-color: yellow; color: black;")
        button_layout.addWidget(self.generate_button)

        self.regenerate_button = QPushButton("Regenerate Response")
        self.regenerate_button.setStyleSheet("background-color: yellow; color: black;")
        button_layout.addWidget(self.regenerate_button)

        button_groupbox.setLayout(button_layout)
        layout.addWidget(button_groupbox)

        # Response area
        self.response_label = QLabel("Response:")
        self.response_label.setFont(QFont("Arial", 12))
        layout.addWidget(self.response_label)

        self.response_text = QTextEdit()
        self.response_text.setReadOnly(True)
        layout.addWidget(self.response_text)

        # Save Button
        self.save_button = QPushButton("Save Response")
        self.save_button.setStyleSheet("background-color: yellow; color: black;")
        layout.addWidget(self.save_button)

        self.setLayout(layout)



    def clearInputText(self):
        # Clear the input text area
        self.input_text.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
