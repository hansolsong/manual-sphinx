# ADR-001: 단일 패키지 아키텍처

## 상태
Accepted (2025-07-11)

## 컨텍스트
MyST/Sphinx 기반으로 HTML과 PDF 출력을 지원하는 매뉴얼 템플릿을 만들고자 한다. 주요 요구사항은:

1. HTML 출력: Quarto의 Cosmo 테마 스타일
2. PDF 출력: Tufte/kaobook 스타일의 2단 레이아웃 (본문 + 마진 노트)
3. 한국어 완벽 지원
4. 다른 프로젝트에서 쉽게 재사용 가능

HTML과 PDF 템플릿을 별도의 패키지로 분리할지, 하나의 통합 패키지로 만들지 결정이 필요했다.

## 결정사항
**단일 통합 패키지**로 `sphinx-marginbook-theme`을 개발한다.

패키지 구조:
```
sphinx-marginbook-theme/
├── sphinx_marginbook_theme/
│   ├── nodes.py           # 공통 노드 정의
│   ├── directives.py      # MyST 디렉티브
│   ├── html/              # HTML 관련
│   └── latex/             # LaTeX/PDF 관련
```

## 근거
1. **Sphinx 아키텍처의 특성**
   - HTML과 LaTeX 빌더가 이미 구조적으로 분리되어 있음
   - HTML은 테마 시스템, PDF는 LaTeX 커스터마이징으로 작동

2. **사용자 편의성**
   - 한 번의 설치로 모든 기능 사용 가능
   - 일관된 API와 설정 방법
   - 버전 호환성 관리 단순화

3. **코드 재사용**
   - MyST 디렉티브 파싱 로직 공유
   - 노드 변환 규칙 통합 관리
   - 공통 유틸리티 함수 활용

4. **기존 사례**
   - sphinx-book-theme, pydata-sphinx-theme 등도 단일 패키지로 다양한 기능 제공

## 결과
### 긍정적 효과
- 설치와 설정이 간단함
- 하나의 소스에서 HTML/PDF 모두 생성
- 유지보수 효율성 증가

### 부정적 효과
- 패키지 크기가 상대적으로 큼
- HTML만 필요한 사용자도 LaTeX 관련 파일 포함

### 완화 방안
- 선택적 의존성으로 LaTeX 관련 패키지 분리
- 모듈화된 내부 구조로 필요한 부분만 로드

## 대안들
1. **별도 패키지 분리**
   - `sphinx-marginbook-html`, `sphinx-marginbook-pdf`
   - 장점: 각 출력 형식에 특화
   - 단점: 설치/관리 복잡, 코드 중복

2. **플러그인 방식**
   - 코어 + HTML 플러그인 + PDF 플러그인
   - 장점: 유연한 구조
   - 단점: 초기 설정 복잡

## 참조
- [Sphinx HTML Theming](https://www.sphinx-doc.org/en/master/usage/theming.html)
- [Sphinx LaTeX Customization](https://www.sphinx-doc.org/en/master/latex.html)
- [sphinx-book-theme Architecture](https://sphinx-book-theme.readthedocs.io/en/stable/contributing/architecture.html)