@echo off

set file=E:\AutoLab\AutoPON.py

python AutoLab\Authenticator\Authenticator.py && python AutoLab\AutoLogin\AutoLogin.py %file%