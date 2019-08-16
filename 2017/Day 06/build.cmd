@echo off
cd dir
cls
.paket\paket.exe restore
if errorlevel 1 (
  exit /b %errorlevel%
)
packages\build\FAKE\tools\FAKE.exe ..\build.fsx %*
