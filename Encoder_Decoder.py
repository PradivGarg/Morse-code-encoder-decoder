import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QMessageBox, QWidget, QTextEdit
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt


#Morse code dictionary for alphabets A-Z and digits 0-9
MORSE_CODE_DICT ={
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': "---..", '9': "----.",
    ' ': '/'
}
REVERSE_CODE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}
# Morse Code Generator using PyQt5

class MorseCodeGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Morse Code encoder/decoder")
        self.setGeometry(200, 200, 500, 400)
        self.setWindowIcon(QIcon("MorseCoder/morse.png"))

        self.layout = QVBoxLayout()

        self.label = QLabel("Enter text to convert:")
        self.label.setFont(QFont("Arial", 12))
        self.layout.addWidget(self.label)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("color: #333;")


        self.inputText = QTextEdit(self)
        self.inputText.setPlaceholderText("Type here...")
        self.layout.addWidget(self.inputText)
        self.inputText.setStyleSheet("""
            QTextEdit {
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 10px;
                font-size: 14px;
            }
        """)

        self.convertButton = QPushButton("Convert to Morse Code", self)
        self.convertButton.clicked.connect(self.convert_to_morse)
        self.layout.addWidget(self.convertButton)
        self.convertButton.setStyleSheet("background-color: #333; color: #fff; border: none; padding: 10px; font-size: 16px; border-radius: 5px;")
        

        self.convertButton = QPushButton("Reverse Convert", self)
        self.convertButton.clicked.connect(self.ReverseMorse)
        self.layout.addWidget(self.convertButton)
        self.convertButton.setStyleSheet("background-color: #333; color: #fff; border: none; padding: 10px; font-size: 16px; border-radius: 5px;")
        

        self.outputLabel = QLabel("Output:")
        self.outputLabel.setFont(QFont("Arial", 12))
        self.layout.addWidget(self.outputLabel)
        self.outputLabel.setAlignment(Qt.AlignCenter)
        self.outputLabel.setStyleSheet("color: #333;")

        self.outputText = QTextEdit(self)
        self.outputText.setReadOnly(True)
        self.layout.addWidget(self.outputText)

        self.setLayout(self.layout)
        self.setStyleSheet("""
            QWidget {
                background-color: #f0f0f0;
            }
            QLabel {
                color: #333;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 10px 20px;
                text-align: center;
                text-decoration: none;
                font-size: 16px;
                margin: 4px 2px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        
    def convert_to_morse(self):
        inputText = self.inputText.toPlainText().upper()
        if not inputText.strip():
            QMessageBox.warning(self, "Input Error", "Please enter some text to convert.")
            return
        morseCodeWords = []
        for char in inputText:
            morseChar = []
            if char in MORSE_CODE_DICT:
                morseChar.append(MORSE_CODE_DICT[char])
            else:
                QMessageBox.warning(self, "Input Error", f"Character '{char}' is not supported. Only A-Z and 0-9 are allowed.")
                return
            morseWord = " ".join(morseChar)
            morseCodeWords.append(morseWord)

        morseCode = " ".join(morseCodeWords)
        self.outputText.setPlainText(morseCode)
    
    def ReverseMorse(self):
        inputText = self.inputText.toPlainText()
        if not inputText.strip():
            QMessageBox.warning(self, "Input Error", "Please enter text to convert.")
            return
        morseCodeWords = inputText.split(" ")
        decodedMessage = []
        for morseChar in morseCodeWords:
            if morseChar in REVERSE_CODE_DICT:
                decodedMessage.append(REVERSE_CODE_DICT[morseChar])
            else:
                QMessageBox.warning(self, "Input Error", f"Morse code '{morseChar}' is not supported.")
                return
        decodedMessage = "".join(decodedMessage)
        self.outputText.setPlainText(decodedMessage)

def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MorseCodeGenerator()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()


        
