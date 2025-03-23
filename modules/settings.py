from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
                             QPushButton, QComboBox, QGroupBox, QFrame)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor

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

class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Настройки")
        self.setMinimumWidth(400)
        self.setStyleSheet("""
            QDialog {
                background-color: #f5f6fa;
            }
        """)
        
        layout = QVBoxLayout(self)
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # Контейнер для настроек
        container = RoundedFrame()
        container_layout = QVBoxLayout(container)
        container_layout.setSpacing(15)
        container_layout.setContentsMargins(20, 20, 20, 20)
        
        # Информация о версии
        version_group = QGroupBox("Информация")
        version_group.setStyleSheet("""
            QGroupBox {
                border: 1px solid #e0e0e0;
                border-radius: 10px;
                margin-top: 15px;
                padding-top: 10px;
                font-weight: bold;
                color: #2c3e50;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px;
            }
        """)
        version_layout = QVBoxLayout()
        version_label = QLabel("Версия: 1.0.0")
        version_label.setStyleSheet("color: #34495e;")
        version_layout.addWidget(version_label)
        version_group.setLayout(version_layout)
        container_layout.addWidget(version_group)
        
        # Настройки темы
        theme_group = QGroupBox("Тема")
        theme_group.setStyleSheet(version_group.styleSheet())
        theme_layout = QVBoxLayout()
        
        theme_combo = QComboBox()
        theme_combo.addItems(["Светлая", "Темная"])
        theme_combo.setStyleSheet("""
            QComboBox {
                padding: 8px;
                border: 1px solid #e0e0e0;
                border-radius: 8px;
                background-color: white;
            }
            QComboBox:hover {
                border: 1px solid #4CAF50;
            }
            QComboBox::drop-down {
                border: none;
                width: 20px;
            }
            QComboBox::down-arrow {
                image: url(down_arrow.png);
                width: 12px;
                height: 12px;
            }
        """)
        theme_combo.currentTextChanged.connect(self.change_theme)
        theme_layout.addWidget(theme_combo)
        
        theme_group.setLayout(theme_layout)
        container_layout.addWidget(theme_group)
        
        # Кнопки
        buttons_layout = QHBoxLayout()
        close_btn = RoundedButton("Закрыть")
        close_btn.clicked.connect(self.accept)
        buttons_layout.addWidget(close_btn)
        container_layout.addLayout(buttons_layout)
        
        layout.addWidget(container)
        
    def change_theme(self, theme):
        if theme == "Светлая":
            self.parent().setStyleSheet("""
                QMainWindow {
                    background-color: #f5f6fa;
                }
                QLabel {
                    color: #2c3e50;
                }
                QFrame {
                    background-color: white;
                }
            """)
        else:
            self.parent().setStyleSheet("""
                QMainWindow {
                    background-color: #2c3e50;
                }
                QLabel {
                    color: #ecf0f1;
                }
                QFrame {
                    background-color: #34495e;
                }
            """) 