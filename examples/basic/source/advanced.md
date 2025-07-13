# 고급 사용법

이 장에서는 MarginBook Theme의 고급 기능과 커스터마이징 방법을 다룹니다.

## 테마 커스터마이징

### HTML 테마 옵션

`conf.py`에서 다양한 테마 옵션을 설정할 수 있습니다:

```python
html_theme_options = {
    # 레이아웃
    'margin_width': '350px',        # 마진 너비
    'margin_gap': '2.5rem',         # 마진과 본문 간격
    'content_max_width': '700px',   # 본문 최대 너비

    # 색상
    'primary_color': '#2c3e50',     # 주 색상
    'link_color': '#18bc9c',        # 링크 색상
    'text_color': '#333333',        # 텍스트 색상

    # 기능
    'show_nav_level': 3,            # 네비게이션 깊이
    'sticky_navigation': True,      # 고정 네비게이션
}
```

:::{margin}
**CSS 변수**

모든 테마 옵션은 CSS 변수로 변환되어 `--mb-` 접두사와 함께 사용됩니다.
:::

### CSS 커스터마이징

추가 CSS를 통해 더 세밀한 조정이 가능합니다:

```css
/* _static/custom.css */
:root {
    --mb-font-family: 'Noto Sans KR', sans-serif;
    --mb-margin-width: 400px;
}

.margin-note {
    font-style: italic;
    border-left: 2px solid var(--mb-primary);
    padding-left: 1rem;
}
```

## LaTeX/PDF 커스터마이징

### LaTeX 요소 수정

```python
# conf.py
from sphinx_marginbook_theme import get_latex_elements

latex_elements = get_latex_elements()

# 추가 커스터마이징
latex_elements['preamble'] += r'''
\setlength{\marginparwidth}{45mm}
\renewcommand{\marginfont}{\small\sffamily}
'''
```

:::{margin}
**LaTeX 팁**

XeLaTeX을 사용하므로 유니코드와 다양한 폰트를 자유롭게 사용할 수 있습니다.
:::

### 한국어 폰트 설정

기본적으로 Noto CJK 폰트를 사용하지만, 다른 폰트로 변경할 수 있습니다:

```latex
\setmainfont{KoPubBatang}
\setsansfont{KoPubDotum}
```

## 고급 마진 노트 기법

### 중첩된 구조

마진 노트 안에 다른 요소를 중첩할 수 있습니다:

::::{margin}
:::{note}
마진 안의 노트 박스

```python
# 코드도 가능
print("Hello, Margin!")
```
:::
::::

### 조건부 콘텐츠

빌더에 따라 다른 콘텐츠를 표시할 수 있습니다{sidenote}`이 기능은 Sphinx의 only 디렉티브를 사용합니다.`:

```markdown
:::{only} html
HTML에서만 보이는 내용
:::

:::{only} latex
PDF에서만 보이는 내용
:::
```

## 성능 최적화

### 이미지 최적화

마진에 배치되는 이미지는 적절한 크기로 최적화하세요:

:::{margin}
**권장 이미지 크기**
- 마진 그림: 300px 너비
- 레티나 디스플레이: 600px
- 파일 형식: WebP (HTML), PNG/PDF (LaTeX)
:::

### 빌드 시간 단축

큰 문서의 경우 다음 방법으로 빌드 시간을 단축할 수 있습니다:

1. `sphinx-autobuild` 사용으로 증분 빌드
2. 병렬 빌드 활성화: `sphinx-build -j auto`
3. 필요한 빌더만 실행

## 문제 해결

### 마진 노트가 겹치는 경우

연속된 마진 노트가 겹치는 경우, CSS로 간격을 조정하세요:

```css
.margin-note + .margin-note {
    margin-top: 2rem;
}
```

### PDF 한글 깨짐

XeLaTeX이 아닌 pdfLaTeX을 사용하는 경우 발생할 수 있습니다:

```python
# 반드시 XeLaTeX 사용
latex_engine = 'xelatex'
```

:::{margin}
**도움말**

추가 문제는 GitHub 이슈에 보고해주세요.
:::

## 확장 개발

MarginBook Theme을 확장하여 새로운 디렉티브를 추가할 수 있습니다:

```python
from sphinx_marginbook_theme.directives import MarginDirective

class CustomMarginDirective(MarginDirective):
    """커스텀 마진 디렉티브"""

    option_spec = {
        **MarginDirective.option_spec,
        'highlight': directives.flag,
    }

    def run(self):
        # 커스텀 로직
        return super().run()
```
