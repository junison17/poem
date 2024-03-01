import streamlit as st
import openai

# OpenAI API 키 설정
openai.api_key = st.secrets["api_key"]

# 이미지 생성 함수 수정
def generate_image(prompt: str) -> str:
    try:
        # 시의 내용을 기반으로 수채화 그림 생성
        response = openai.Image.create(
            model="dall-e-2",  # 실제 사용 가능한 모델 이름으로 확인 필요
            prompt=f"수채화 그림, {prompt}",  # 시 내용을 포함한 수채화 스타일 프롬프트
            size="512x512",
            n=1,
        )
        return response.data[0].url
    except Exception as e:
        raise Exception(f"이미지 생성 중 오류가 발생했습니다: {str(e)}")

# 시 생성 함수 수정
def generate_poem(prompt: str) -> str:
    try:
        # 대화체 시 유형으로 시 생성
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # 실제 사용 가능한 채팅 모델로 확인 필요
            messages=[
                {"role": "system", "content": "원태연 시인의 스타일로 대화체 시를 작성하십시오."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message['content']
    except Exception as e:
        raise Exception(f"시 생성 중 오류가 발생했습니다: {str(e)}")

# 사용자 입력 받기
prompt = st.text_input('당신의 기분을 입력하세요', '')

# 시 생성 버튼
if st.button('Generate Poem'):
    with st.spinner('시를 생성 중입니다...'):
        try:
            poem = generate_poem(prompt)
            st.session_state['last_poem'] = poem  # 생성된 시를 세션 상태에 저장
            st.write(poem)
        except Exception as e:
            st.error(f"{e}")

# 이미지 생성 버튼
if st.button('Generate Image'):
    with st.spinner('이미지를 생성 중입니다...'):
        try:
            # 세션 상태에서 시의 내용을 가져와 이미지 생성에 사용
            if 'last_poem' in st.session_state:
                image_url = generate_image(st.session_state['last_poem'])
                st.image(image_url, caption='Generated Image')
            else:
                st.error("먼저 시를 생성해주세요.")
        except Exception as e:
            st.error(f"{e}")
