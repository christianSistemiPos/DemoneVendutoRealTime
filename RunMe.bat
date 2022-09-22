@echo off
:: BatchGotAdmin
::-------------------------------------
REM  --> Check for permissions
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"

REM --> If error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    set params = %*:"="
    echo UAC.ShellExecute "cmd.exe", "/c %~s0 %params%", "", "runas", 1 >> "%temp%\getadmin.vbs"

    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
    pushd "%CD%"
    CD /D "%~dp0"
::--------------------------------------
/../git/bin/git clone https://github.com/christianSistemiPos/DemoneVendutoRealTime.git VendutoRealTime
echo "Installazione Build Tools"
C:\SistemiPos\VendutoRealTime\Installazione\utils\buildtools.exe
echo "Ok."
timeout /t 5
echo "Installazione SQLConnector"
C:\SistemiPos\VendutoRealTime\Installazione\utils\msodbcsql.msi
echo "Ok."
timeout /t 5
echo "Installazione python"
cd C:\SistemiPos\VendutoRealTime\bin
python get-pip.py
python -m pip install -r C:\SistemiPos\VendutoRealTime\Installazione\utils\requirements.txt
echo "OK".
timeout /t 5
echo "Avvio Installazione"
python ../installa.py
echo "OK".
timeout /t 5
"Criptazione Dati"
echo "Criptazione configurazione"
python C:\SistemiPos\VendutoRealTime\Demone\Assistenza\bin\cripta_configurazione.py
echo "OK".
timeout /t 5
echo "Installazione servizio"
cd ..\Installazione
cd nssm\win64
nssm install "VendutoRealTime" "C:\SistemiPos\VendutoRealTime\bin\python.exe" "C:\SistemiPos\VendutoRealTime\Demone\main.py"
nssm set VendutoRealTime AppStderr "C:\SistemiPos\VendutoRealTime\Demone\servizio_err.log"
nssm set VendutoRealTime AppStdout "C:\SistemiPos\VendutoRealTime\Demone\servizio.log"
timeout /t 5
echo "Ok."
cd C:\SistemiPos\VendutoRealTime\
rm -r ./PDVVRT
rm -r ./Installazione
rm installa.py
rm config.json