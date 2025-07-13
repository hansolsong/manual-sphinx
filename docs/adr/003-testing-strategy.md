# ADR-003: PDF 테스트 전략

## 상태
Accepted (2025-07-11)

## 컨텍스트
PDF 출력의 품질을 보장하기 위해 체계적인 테스트가 필요하다. 특히:

1. 마진 노트가 올바른 위치에 렌더링되는지
2. 한국어 텍스트가 제대로 표시되는지
3. 레이아웃이 일관되게 유지되는지
4. HTML과 PDF에서 동일한 콘텐츠 구조를 갖는지

PDF는 시각적 매체이므로 텍스트 기반 테스트만으로는 불충분하다.

## 결정사항
**다층적 테스트 전략**을 채택한다:

1. **Level 1: LaTeX 출력 테스트**
   - LaTeX 명령어가 올바르게 생성되는지 검증
   - pytest + sphinx-toolbox 사용

2. **Level 2: PDF 시각적 테스트**
   - 생성된 PDF를 참조 PDF와 비교
   - diff-pdf-visually 도구 사용

3. **Level 3: PDF 구조 테스트**
   - 마진 크기, 텍스트 위치 등 측정
   - pdfplumber로 PDF 내부 구조 분석

4. **Level 4: 스냅샷 테스트**
   - 페이지별 이미지 스냅샷 비교
   - pytest-regression 사용

## 근거
1. **다각도 검증**
   - 각 레벨이 서로 다른 측면을 검증
   - 종합적인 품질 보장

2. **자동화 가능**
   - CI/CD 파이프라인에 통합 가능
   - 회귀 테스트 자동화

3. **빠른 피드백**
   - LaTeX 테스트는 빠르게 실행
   - 시각적 테스트는 필요시에만

4. **유지보수성**
   - 골든 파일 업데이트 용이
   - 테스트 실패 시 명확한 피드백

## 결과
### 긍정적 효과
- PDF 품질 보장
- 의도하지 않은 레이아웃 변경 방지
- 한국어 지원 검증

### 부정적 효과
- 테스트 인프라 복잡도 증가
- CI 실행 시간 증가
- 골든 파일 관리 필요

### 완화 방안
- 테스트 레벨별 선택적 실행
- 캐싱으로 빌드 시간 단축
- 주요 변경사항에만 전체 테스트

## 대안들
1. **수동 테스트만**
   - 장점: 설정 간단
   - 단점: 확장성 없음, 실수 가능성

2. **LaTeX 테스트만**
   - 장점: 빠른 실행
   - 단점: 실제 렌더링 검증 불가

3. **상용 도구 사용**
   - 장점: 고급 기능
   - 단점: 라이선스 비용, 의존성

## 구현 예시
```python
# LaTeX 출력 테스트
def test_margin_note_latex(app, latex_regression):
    app.build()
    content = (app.outdir / "test.tex").read_text()
    assert r"\marginnote{" in content

# 시각적 테스트
def test_margin_layout(build_pdf):
    result = diff("expected.pdf", build_pdf)
    assert result == 0

# 구조 테스트
def test_margin_position(build_pdf):
    with pdfplumber.open(build_pdf) as pdf:
        # 마진 노트 위치 검증
        ...
```

## 테스트 데이터
```
tests/
├── fixtures/          # 테스트용 MyST 문서
├── references/        # 골든 PDF 파일
└── snapshots/         # 페이지 스냅샷
```

## CI/CD 통합
- Ubuntu에서 TeX Live 설치
- 한국어 폰트 (Noto CJK) 설치
- 테스트 실패 시 diff 이미지 아티팩트 업로드

## 참조
- [diff-pdf-visually](https://github.com/bgeron/diff-pdf-visually)
- [sphinx-toolbox Testing](https://sphinx-toolbox.readthedocs.io/en/latest/api/testing.html)
- [pytest-regression](https://pytest-regression.readthedocs.io/)
