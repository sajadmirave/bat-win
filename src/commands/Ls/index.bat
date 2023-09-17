@echo off
rem Get the root directory of the batch script
set "root_dir=%~dp0"

rem Construct the path to the Python script
set "path_command=%root_dir%index.py"

rem Execute the Python script with the captured arguments
echo %path_command%
python "%path_command%"

rem You can add additional commands or error handling here
