# CLAUDE.md - sphinx-marginbook-theme 프로젝트 가이드

이 문서는 sphinx-marginbook-theme 개발을 위한 Claude Code 전용 가이드입니다.

## 프로젝트 개요

MyST/Sphinx 기반으로 아름다운 매뉴얼을 작성할 수 있는 통합 테마 패키지입니다.

### 핵심 목표
- **HTML 출력**: Quarto Cosmo 스타일의 깔끔한 디자인
- **PDF 출력**: Tufte/kaobook 스타일의 마진 노트 레이아웃
- **한국어 지원**: 완벽한 한국어 문서 작성
- **사용 편의성**: 간단한 설정으로 즉시 사용 가능

## 아키텍처 결정사항 (ADR)

프로젝트의 주요 설계 결정사항은 ADR로 문서화되어 있습니다:

1. [ADR-001: 단일 패키지 아키텍처](docs/adr/001-package-architecture.md)
   - HTML과 PDF를 하나의 패키지로 통합
   - 모듈화된 내부 구조

2. [ADR-002: 테마 스타일링 접근법](docs/adr/002-theme-styling-approach.md)
   - kaobook 구조 참고, 독자적 구현
   - 최소한의 LaTeX 커스터마이징

3. [ADR-003: PDF 테스트 전략](docs/adr/003-testing-strategy.md)
   - 다층적 테스트 (LaTeX, 시각적, 구조적, 스냅샷)
   - CI/CD 통합 자동화

## 개발 가이드라인

### 패키지 구조
```
sphinx-marginbook-theme/
├── sphinx_marginbook_theme/
│   ├── __init__.py         # setup() 함수 포함
│   ├── nodes.py            # docutils 노드 정의
│   ├── directives.py       # MyST 디렉티브
│   ├── html/               # HTML 빌더 관련
│   └── latex/              # LaTeX 빌더 관련
```

### 코딩 규칙

1. **Python 코드**
   - Type hints 사용 필수
   - docstring은 Google 스타일
   - Black으로 포매팅
   - Ruff로 린팅

2. **CSS/JavaScript**
   - CSS 변수 활용으로 커스터마이징 용이하게
   - 모바일 우선 반응형 디자인
   - 접근성(a11y) 고려

3. **LaTeX 템플릿**
   - 주석으로 각 섹션 설명
   - 한국어 사용자를 위한 설정 명시
   - 최소한의 패키지 의존성

### 테스트 작성

PDF 테스트 시:
```bash
# LaTeX 출력만 테스트 (빠름)
pytest tests/test_latex_output.py

# 전체 PDF 테스트 (느림)
pytest tests/test_pdf_*.py

# 골든 파일 업데이트
pytest tests/test_pdf_visual.py --regen
```

### 커밋 메시지
```
feat(latex): 마진 노트 위치 조정 기능 추가
fix(html): 모바일에서 마진 노트 겹침 수정
test(pdf): 한국어 폰트 렌더링 테스트 추가
docs: MyST 디렉티브 사용법 문서화
```

## 주요 기능 구현 상태

- [ ] 기본 패키지 구조
- [ ] MyST 디렉티브 (`{margin}`, `{sidenote}`)
- [ ] HTML 테마 (Cosmo 스타일)
- [ ] LaTeX 템플릿 (마진 레이아웃)
- [ ] 한국어 지원
- [ ] PDF 테스트 인프라
- [ ] 예제 프로젝트
- [ ] 문서화
- [ ] PyPI 배포 준비

## 개발 환경 설정

```bash
# uv 사용
uv venv
uv pip install -e ".[dev]"

# pre-commit 설정
pre-commit install
```

## 빌드 및 테스트

```bash
# 문서 빌드
cd docs
make html
make latexpdf

# 테스트 실행
pytest
pytest --cov=sphinx_marginbook_theme

# 타입 체크
mypy sphinx_marginbook_theme
```

## 디버깅 팁

1. **LaTeX 에러**: `_build/latex/` 디렉토리의 `.log` 파일 확인
2. **마진 노트 위치**: 브라우저 개발자 도구로 CSS 확인
3. **PDF 차이**: `diff-pdf-visually`로 시각적 비교

## 참고 자료

- [Sphinx 공식 문서](https://www.sphinx-doc.org/)
- [MyST Parser](https://myst-parser.readthedocs.io/)
- [kaobook 소스 코드](https://github.com/fmarotta/kaobook)
- [Tufte CSS](https://edwardtufte.github.io/tufte-css/)

---

**주의**: 이 프로젝트는 사용자 친화적인 API를 최우선으로 합니다. 복잡한 설정보다는 합리적인 기본값을 제공하세요.