REM Demo 'BAT' Notification for Paessler Network Monitor
REM Writes current Date/Time into a File
REM 
REM How to use it:
REM 
REM Create a exe-notification on PRTG, select 'Demo Exe Notifcation - OutFile.bat' as program,
REM The Parametersection consists of one parameter:
REM 
REM - Filename
REM 
REM e.g.
REM 
REM         "C:\temp\test.txt"
REM 
REM Note that the directory specified must exist.
REM Adapt Errorhandling to your needs.
REM This script comes without warranty or support.


Echo  %DATE% %TIME% >%1%