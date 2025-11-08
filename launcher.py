"""
시와 그림 생성기 - 간단 실행 프로그램
"""
import os
import sys
import subprocess
import webbrowser
import time

def main():
    print("=" * 60)
    print("🌸 시와 그림 생성기 🎨")
    print("=" * 60)
    print("\n프로그램을 시작합니다...\n")

    try:
        # Streamlit 실행
        port = 8501
        url = f"http://localhost:{port}"

        print(f"서버 시작 중... (포트: {port})")
        print(f"\n잠시 후 브라우저가 자동으로 열립니다.")
        print(f"수동으로 열려면: {url}")
        print("\n프로그램을 종료하려면 이 창을 닫으세요.")
        print("=" * 60)
        print()

        # 브라우저 열기 (3초 후)
        import threading
        def open_browser():
            time.sleep(3)
            webbrowser.open(url)

        threading.Thread(target=open_browser, daemon=True).start()

        # Streamlit 실행
        os.system(f"streamlit run app.py --server.port {port} --server.headless true --browser.gatherUsageStats false")

    except KeyboardInterrupt:
        print("\n\n프로그램을 종료합니다...")
    except Exception as e:
        print(f"\n오류 발생: {e}")
        print("\n문제가 계속되면 start_app.bat을 실행해보세요.")
        input("\n아무 키나 누르면 종료됩니다...")

if __name__ == "__main__":
    main()
