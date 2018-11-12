@echo off

title FYP Flask Batch
echo Script is running!
cmd /k "cd /d %~dp0\venv\Scripts & activate & cd /d    %~dp0 & Set FLASK_APP=proto1.py & Set FLASK_ENV=development & Set FLASK_DEBUG=1 & Flask run"
pause