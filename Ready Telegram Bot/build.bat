@echo off
mode con: cols=100 lines=30
title vusa
color 0a

echo INSTALLING REQUIREMENTS
pip install -U -r requirements.txt

echo Done!

if exist build rmdir /s /q build
py -3.10 builder/Vusa_Telegram_Bot.py


pause