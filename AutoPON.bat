@echo off

set file=E:\AutoLab\AutoPON

python AutoLab\Authenticator\Authenticator.py && python AutoLab\AutoLogin\AutoLogin.py %file%
