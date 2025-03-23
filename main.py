import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                            QPushButton, QLabel, QScrollArea, QFrame, QHBoxLayout)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QPainter, QPainterPath, QColor, QLinearGradient
from modules.task_manager import TaskManager
from modules.settings import SettingsDialog

class RoundedButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setFixedSize(40, 40)
        self.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                border-radius: 20px;
                color: white;
                font-size: 24px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3d8b40;
            }
        """)

class RoundedFrame(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 15px;
                border: 1px solid #e0e0e0;
            }
        """)

class QuestManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QuestManager")
        self.setMinimumSize(900, 600)
        
        # Создаем центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)
        
        # Создаем основной контейнер с закругленными углами
        container = RoundedFrame()
        container_layout = QVBoxLayout(container)
        container_layout.setContentsMargins(20, 20, 20, 20)
        
        # Заголовок
        title_label = QLabel("QuestManager")
        title_label.setStyleSheet("""
            QLabel {
                color: #2c3e50;
                font-size: 24px;
                font-weight: bold;
                padding: 10px;
            }
        """)
        container_layout.addWidget(title_label)
        
        # Область прокрутки для задач
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("""
            QScrollArea {
                border: none;
                background-color: transparent;
            }
            QScrollBar:vertical {
                border: none;
                background-color: #f0f0f0;
                width: 10px;
                margin: 0px;
            }
            QScrollBar::handle:vertical {
                background-color: #c0c0c0;
                border-radius: 5px;
                min-height: 20px;
            }
        """)
        
        tasks_widget = QWidget()
        self.tasks_layout = QVBoxLayout(tasks_widget)
        self.tasks_layout.setSpacing(15)
        scroll_area.setWidget(tasks_widget)
        container_layout.addWidget(scroll_area)
        
        # Кнопки управления
        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(10)
        
        self.add_task_btn = RoundedButton("+")
        self.settings_btn = RoundedButton("⚙")
        
        buttons_layout.addStretch()
        buttons_layout.addWidget(self.add_task_btn)
        buttons_layout.addWidget(self.settings_btn)
        
        container_layout.addLayout(buttons_layout)
        
        # Добавляем контейнер в основной layout
        main_layout.addWidget(container)
        
        # Подключаем сигналы
        self.add_task_btn.clicked.connect(self.show_add_task_dialog)
        self.settings_btn.clicked.connect(self.show_settings)
        
        # Инициализация менеджера задач
        self.task_manager = TaskManager(self)
        
        # Устанавливаем стиль окна
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f6fa;
            }
        """)
        
    def show_add_task_dialog(self):
        self.task_manager.show_add_task_dialog()
        
    def show_settings(self):
        settings_dialog = SettingsDialog(self)
        settings_dialog.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = QuestManager()
    window.show()
    sys.exit(app.exec())
