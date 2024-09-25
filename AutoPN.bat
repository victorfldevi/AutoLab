@echo off

set file=E:\AutoLab\AutoPN

python AutoLab\Authenticator\Authenticator.py && python AutoLab\AutoLogin\AutoLogin.py %file%
