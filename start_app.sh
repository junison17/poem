#!/bin/bash

echo "========================================================"
echo ""
echo "           🌸 시와 그림 생성기 🎨"
echo ""
echo "========================================================"
echo ""
echo "프로그램을 시작합니다..."
echo ""

# Python이 설치되어 있는지 확인
if ! command -v python3 &> /dev/null && ! command -v python &> /dev/null
then
    echo "❌ Python이 설치되어 있지 않습니다."
    echo ""
    echo "Python을 설치해주세요: https://www.python.org/downloads/"
    echo ""
    read -p "아무 키나 누르면 종료됩니다..."
    exit 1
fi

# Python 명령어 설정
PYTHON_CMD="python3"
if ! command -v python3 &> /dev/null
then
    PYTHON_CMD="python"
fi

# 필요한 패키지 설치 확인
echo "필요한 패키지를 확인하는 중..."
$PYTHON_CMD -m pip show streamlit > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "Streamlit이 설치되어 있지 않습니다. 설치를 시작합니다..."
    $PYTHON_CMD -m pip install -r requirements.txt
fi

# Streamlit 앱 실행
echo ""
echo "✨ 앱을 시작합니다..."
echo ""
echo "브라우저가 자동으로 열립니다."
echo "종료하려면 Ctrl+C를 누르세요."
echo ""
echo "========================================================"
echo ""

$PYTHON_CMD -m streamlit run app.py --server.port 8501
