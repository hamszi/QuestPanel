@echo off
echo Проверка версии Python...
python --version
if errorlevel 1 (
    echo Python не установлен или не добавлен в PATH
    pause
    exit /b 1
)

echo Проверка установки PyQt6...
python -c "import PyQt6" 2>nul
if errorlevel 1 (
    echo PyQt6 не установлен. Запуск установки зависимостей...
    call install_dependencies.bat
)

echo Проверка установки PyQt6-Qt6...
python -c "import PyQt6.QtCore" 2>nul
if errorlevel 1 (
    echo Ошибка загрузки PyQt6-Qt6. Попытка переустановки...
    call install_dependencies.bat
)

echo Запуск QuestManager в режиме разработки...
python main.py
pause 