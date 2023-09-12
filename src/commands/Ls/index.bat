@echo off
setlocal

rem Get the root directory of the batch script
set "root_dir=%~dp0"

set path_command =  %root_dir%index.py
rem Execute the Python script with the captured arguments
python %path_command%
