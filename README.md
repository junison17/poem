# 🌸 시와 그림 생성기 🎨

Claude AI와 DALL-E를 활용한 감성적인 시와 수채화 그림 생성 애플리케이션입니다.

## ✨ 주요 기능

- 🖋️ **AI 시 생성**: Claude API를 사용하여 원태연 시인 스타일의 대화체 시를 생성합니다
- 🎨 **수채화 그림 생성**: OpenAI DALL-E 2를 사용하여 시에 어울리는 파스텔 톤의 수채화 그림을 생성합니다
- 🌈 **부드러운 파스텔 UI**: 감성적인 파스텔 컬러 테마로 디자인된 사용자 인터페이스

## 🚀 설치 및 실행

### 1. 저장소 클론

```bash
git clone https://github.com/junison17/poem.git
cd poem
```

### 2. 필요한 패키지 설치

```bash
pip install -r requirements.txt
```

### 3. API 키 설정

`.streamlit/secrets.toml.example` 파일을 `.streamlit/secrets.toml`로 복사하고 실제 API 키를 입력합니다:

```bash
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
```

`.streamlit/secrets.toml` 파일을 열어 다음과 같이 수정하세요:

```toml
CLAUDE_API_KEY = "your-actual-claude-api-key"
OPENAI_API_KEY = "your-actual-openai-api-key"
```

#### API 키 발급 방법:
- **Claude API 키**: [Anthropic Console](https://console.anthropic.com/)에서 발급
- **OpenAI API 키**: [OpenAI Platform](https://platform.openai.com/)에서 발급

### 4. 애플리케이션 실행

```bash
streamlit run app.py
```

브라우저에서 자동으로 열립니다 (기본: http://localhost:8501)

## 📖 사용 방법

1. **감정 입력**: 당신의 기분이나 감정을 입력란에 작성하세요 (예: "외로움", "봄날의 설렘", "비 오는 날의 고요함")
2. **시 생성**: "🖋️ 시 생성하기" 버튼을 클릭하여 AI가 작성한 시를 확인하세요
3. **그림 생성**: "🎨 그림 생성하기" 버튼을 클릭하여 시와 어울리는 수채화 그림을 생성하세요

## 🛠️ 기술 스택

- **Frontend**: Streamlit
- **AI Models**:
  - Claude 3.5 Sonnet (시 생성)
  - DALL-E 2 (이미지 생성)
- **언어**: Python 3.8+

## 🎨 UI 특징

- 부드러운 파스텔 그라데이션 배경
- 감성적인 컬러 팔레트 (핑크, 라벤더, 블루 톤)
- 반응형 레이아웃
- 직관적인 사용자 경험

## 📝 라이선스

이 프로젝트는 개인 및 교육 목적으로 자유롭게 사용할 수 있습니다.

## 🤝 기여

이슈와 풀 리퀘스트는 언제나 환영합니다!

---

**Made with 💜 by Claude AI & DALL-E**
