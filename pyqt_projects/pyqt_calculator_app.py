import sys
from PyQt6.QtWidgets import QWidget,QApplication,QGridLayout,QLabel,QPushButton
from PyQt6.QtCore import Qt

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Calculator')

        self.current_input = '0'
        self.previous_input = ''
        self.current_operator = ''

        layout = QGridLayout()
        self.setLayout(layout)

        self.display = QLabel('0')
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.display, 0, 0, 1, 4)

        buttons = [QPushButton(str(i)) for i in range(10)]

        operators = ['+', '-', '*', '/']
        operator_buttons = [QPushButton(op) for op in operators]
        
        for button in operator_buttons:
            button.clicked.connect(self.operator_button_clicked)

        equals_button = QPushButton('=')
        clear_button = QPushButton('C')

        for i, button in enumerate(buttons):
            row, col = divmod(i, 3)
            layout.addWidget(button, row+1, col)
        
        for button in buttons:
            button.clicked.connect(self.number_button_clicked)
        
        for i, op_button in enumerate(operator_buttons):
            layout.addWidget(op_button, i+1, 3)
        

        layout.addWidget(equals_button, 4, 1)
        layout.addWidget(clear_button, 4, 2)
    
    def number_button_clicked(self):
        digit = self.sender().text()

        if self.current_input == '0':
            self.current_input = digit
        
        else:
            self.current_input += digit
        
        self.display.setText(self.current_input)
    
    def operator_button_clicked(self):
        operator = self.sender().text()
        if self.current_operator == '':
            self.current_operator = operator
            self.previous_input = self.current_input
            self.current_input = '0'
        
        else:
            self.calculate()
            self.current_operator = operator
            self.previous_input = self.current_input
            self.current_input = '0'
        
    def calculate(self):
        if self.current_operator == '+':
            result = float(self.previous_input) + float(self.current_input)
        elif self.current_operator == '-':
            result = float(self.previous_input) - float(self.current_input)
        
        elif self.current_operator == '*':
            result = float(self.previous_input) * float(self.current_input)
        
        elif self.current_operator == '/':
            if self.current_input == '0':
                result = 'Error'
            else:
                result = float(self.previous_input) / float(self.current_input)
        else:
            result = self.current_input
        
        self.display.setText(result)
        self.current_input = result
        self.current_operator = ''



app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())