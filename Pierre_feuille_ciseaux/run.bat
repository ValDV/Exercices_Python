@echo off
:loop
python script.py
echo.
echo Voulez-vous refaire une partie ? (oui/non)
set /p rejouer=
if /i "%rejouer%"=="oui" goto loop
pause