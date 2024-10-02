@echo off

set file=AutoLab\AutoPON

python AutoLab\Authenticator\Authenticator.py && python AutoLab\AutoLogin\AutoLogin.py %file%
