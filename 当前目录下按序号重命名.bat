@echo off 
setlocal enabledelayedexpansion
::打开系统延时
set /a b=0
dir /b/od
::按时间顺序显示当前文件夹下的所有文件名
pause

for /f "delims=" %%f in ('dir /b/od *.*') do (
  if not "%%f"=="%~nx0" (
           set /a b+=1 
           ren "%%f" "!b!%%~xf"
           echo. !b!%%~xf
  )
)
pause