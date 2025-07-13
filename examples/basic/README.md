# MarginBook Theme 예제 프로젝트

이 디렉토리는 sphinx-marginbook-theme의 기능을 보여주는 예제 프로젝트입니다.

## 빌드 방법

### 사전 요구사항

```bash
# 패키지 설치 (프로젝트 루트에서)
uv pip install -e ../..
```

### HTML 빌드

```bash
make html
# 또는
sphinx-build -b html source build/html
```

빌드된 문서는 `build/html/index.html`에서 확인할 수 있습니다.

### PDF 빌드

PDF 빌드를 위해서는 XeLaTeX이 필요합니다:

```bash
# macOS
brew install --cask mactex

# Ubuntu/Debian
sudo apt-get install texlive-xetex texlive-fonts-recommended texlive-lang-korean fonts-noto-cjk

# Windows
# MiKTeX 또는 TeX Live 설치
```

그 다음:

```bash
make latexpdf
# 또는
sphinx-build -b latex source build/latex
cd build/latex
make
```

### 실시간 미리보기

```bash
# sphinx-autobuild 설치
uv pip install sphinx-autobuild

# 실시간 서버 시작
sphinx-autobuild source build/html
```

브라우저에서 http://127.0.0.1:8000 접속

## 예제 내용

- `index.md`: 메인 페이지와 목차
- `introduction.md`: 테마 소개와 디자인 철학
- `features.md`: 모든 기능 데모
- `advanced.md`: 고급 사용법과 커스터마이징

## 주요 기능 데모

1. **마진 노트**: `{margin}` 디렉티브
2. **사이드노트**: `{sidenote}` 역할
3. **마진 그림**: `{margin-figure}` 디렉티브
4. **반응형 디자인**: 브라우저 크기 조절로 확인
5. **한국어 지원**: 한글 콘텐츠와 PDF 출력