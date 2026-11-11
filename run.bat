@echo off
chcp 65001 >nul
cd /d "%~dp0"

set PYTHON=C:\Users\14193\python-sdk\python3.13.2\python.exe
set ALLURE=C:\Users\14193\.local\bin\allure-2.29.0\bin\allure.bat

echo [1/3] 运行测试...
"%PYTHON%" -m pytest --alluredir=allure-results --clean-alluredir
if errorlevel 1 echo 测试未全部通过，继续生成报告...

echo.
echo [2/3] 生成 HTML 报告...
call "%ALLURE%" generate allure-results -o allure-report --clean
if errorlevel 1 (
    echo 报告生成失败，请检查 allure 是否可用。
    pause
    exit /b 1
)

echo.
echo [3/3] 启动本地服务并打开报告（按 Ctrl+C 结束服务）...
call "%ALLURE%" open allure-report
