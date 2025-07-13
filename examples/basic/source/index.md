# MarginBook Theme 예제 문서

```{toctree}
:maxdepth: 2
:caption: 목차

introduction
features
advanced
```

이 문서는 **sphinx-marginbook-theme**의 기능을 보여주는 예제입니다.

:::{margin}
**MarginBook Theme**

HTML과 PDF 모두에서 아름다운 마진 노트를 지원하는 Sphinx 테마입니다.
:::

## 주요 특징

- 📝 **마진 노트**: MyST 디렉티브를 사용한 우아한 사이드 콘텐츠
- 🎨 **Cosmo 스타일**: 깔끔하고 현대적인 디자인
- 📖 **PDF 지원**: Tufte 스타일의 전문적인 PDF 출력
- 🌏 **한국어 지원**: 완벽한 한국어 문서 작성

## 빠른 시작

테마를 사용하려면 다음과 같이 설정하세요:

```python
# conf.py
extensions = [
    'myst_parser',
    'sphinx_marginbook_theme',
]

html_theme = 'marginbook'
```

이제 문서에서 마진 노트를 사용할 수 있습니다{sidenote}`이것은 번호가 있는 사이드노트입니다.`!

:::{margin}
**팁**: 마진 노트는 추가 정보나 참고 사항을 제공하는 데 적합합니다.
:::

## 문서 구성

이 예제 문서는 다음과 같이 구성되어 있습니다:

1. **소개** - 테마의 기본 개념
2. **기능** - 마진 노트, 그림, 코드 블록 등
3. **고급 사용법** - 커스터마이징과 확장