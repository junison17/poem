@echo off
chcp 65001 >nul
echo ========================================================
echo.
echo        🔧 시와 그림 생성기 - EXE 빌드 스크립트
echo.
echo ========================================================
echo.

REM PyInstaller 설치 확인
echo PyInstaller를 설치하는 중...
pip install pyinstaller

echo.
echo EXE 파일을 생성하는 중...
echo.

REM 이전 빌드 정리
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist

REM PyInstaller로 빌드
pyinstaller --clean --onefile --name "시와그림생성기" --add-data "app.py;." --add-data ".streamlit;.streamlit" --console launcher.py

echo.
echo ========================================================
echo.
if exist "dist\시와그림생성기.exe" (
    echo ✅ 성공! EXE 파일이 생성되었습니다!
    echo.
    echo 📁 파일 위치: %CD%\dist\시와그림생성기.exe
    echo.
    echo 💡 사용 방법:
    echo    1. dist 폴더로 이동
    echo    2. "시와그림생성기.exe" 파일을 실행
    echo.
) else (
    echo ❌ 빌드에 실패했습니다.
    echo.
)
echo ========================================================
pause
