@echo off

set file=AutoLab\AutoPN

python AutoLab\Authenticator\Authenticator.py && python AutoLab\AutoLogin\AutoLogin.py %file%
