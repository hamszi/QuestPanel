@echo off
echo Сборка QuestManager...
pyinstaller --onefile --windowed main.py
echo Сборка завершена!
pause 