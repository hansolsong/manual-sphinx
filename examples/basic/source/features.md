# 기능 소개

이 페이지에서는 MarginBook Theme의 주요 기능들을 살펴봅니다.

## 마진 노트

### 블록 마진 노트

가장 기본적인 마진 노트는 `{margin}` 디렉티브를 사용합니다:

:::{margin}
**마진 노트 예제**

이것은 블록 레벨 마진 노트입니다. 여러 줄의 텍스트와 다양한 마크다운 요소를 포함할 수 있습니다:

- 목록 항목 1
- 목록 항목 2
- 목록 항목 3
:::

```markdown
:::{margin}
마진에 표시될 내용
:::
```

### 인라인 사이드노트

짧은 주석은 인라인 사이드노트를 사용하세요{sidenote}`이렇게 번호가 자동으로 부여됩니다.`:

```markdown
본문 텍스트{sidenote}`사이드노트 내용`
```

여러 개의 사이드노트를 사용할 수 있으며{sidenote}`첫 번째 노트`, 각각 순차적으로 번호가 매겨집니다{sidenote}`두 번째 노트`.

## 마진 그림

그림을 마진에 배치할 수도 있습니다:

:::{margin-figure} https://via.placeholder.com/300x200
:alt: 예제 이미지

마진에 배치된 그림의 캡션
:::

```markdown
:::{margin-figure} image.png
:alt: 대체 텍스트

그림 캡션
:::
```

## 코드 블록

### 일반 코드 블록

```python
def calculate_margin_width(content_width: float, ratio: float = 0.4) -> float:
    """마진 너비를 계산합니다.
    
    Args:
        content_width: 메인 콘텐츠 영역의 너비
        ratio: 마진 너비 비율
        
    Returns:
        계산된 마진 너비
    """
    return content_width * ratio
```

:::{margin}
**코드 설명**

이 함수는 황금비를 기반으로 최적의 마진 너비를 계산합니다.
:::

### 마진 내 코드

마진 노트 안에도 코드를 넣을 수 있습니다:

:::{margin}
```python
# 간단한 예제
margin = 300  # pixels
content = 650  # pixels
total = margin + content
```
:::

## 수식

수학 수식도 지원됩니다. 인라인 수식 $E = mc^2$과 블록 수식:

$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$

:::{margin}
**가우스 적분**

이 적분은 정규분포와 관련된 중요한 적분입니다.
:::

## 표

| 기능 | HTML | PDF |
|------|------|-----|
| 마진 노트 | ✅ | ✅ |
| 사이드노트 | ✅ | ✅ |
| 마진 그림 | ✅ | ✅ |
| 반응형 | ✅ | ➖ |

:::{margin}
✅ 완전 지원
➖ 해당 없음
:::

## 경고 상자

:::{note}
이것은 일반적인 참고 사항입니다.
:::

:::{margin}
:::{warning}
마진 안에도 경고 상자를 넣을 수 있습니다!
:::
:::

:::{tip}
마진 노트를 효과적으로 사용하려면 주요 내용은 본문에, 보조 정보는 마진에 배치하세요.
:::