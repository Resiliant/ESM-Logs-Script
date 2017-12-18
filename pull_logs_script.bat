REM USE WINSCP SPECIFIC COMMANDS TO PUSH BATCH SCRIPTS TO ESM THEN PULL DATA LOGS FROM ESM

REM Start batch script
@echo off

"C:\Program Files (x86)\WinSCP\WinSCP.com" ^
  /log="C:\Users\Razil\Desktop\WinSCP_Logs\WinSCP.log" /ini=nul ^
  /command ^
    "open sftp://root:Password.1@192.168.1.230/ -hostkey=""ssh-rsa 2048 e8:d1:5c:35:07:c1:66:46:37:d3:1b:5e:a6:0f:09:cc""" ^
    "put *.sh /root/Scripts/" ^
    "exit"

set WINSCP_RESULT=%ERRORLEVEL%
if %WINSCP_RESULT% equ 0 (
  echo Success
) else (
  echo Error
)
pause
REM exit /b %WINSCP_RESULT%