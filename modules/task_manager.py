from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
                             QLineEdit, QTextEdit, QCalendarWidget, QPushButton,
                             QWidget, QScrollArea, QFrame)
from PyQt6.QtCore import Qt, QDate
from PyQt6.QtGui import QIcon, QPainter, QPainterPath, QColor
from datetime import datetime

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

class RoundedButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                border-radius: 10px;
                color: white;
                padding: 8px 16px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3d8b40;
            }
        """)

class TaskDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Новая задача")
        self.setMinimumWidth(500)
        self.setStyleSheet("""
            QDialog {
                background-color: #f5f6fa;
            }
        """)
        
        layout = QVBoxLayout(self)
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # Контейнер для формы
        form_container = RoundedFrame()
        form_layout = QVBoxLayout(form_container)
        form_layout.setSpacing(15)
        form_layout.setContentsMargins(20, 20, 20, 20)
        
        # Название задачи
        title_layout = QHBoxLayout()
        title_label = QLabel("Название:")
        title_label.setStyleSheet("font-size: 14px; color: #2c3e50;")
        self.title_edit = QLineEdit()
        self.title_edit.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border: 1px solid #e0e0e0;
                border-radius: 8px;
                background-color: white;
            }
            QLineEdit:focus {
                border: 1px solid #4CAF50;
            }
        """)
        title_layout.addWidget(title_label)
        title_layout.addWidget(self.title_edit)
        form_layout.addLayout(title_layout)
        
        # Описание задачи
        desc_label = QLabel("Описание:")
        desc_label.setStyleSheet("font-size: 14px; color: #2c3e50;")
        self.desc_edit = QTextEdit()
        self.desc_edit.setStyleSheet("""
            QTextEdit {
                padding: 8px;
                border: 1px solid #e0e0e0;
                border-radius: 8px;
                background-color: white;
            }
            QTextEdit:focus {
                border: 1px solid #4CAF50;
            }
        """)
        form_layout.addWidget(desc_label)
        form_layout.addWidget(self.desc_edit)
        
        # Календарь
        calendar_label = QLabel("Срок выполнения:")
        calendar_label.setStyleSheet("font-size: 14px; color: #2c3e50;")
        self.calendar = QCalendarWidget()
        self.calendar.setStyleSheet("""
            QCalendarWidget {
                background-color: white;
                border: 1px solid #e0e0e0;
                border-radius: 8px;
            }
            QCalendarWidget QToolButton {
                color: #2c3e50;
            }
            QCalendarWidget QMenu {
                background-color: white;
                border: 1px solid #e0e0e0;
                border-radius: 8px;
            }
        """)
        form_layout.addWidget(calendar_label)
        form_layout.addWidget(self.calendar)
        
        # Кнопки
        buttons_layout = QHBoxLayout()
        save_btn = RoundedButton("Сохранить")
        cancel_btn = RoundedButton("Отмена")
        cancel_btn.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                border-radius: 10px;
                color: white;
                padding: 8px 16px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
            QPushButton:pressed {
                background-color: #a93226;
            }
        """)
        save_btn.clicked.connect(self.accept)
        cancel_btn.clicked.connect(self.reject)
        buttons_layout.addWidget(save_btn)
        buttons_layout.addWidget(cancel_btn)
        form_layout.addLayout(buttons_layout)
        
        layout.addWidget(form_container)
        
    def get_task_data(self):
        return {
            'title': self.title_edit.text(),
            'description': self.desc_edit.toPlainText(),
            'due_date': self.calendar.selectedDate().toPyDate()
        }

class TaskWidget(QWidget):
    def __init__(self, task_data, parent=None):
        super().__init__(parent)
        self.task_data = task_data
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(5)
        layout.setContentsMargins(5, 5, 5, 5)
        
        # Контейнер задачи
        task_container = RoundedFrame()
        task_layout = QVBoxLayout(task_container)
        task_layout.setSpacing(5)
        task_layout.setContentsMargins(10, 10, 10, 10)
        
        # Верхняя строка с заголовком, сроком и кнопками
        header_layout = QHBoxLayout()
        header_layout.setSpacing(5)
        
        # Заголовок
        title_label = QLabel(self.task_data['title'])
        title_label.setStyleSheet("font-weight: bold; font-size: 14px; color: #2c3e50;")
        title_label.setMaximumWidth(200)  # Уменьшаем максимальную ширину заголовка
        title_label.setWordWrap(True)
        header_layout.addWidget(title_label)
        
        # Срок
        date_label = QLabel(f"• {self.task_data['due_date'].strftime('%d.%m.%Y')}")
        date_label.setStyleSheet("color: #7f8c8d; font-size: 12px;")
        header_layout.addWidget(date_label)
        
        # Кнопки управления
        edit_btn = QPushButton("✎")
        delete_btn = QPushButton("×")
        for btn in [edit_btn, delete_btn]:
            btn.setFixedSize(25, 25)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #4CAF50;
                    border-radius: 12px;
                    color: white;
                    font-size: 14px;
                }
                QPushButton:hover {
                    background-color: #45a049;
                }
                QPushButton:pressed {
                    background-color: #3d8b40;
                }
            """)
        delete_btn.setStyleSheet(delete_btn.styleSheet().replace("#4CAF50", "#e74c3c")
                                                      .replace("#45a049", "#c0392b")
                                                      .replace("#3d8b40", "#a93226"))
        
        header_layout.addWidget(edit_btn)
        header_layout.addWidget(delete_btn)
        task_layout.addLayout(header_layout)
        
        # Описание (с ограничением высоты)
        desc_label = QLabel(self.task_data['description'])
        desc_label.setStyleSheet("color: #34495e; font-size: 12px;")
        desc_label.setWordWrap(True)
        desc_label.setMaximumHeight(40)
        task_layout.addWidget(desc_label)
        
        # Подключаем сигналы
        edit_btn.clicked.connect(self.edit_task)
        delete_btn.clicked.connect(self.delete_task)
        
        layout.addWidget(task_container)
        
    def edit_task(self):
        dialog = TaskDialog(self)
        if dialog.exec():
            new_data = dialog.get_task_data()
            self.task_data.update(new_data)
            self.setup_ui()
            
    def delete_task(self):
        self.deleteLater()

class TaskManager:
    def __init__(self, parent):
        self.parent = parent
        self.tasks = []
        
    def show_add_task_dialog(self):
        dialog = TaskDialog(self.parent)
        if dialog.exec():
            task_data = dialog.get_task_data()
            self.add_task(task_data)
            
    def add_task(self, task_data):
        task_widget = TaskWidget(task_data)
        self.tasks.append(task_widget)
        self.parent.tasks_layout.addWidget(task_widget) 