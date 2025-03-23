@echo off
echo Установка зависимостей QuestManager...
python -m pip install --upgrade pip
pip uninstall PyQt6 PyQt6-Qt6 PyQt6-sip -y
pip install PyQt6==6.2.3
pip install PyQt6-Qt6==6.2.3
pip install PyQt6-sip==13.2.1
pip install python-dateutil==2.8.2
pip install pyinstaller==6.3.0
echo Установка завершена!
pause 