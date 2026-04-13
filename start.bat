@echo off
title Discord Lunar Matrix Bot
color 0a
echo Starting Discord Lunar Matrix Bot...
echo Loading Maya 3D Plane Alignments...
echo Connecting to the Cosmos...

if not exist venv\ (
    echo [!] Virtual environment not found. Creating one...
    python -m venv venv
    call venv\Scripts\activate.bat
    echo [!] Installing requirements...
    pip install -r requirements.txt
) else (
    call venv\Scripts\activate.bat
)

echo [!] Launching Bot...
python bot.py

pause
