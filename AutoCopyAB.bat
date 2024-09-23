@echo off
set start=1
python AutoLab\Authenticator\Authenticator.py && python AutoLab\AutoCopyAB\AutoCopyAB.py %start%
pause
set start=2
python AutoLab\Authenticator\Authenticator.py && python AutoLab\AutoCopyAB\AutoCopyAB.py %start%