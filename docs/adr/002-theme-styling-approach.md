# ADR-002: 테마 스타일링 접근법

## 상태
Accepted (2025-07-11)

## 컨텍스트
HTML과 PDF 출력에 대해 각각 다른 스타일링 요구사항이 있다:

1. **HTML**: Quarto의 Cosmo 테마 스타일
   - 깔끔하고 현대적인 디자인
   - Bootstrap 5 기반
   - 반응형 레이아웃

2. **PDF**: Tufte/kaobook 스타일
   - 2단 레이아웃 (본문 + 넓은 마진)
   - 마진 노트와 사이드 노트
   - 고품질 타이포그래피

두 출력 형식에서 일관된 사용자 경험을 제공하면서도 각 매체의 특성을 살려야 한다.

## 결정사항
1. **kaobook을 직접 사용하지 않고 구조만 참고**하여 핵심 기능을 독자적으로 구현
2. **HTML**: 기존 Sphinx 테마 시스템 활용 + 커스텀 CSS
3. **PDF**: 최소한의 LaTeX 커스터마이징으로 마진 레이아웃 구현

### HTML 구현 방식
```css
/* Cosmo 스타일 색상과 타이포그래피 */
:root {
    --margin-width: 300px;
    --cosmo-primary: #2c3e50;
}

/* 마진 노트는 position: absolute로 구현 */
.margin-note {
    position: absolute;
    width: var(--margin-width);
    /* 반응형: 작은 화면에서는 인라인으로 */
}
```

### PDF 구현 방식
```latex
% geometry 패키지로 레이아웃 설정
\usepackage[textwidth=117mm, marginparwidth=39.4mm]{geometry}

% marginnote 패키지로 마진 노트 구현
\usepackage{marginnote}
\newcommand{\sidenote}[1]{...}
```

## 근거
1. **독립성 유지**
   - kaobook 전체를 포함하면 의존성이 복잡해짐
   - 핵심 기능만 구현하여 유지보수 용이

2. **Sphinx 생태계 통합**
   - 기존 Sphinx 워크플로우와 자연스럽게 통합
   - 표준 빌드 프로세스 유지

3. **단순성**
   - 복잡한 LaTeX 클래스 대신 필요한 기능만 구현
   - 사용자가 이해하고 커스터마이징하기 쉬움

## 결과
### 긍정적 효과
- 가벼운 패키지 크기
- Sphinx의 기존 기능들과 호환
- 커스터마이징 용이

### 부정적 효과
- kaobook의 모든 기능을 사용할 수 없음
- 일부 고급 레이아웃 기능 제한

### 완화 방안
- 사용자가 필요시 추가 LaTeX 패키지 로드 가능
- 확장 가능한 구조로 설계

## 대안들
1. **kaobook 직접 사용**
   - 장점: 완성도 높은 레이아웃
   - 단점: 복잡한 의존성, Sphinx와의 통합 어려움

2. **완전 커스텀 LaTeX 클래스**
   - 장점: 완벽한 제어
   - 단점: 개발 시간 과다, 유지보수 부담

3. **CSS Print 스타일시트**
   - 장점: HTML/PDF 통일된 코드
   - 단점: PDF 품질 제한, 브라우저 의존

## 구현 세부사항
### MyST 디렉티브
```markdown
:::{margin}
마진에 표시될 내용
:::

본문{sidenote}`번호가 있는 사이드노트`
```

### 빌더별 처리
- HTML: CSS 클래스와 JavaScript로 렌더링
- LaTeX: `\marginnote{}`, `\sidenote{}` 명령어로 변환

## 참조
- [Tufte CSS](https://edwardtufte.github.io/tufte-css/)
- [kaobook LaTeX class](https://github.com/fmarotta/kaobook)
- [Quarto HTML Themes](https://quarto.org/docs/output-formats/html-themes.html)