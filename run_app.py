"""
시와 그림 생성기 런처
이 프로그램은 Streamlit 앱을 실행합니다.
"""
import os
import sys
import subprocess
import webbrowser
import time
from pathlib import Path

def main():
    # 현재 스크립트의 디렉토리 경로
    if getattr(sys, 'frozen', False):
        # PyInstaller로 빌드된 경우
        application_path = os.path.dirname(sys.executable)
    else:
        # 일반 Python 스크립트로 실행되는 경우
        application_path = os.path.dirname(os.path.abspath(__file__))

    # app.py 경로
    app_file = os.path.join(application_path, 'app.py')

    print("=" * 60)
    print("🌸 시와 그림 생성기 🎨")
    print("=" * 60)
    print("\n프로그램을 시작합니다...\n")

    # Streamlit 서버 시작
    try:
        port = 8501
        print(f"서버를 시작하는 중입니다... (포트: {port})")

        # Streamlit 실행
        cmd = [
            sys.executable, '-m', 'streamlit', 'run',
            app_file,
            '--server.port', str(port),
            '--server.headless', 'true',
            '--browser.gatherUsageStats', 'false'
        ]

        # 서브프로세스로 Streamlit 실행
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # 서버가 시작될 때까지 대기
        time.sleep(3)

        # 브라우저 열기
        url = f"http://localhost:{port}"
        print(f"\n✨ 브라우저에서 앱을 엽니다: {url}")
        print("\n프로그램을 종료하려면 이 창을 닫으세요.")
        print("=" * 60)

        webbrowser.open(url)

        # 프로세스가 종료될 때까지 대기
        process.wait()

    except KeyboardInterrupt:
        print("\n\n프로그램을 종료합니다...")
        if process:
            process.terminate()
    except Exception as e:
        print(f"\n오류가 발생했습니다: {e}")
        input("\n아무 키나 누르면 종료됩니다...")
        return 1

    return 0

if __name__ == "__main__":
    sys.exit(main())
