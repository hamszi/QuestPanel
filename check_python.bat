@echo off
echo Проверка окружения Python...
echo.

echo Версия Python:
python --version
echo.

echo Путь к Python:
where python
echo.

echo Путь к pip:
where pip
echo.

echo Установленные пакеты:
pip list
echo.

echo Проверка PyQt6:
python -c "import PyQt6; print('PyQt6 версия:', PyQt6.__version__)"
echo.

pause 