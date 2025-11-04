import streamlit as st
import openai
from anthropic import Anthropic

# API 키 설정
# Streamlit secrets 또는 환경 변수에서 API 키를 가져옵니다
# .streamlit/secrets.toml 파일에 다음과 같이 설정하세요:
# CLAUDE_API_KEY = "your-claude-api-key"
# OPENAI_API_KEY = "your-openai-api-key"

import os

CLAUDE_API_KEY = st.secrets.get("CLAUDE_API_KEY", os.getenv("CLAUDE_API_KEY", ""))
OPENAI_API_KEY = st.secrets.get("OPENAI_API_KEY", os.getenv("OPENAI_API_KEY", ""))

# OpenAI 클라이언트 초기화
openai.api_key = OPENAI_API_KEY

# Anthropic 클라이언트 초기화
anthropic_client = Anthropic(api_key=CLAUDE_API_KEY)

# 파스텔 UI 스타일 적용
st.set_page_config(page_title="시와 그림 생성기", page_icon="🌸", layout="wide")

# 커스텀 CSS로 부드러운 파스텔 테마 적용
st.markdown("""
<style>
    /* 전체 배경 */
    .stApp {
        background: linear-gradient(135deg, #ffeef8 0%, #e7f3ff 50%, #fff5e7 100%);
    }

    /* 헤더 스타일 */
    h1 {
        color: #d896b0 !important;
        text-align: center;
        font-family: 'Georgia', serif;
        text-shadow: 2px 2px 4px rgba(216, 150, 176, 0.2);
        padding: 20px;
    }

    h2 {
        color: #b8a4d4 !important;
        font-family: 'Georgia', serif;
    }

    h3 {
        color: #9db8d4 !important;
        font-family: 'Georgia', serif;
    }

    /* 입력 박스 스타일 */
    .stTextInput > div > div > input {
        background-color: #ffffff;
        border: 2px solid #f5d5e6;
        border-radius: 15px;
        padding: 15px;
        color: #8b6f8f;
        font-size: 16px;
    }

    .stTextInput > div > div > input:focus {
        border-color: #d896b0;
        box-shadow: 0 0 10px rgba(216, 150, 176, 0.3);
    }

    /* 버튼 스타일 */
    .stButton > button {
        background: linear-gradient(135deg, #f5d5e6 0%, #e7d5f5 100%);
        color: #8b6f8f;
        border: none;
        border-radius: 20px;
        padding: 15px 30px;
        font-size: 16px;
        font-weight: bold;
        box-shadow: 0 4px 6px rgba(216, 150, 176, 0.2);
        transition: all 0.3s ease;
        width: 100%;
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #e7d5f5 0%, #d5e7f5 100%);
        box-shadow: 0 6px 12px rgba(184, 164, 212, 0.3);
        transform: translateY(-2px);
    }

    /* 스피너 스타일 */
    .stSpinner > div {
        border-top-color: #d896b0 !important;
    }

    /* 텍스트 영역 스타일 */
    .stMarkdown {
        background-color: rgba(255, 255, 255, 0.7);
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
        border-left: 5px solid #d896b0;
    }

    /* 에러 및 성공 메시지 */
    .stSuccess {
        background-color: #d5f5e3;
        border-radius: 10px;
        padding: 15px;
    }

    .stError {
        background-color: #ffd5e0;
        border-radius: 10px;
        padding: 15px;
    }

    /* 이미지 컨테이너 */
    .stImage {
        border-radius: 20px;
        box-shadow: 0 8px 16px rgba(216, 150, 176, 0.3);
        overflow: hidden;
    }

    /* 사이드바 */
    .css-1d391kg {
        background-color: #ffeef8;
    }

    /* 구분선 */
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, #f5d5e6 0%, #e7d5f5 50%, #d5e7f5 100%);
        margin: 30px 0;
    }
</style>
""", unsafe_allow_html=True)

# 앱 제목
st.markdown("# 🌸 시와 그림 생성기 🎨")
st.markdown("### ✨ 당신의 감정을 아름다운 시와 수채화로 표현해드립니다")
st.markdown("---")

