from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize the main window layout
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        # Create and add initial widgets/layouts to the main layout
        self.add_initial_layouts()

    def add_initial_layouts(self):
        # Add initial widgets/layouts to the main layout
        inner_layout = QHBoxLayout()
        button1 = QPushButton("Button 1")
        label1 = QLabel("Label 1")
        inner_layout.addWidget(button1)
        inner_layout.addWidget(label1)

        self.main_layout.addLayout(inner_layout)

    def replace_layouts(self):
        # Clear the existing main layout
        while self.main_layout.count():
            item = self.main_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
            else:
                layout = item.layout()
                if layout:
                    self.clear_layout(layout)

        # Add new widgets/layouts to the main layout
        inner_layout = QVBoxLayout()
        button2 = QPushButton("Button 2")
        label2 = QLabel("Label 2")
        inner_layout.addWidget(button2)
        inner_layout.addWidget(label2)

        inner_layout.setAlignment(QtCore.Qt.Alignment.AlignTop)
        self.main_layout.addLayout(inner_layout)

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()

    # Example: Replace layouts after a certain event (e.g., button click)
    # Replace this with your actual event triggering the layout replacement
    # For demonstration, I'm calling replace_layouts after 3 seconds
    import sys
    from PyQt6.QtCore import QTimer
    QTimer.singleShot(3000, window.replace_layouts)

    sys.exit(app.exec())
