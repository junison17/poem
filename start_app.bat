@echo off
chcp 65001 >nul
title 시와 그림 생성기
color 0D

echo ========================================================
echo.
echo            🌸 시와 그림 생성기 🎨
echo.
echo ========================================================
echo.
echo 프로그램을 시작합니다...
echo.

REM Python이 설치되어 있는지 확인
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python이 설치되어 있지 않습니다.
    echo.
    echo Python을 설치해주세요: https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

REM 필요한 패키지 설치 확인
echo 필요한 패키지를 확인하는 중...
pip show streamlit >nul 2>&1
if errorlevel 1 (
    echo Streamlit이 설치되어 있지 않습니다. 설치를 시작합니다...
    pip install -r requirements.txt
)

REM Streamlit 앱 실행
echo.
echo ✨ 앱을 시작합니다...
echo.
echo 브라우저가 자동으로 열립니다.
echo 종료하려면 이 창을 닫거나 Ctrl+C를 누르세요.
echo.
echo ========================================================
echo.

start http://localhost:8501
streamlit run app.py --server.port 8501

pause