# 이미지 생성 함수 (GPT DALL-E 사용)
def generate_image(prompt: str) -> str:
    try:
        # 시의 내용을 기반으로 수채화 그림 생성
        response = openai.Image.create(
            model="dall-e-2",
            prompt=f"Soft watercolor painting, pastel colors, dreamy atmosphere: {prompt}",
            size="512x512",
            n=1,
        )
        return response.data[0].url
    except Exception as e:
        raise Exception(f"이미지 생성 중 오류가 발생했습니다: {str(e)}")

# 시 생성 함수 (Claude API 사용)
def generate_poem(prompt: str) -> str:
    try:
        # Claude API를 사용하여 시 생성
        message = anthropic_client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": f"원태연 시인의 스타일로 '{prompt}'라는 기분이나 주제로 대화체의 아름다운 시를 작성해주세요. 감성적이고 서정적인 표현을 사용하되, 자연스럽고 일상적인 언어로 써주세요."
                }
            ]
        )
        return message.content[0].text
    except Exception as e:
        raise Exception(f"시 생성 중 오류가 발생했습니다: {str(e)}")

# 메인 컨테이너
col1, col2 = st.columns([3, 2])

with col1:
    st.markdown("### 💭 기분이나 감정을 입력해주세요")
    prompt = st.text_input('', placeholder='예: 외로움, 봄날의 설렘, 비 오는 날의 고요함...', label_visibility="collapsed")

    st.markdown("")

    # 버튼을 나란히 배치
    btn_col1, btn_col2 = st.columns(2)

    with btn_col1:
        generate_poem_btn = st.button('🖋️ 시 생성하기')

    with btn_col2:
        generate_image_btn = st.button('🎨 그림 생성하기')

with col2:
    st.markdown("### 📝 사용 방법")
    st.markdown("""
    1. 왼쪽에 당신의 기분이나 감정을 입력하세요
    2. '시 생성하기' 버튼을 클릭하여 시를 만드세요
    3. '그림 생성하기' 버튼으로 시에 어울리는 그림을 만드세요
    """)

st.markdown("---")

# 시 생성
if generate_poem_btn:
    if prompt:
        with st.spinner('✨ 아름다운 시를 작성하고 있습니다...'):
            try:
                poem = generate_poem(prompt)
                st.session_state['last_poem'] = poem
                st.session_state['last_prompt'] = prompt

                st.markdown("### 📜 생성된 시")
                st.markdown(f"""
                <div style='background: linear-gradient(135deg, #ffffff 0%, #ffeef8 100%);
                            border-radius: 15px;
                            padding: 30px;
                            border-left: 5px solid #d896b0;
                            box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
                    <p style='color: #8b6f8f;
                             line-height: 1.8;
                             font-size: 16px;
                             white-space: pre-wrap;
                             font-family: "Georgia", serif;'>{poem}</p>
                </div>
                """, unsafe_allow_html=True)
            except Exception as e:
                st.error(f"❌ {e}")
    else:
        st.warning("⚠️ 먼저 기분이나 감정을 입력해주세요!")

# 이미지 생성
if generate_image_btn:
    with st.spinner('🎨 수채화 그림을 그리고 있습니다...'):
        try:
            if 'last_poem' in st.session_state:
                # 시의 내용과 원래 프롬프트를 모두 활용
                image_prompt = f"{st.session_state.get('last_prompt', '')}: {st.session_state['last_poem'][:200]}"
                image_url = generate_image(image_prompt)

                st.markdown("### 🖼️ 생성된 그림")
                st.image(image_url, caption='수채화 스타일의 그림', use_column_width=True)
            else:
                st.error("❌ 먼저 시를 생성해주세요!")
        except Exception as e:
            st.error(f"❌ {e}")

# 세션 상태에 시가 있으면 표시
if 'last_poem' in st.session_state and not generate_poem_btn:
    st.markdown("### 📜 이전에 생성된 시")
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, #ffffff 0%, #ffeef8 100%);
                border-radius: 15px;
                padding: 30px;
                border-left: 5px solid #d896b0;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
        <p style='color: #8b6f8f;
                 line-height: 1.8;
                 font-size: 16px;
                 white-space: pre-wrap;
                 font-family: "Georgia", serif;'>{st.session_state['last_poem']}</p>
    </div>
    """, unsafe_allow_html=True)

# 푸터
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #b8a4d4; padding: 20px;'>
    <p>🌸 Powered by Claude AI & DALL-E 🎨</p>
    <p style='font-size: 12px;'>당신의 감정을 예술로 승화시킵니다</p>
</div>
""", unsafe_allow_html=True)
