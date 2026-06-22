# 스토리보드 기획 문서
# Storyboard Planning Document

---

| 항목 | 내용 |
|------|------|
| 캠페인명 | 만들기 전에, 한 번 더 |
| 공모전 | K-AI 콘텐츠 공모전 2026 |
| 출품 부문 | Track A. 대학(원)/일반부 — AI 영상(광고) |
| 문서 작성일 | 2026-06-14 |

---

## 1. 브랜드 아이덴티티 / Brand Identity

| 항목 | 내용 |
|------|------|
| **캠페인명** | 만들기 전에, 한 번 더 |
| **공모 주제 분류** | AI 윤리 준수 — 생성형 AI 사용 시 지켜야 할 에티켓 및 저작권 보호 |
| **타겟** | 생성형 AI 창작 도구를 사용하는 대학생·크리에이터·일반인 (20~40대) |
| **톤앤매너** | 미니멀·감성적 / 차분하고 여운 있는 시네마틱 |
| **USP (차별점)** | "AI로 만들 때도 창작자의 권리를 먼저 생각한다"는 태도 자체가 새로운 창작 문화임을 보여줌 |
| **핵심 메시지 (한 문장)** | **AI로 만들 때도, 창작자를 먼저 생각합니다.** |
| **엔딩 슬로건** | 만들기 전에, 한 번 더. |

---

## 2. 캠페인 목표 및 서사 구조 / Campaign Objective & Narrative

**광고 목적** : AI 저작권·에티켓 인식 제고 (인지 + 태도 변화)

**서사 구조 (기승전결)**

```
[기]  누군가의 손에서 창작물이 탄생한다          → 씬 1
[승]  그 수많은 창작물들이 AI를 만들었다          → 씬 2
[전]  이제 당신도 AI로 창작하는 사람이다          → 씬 3
[결]  만들기 전에, 한 번 더 — 출처·허락·존중      → 씬 4 + 씬 5
```

---

## 3. 영상 스펙 / Video Specification

| 항목 | 내용 |
|------|------|
| 총 길이 | 40초 |
| 해상도 | 1920 × 1080 (1080p) |
| 화면 비율 | 16:9 가로형 |
| 프레임레이트 | 24fps |
| 비디오 코덱 | H.264 |
| 오디오 코덱 | AAC |
| BGM | 공모전 공식 지정 음원 |
| AI 워터마크 | 공식 가이드 기준 우측 하단 표기 |

---

## 4. 사용 도구 목록 / Tool List

| 목적 | 주 도구 | 대안 도구 | 선택 이유 |
|------|---------|-----------|-----------|
| 이미지 생성 | Google Gemini | Ideogram, Canva AI | 프롬프트 접근성이 높고 사실적·일러스트 스타일 모두 지원 |
| 영상 변환 | Runway Gen-3 | Pika | 이미지 → 모션 변환 품질이 우수하며 씬별 세밀한 모션 제어 가능 |
| 음성 합성 (TTS) | ElevenLabs | CLOVA Voice | 감성적이고 자연스러운 한국어 목소리 지원 |
| BGM | 공모전 공식 지정 음원 | — | 공모전 규정 필수 |
| 편집 통합 | CapCut | DaVinci Resolve | 텍스트 애니메이션·AI 워터마크 삽입·BGM 페이드아웃 편집 |

---

## 5. 씬별 스토리보드 / Scene-by-Scene Storyboard

---

### 씬 1 — 창작자의 손 / Creator's Hand

| 필드 | 내용 |
|------|------|
| **씬 번호** | 1 |
| **씬 길이** | 7초 (0~7초) |
| **목표 메시지** | 사람의 손에서 창작물이 탄생한다는 사실을 시각적으로 각인시킨다 |
| **화면 구성** | 클로즈업 / 손·붓·건반·키보드 / 어두운 스튜디오 배경 / 텍스트 없음 |
| **내레이션 / 카피** | 없음 (음악과 영상만) |
| **사용 도구** | 이미지 : Google Gemini / 영상 : Runway Gen-3 |
| **도구 선택 이유** | Gemini로 3개 장면(화가·피아니스트·작가) 키비주얼 생성 후 Runway로 짧은 슬로우모션 변환 |

**캐릭터 시트 — 상우 (Sangwoo)**

![캐릭터 시트 — 상우](../02_text to img/character_sheets/character_sheet_sangwoo_v2_fixed.png)

**씬 1 구성 : 3개 컷을 빠르게 이어붙임 (각 약 2초)**

#### [컷 A] 화가의 손 / Painter's Hand

**이미지 생성 프롬프트 (Gemini 입력용)**

```
A dramatic close-up of a painter's hand holding a fine brush,
making a single delicate stroke on a white canvas.
Chiaroscuro lighting, dark studio background, warm golden highlights,
shallow depth of field, cinematic, photorealistic, 4K.
```
> 화가의 손이 붓으로 한 획을 긋는 클로즈업. 명암 대비 강한 조명, 어두운 배경, 황금빛 하이라이트.

**영상 변환 프롬프트 (Runway 입력용)**

```
The hand slowly raises the brush and makes a single deliberate stroke,
gentle motion, cinematic slow motion, 24fps.
```
> 붓을 천천히 들어올려 한 획을 긋는 슬로우모션

| | |
|--|--|
| **생성 결과 파일명** | `scene01A_painter.png` / `scene01A_motion.mp4` |
| **출력 결과 요약** | 황금빛 조명 아래 붓을 쥔 손 클로즈업, 시네마틱 분위기 확보 |

---

#### [컷 B] 피아니스트의 손 / Pianist's Hand

**이미지 생성 프롬프트 (Gemini 입력용)**

```
A close-up of elegant fingers resting on black and white piano keys,
soft dramatic studio lighting, dark blurred background,
cool blue and white tones, shallow depth of field,
cinematic, photorealistic, 4K.
```
> 피아노 건반 위에 얹힌 우아한 손가락. 차가운 청백 색조, 어두운 배경.

**영상 변환 프롬프트 (Runway 입력용)**

```
Fingers gently press the piano keys one by one,
slow and deliberate, soft sound wave ripple effect on keys,
cinematic slow motion.
```
> 건반을 하나씩 천천히 누르는 동작, 음파 잔물결 효과

| | |
|--|--|
| **생성 결과 파일명** | `scene01B_pianist.png` / `scene01B_motion.mp4` |
| **출력 결과 요약** | 청백 색조의 우아한 손가락 건반 클로즈업 확보 |

---

#### [컷 C] 작가의 손 / Writer's Hand

**이미지 생성 프롬프트 (Gemini 입력용)**

```
A close-up of a writer's hand typing on a mechanical keyboard,
fingers mid-keystroke, one key in sharp focus,
dark moody background, desaturated cool tones with warm fingertip highlight,
cinematic, photorealistic, 4K, shallow depth of field.
```
> 기계식 키보드를 타이핑하는 손. 하나의 키에 선명하게 초점.

**영상 변환 프롬프트 (Runway 입력용)**

```
Fingers type steadily on the keyboard, keys pressing down rhythmically,
cinematic slow motion, subtle motion blur on fingers.
```
> 리드미컬하게 타이핑하는 손, 슬로우모션 + 손 모션 블러

| | |
|--|--|
| **생성 결과 파일명** | `scene01C_writer.png` / `scene01C_motion.mp4` |
| **출력 결과 요약** | 어두운 배경에 타이핑하는 손 클로즈업, 긴장감 있는 분위기 확보 |

---

### 씬 2 — AI 학습 시각화 / AI Learning Visualization

| 필드 | 내용 |
|------|------|
| **씬 번호** | 2 |
| **씬 길이** | 10초 (7~17초) |
| **목표 메시지** | 수많은 창작물이 AI를 학습시켰다는 사실을 추상적으로 시각화한다 |
| **화면 구성** | 광각 / 창작물 파티클이 중앙 AI 아이콘으로 수렴 / 어두운 우주 배경 / 내레이션 텍스트 있음 |
| **내레이션 / 카피** | "이 모든 창작물이... AI를 만들었습니다." |
| **사용 도구** | 이미지 : Google Gemini / 영상 : Runway Gen-3 / 음성 : ElevenLabs |
| **도구 선택 이유** | Gemini로 추상 파티클 시각화 이미지 생성, Runway로 수렴 모션 연출, ElevenLabs로 감성적 내레이션 |

**이미지 생성 프롬프트 (Gemini 입력용)**

```
An abstract digital visualization of thousands of tiny artworks,
music notes, handwritten text, and painting fragments
all flowing and converging into a single glowing AI neural network icon at the center.
Deep dark navy space background, electric blue and white luminous particles,
flowing data streams, cinematic, high contrast, dramatic, 4K.
```
> 그림·악보·텍스트 조각들이 중앙의 빛나는 AI 아이콘으로 수렴. 어두운 우주 배경, 파란 파티클.

**영상 변환 프롬프트 (Runway 입력용)**

```
Thousands of tiny image and text particles swirl and stream inward,
converging into the central glowing AI icon which pulses with light,
smooth flowing motion, cinematic VFX style.
```
> 파티클이 소용돌이치며 중앙으로 수렴, AI 아이콘이 맥박처럼 빛나는 VFX 연출

**내레이션 텍스트 (ElevenLabs 입력용)**

```
이 모든 창작물이... AI를 만들었습니다.
```
> 목소리 설정 : 차분하고 낮은 톤 / 느린 속도 / 감성적

| | |
|--|--|
| **생성 결과 파일명** | `scene02_ai_learning.png` / `scene02_motion.mp4` / `scene02_narration.mp3` |
| **출력 결과 요약** | 어두운 우주 배경 위 파란 파티클이 AI 아이콘으로 수렴하는 추상 시각 확보 |

---

### 씬 3 — 당신도 창작자 / You Are Also a Creator

| 필드 | 내용 |
|------|------|
| **씬 번호** | 3 |
| **씬 길이** | 8초 (17~25초) |
| **목표 메시지** | AI 도구를 사용하는 사람도 창작 행위의 주체임을 인식시킨다 |
| **화면 구성** | 미디엄 샷 / 노트북 앞 인물 실루엣 / 따뜻한 자연광 배경 / 내레이션 텍스트 있음 |
| **내레이션 / 카피** | "이제, 당신도 창작자입니다." |
| **사용 도구** | 이미지 : Google Gemini / 영상 : Runway Gen-3 / 음성 : ElevenLabs |
| **도구 선택 이유** | 실루엣 처리로 시청자가 인물에 자신을 투영할 수 있게 하고, 창문 자연광으로 씬 2의 어두운 분위기에서 희망적 분위기로 전환 |

**이미지 생성 프롬프트 (Gemini 입력용)**

```
A medium shot of a person's silhouette sitting at a desk with a laptop,
the laptop screen glowing brightly showing colorful AI-generated artwork.
Soft warm sunlight streaming through a window behind the figure,
golden dust particles floating in the light, lens flare,
cinematic, hopeful atmosphere, photorealistic, 4K.
```
> 노트북 앞에 앉은 인물 실루엣. 창문에서 흘러드는 따뜻한 자연광, 먼지 파티클, 희망적 분위기.

**영상 변환 프롬프트 (Runway 입력용)**

```
The person slowly raises their head and looks at the glowing screen,
camera slowly pushes in toward the laptop screen,
warm sunlight gradually brightens, cinematic slow motion.
```
> 인물이 고개를 들어 화면을 바라보며 카메라가 화면 쪽으로 천천히 당겨지는 연출

**내레이션 텍스트 (ElevenLabs 입력용)**

```
이제, 당신도 창작자입니다.
```
> 목소리 설정 : 따뜻하고 부드러운 톤 / 확신 있는 속도

| | |
|--|--|
| **생성 결과 파일명** | `scene03_creator.png` / `scene03_motion.mp4` / `scene03_narration.mp3` |
| **출력 결과 요약** | 따뜻한 자연광 아래 노트북 앞 실루엣, 희망적 분위기 전환 확보 |

---

### 씬 4 — 행동 지침 / Three Actions

| 필드 | 내용 |
|------|------|
| **씬 번호** | 4 |
| **씬 길이** | 10초 (25~35초) |
| **목표 메시지** | 출처 표기·허락·존중, 3가지 구체적 행동을 명확하게 전달한다 |
| **화면 구성** | 센터 프레임 / 아티스트와 AI 사용자 미니멀 일러스트 / 흰 배경 / 3단계 텍스트 순차 강조 |
| **내레이션 / 카피** | "출처를 밝히고, 허락을 구하고, 창작자를 존중합니다." |
| **사용 도구** | 이미지 : Google Gemini / 영상 : Runway Gen-3 / 텍스트 : CapCut / 음성 : ElevenLabs |
| **도구 선택 이유** | Gemini로 미니멀 일러스트 스타일 이미지 생성, CapCut으로 3단계 텍스트 페이드인 삽입 |

**이미지 생성 프롬프트 (Gemini 입력용)**

```
A minimalist flat vector illustration of two friendly figures standing side by side.
Left figure: an artist holding a paintbrush and color palette.
Right figure: a person using a laptop with a small glowing star icon on the screen.
Clean white background, pastel color palette of soft blue and warm yellow,
simple geometric shapes, balanced and warm composition, no text, no shadows.
```
> 두 인물이 나란히 선 미니멀 일러스트. 왼쪽은 아티스트, 오른쪽은 AI 사용자. 파스텔 블루·노란색.

**영상 변환 프롬프트 (Runway 입력용)**

```
The two figures simultaneously turn toward each other and nod gently,
subtle friendly animation, soft pastel glow between them,
smooth looping motion, flat 2D animation style.
```
> 두 인물이 서로를 향해 고개를 끄덕이는 친근한 애니메이션, 사이에 파스텔 빛

**내레이션 텍스트 (ElevenLabs 입력용)**

```
출처를 밝히고, 허락을 구하고, 창작자를 존중합니다.
```
> 목소리 설정 : 명확하고 또렷한 톤 / 세 문장 사이 짧은 간격

**CapCut 텍스트 편집 (씬 4 내부)**

| 타이밍 | 텍스트 | 효과 |
|--------|--------|------|
| 0~3초 | 출처를 밝히고, | 페이드인 |
| 3~6초 | 허락을 구하고, | 페이드인 |
| 6~10초 | 창작자를 존중합니다. | 페이드인 + 유지 |

| | |
|--|--|
| **생성 결과 파일명** | `scene04_coexist.png` / `scene04_motion.mp4` / `scene04_narration.mp3` |
| **출력 결과 요약** | 파스텔 톤 두 인물 공존 일러스트, 따뜻하고 균형 있는 구성 확보 |

---

### 씬 5 — 엔딩 슬로건 카드 / Ending Slogan Card

| 필드 | 내용 |
|------|------|
| **씬 번호** | 5 |
| **씬 길이** | 5초 (35~40초) |
| **목표 메시지** | 슬로건을 각인시키고 AI 워터마크와 함께 공모전 아이덴티티를 마무리한다 |
| **화면 구성** | 센터 타이포그래피 / 텍스트만 / 짙은 네이비 배경 / 슬로건 + 서브 메시지 |
| **내레이션 / 카피** | "만들기 전에, 한 번 더." |
| **사용 도구** | 편집 : CapCut / 음성 : ElevenLabs |
| **도구 선택 이유** | AI 이미지 생성 불필요. CapCut 타이포그래피 애니메이션으로 슬로건 엔딩 카드 제작, AI 워터마크 삽입 및 BGM 페이드아웃 처리 |
| **입력 프롬프트** | 해당 없음 (편집 작업) |
| **출력 결과 요약** | 슬로건 타이포그래피 엔딩 카드 완성 |

**CapCut 설정**

| 항목 | 설정값 |
|------|--------|
| 배경색 | `#0D1B2A` (짙은 네이비 블랙) |
| 메인 텍스트 | `만들기 전에, 한 번 더.` |
| 메인 텍스트 색상 | `#FFFFFF` |
| 서브 텍스트 | `AI로 만들 때도, 창작자를 먼저 생각합니다.` |
| 텍스트 폰트 | Noto Sans KR Bold 계열 |
| 등장 효과 | 페이드인 (0.5초) |
| BGM | 공모전 공식 지정 음원 → 페이드아웃 |
| AI 워터마크 | 우측 하단 삽입 |

**내레이션 텍스트 (ElevenLabs 입력용)**

```
만들기 전에, 한 번 더.
```
> 목소리 설정 : 여운이 있는 낮고 조용한 톤 / 천천히

| | |
|--|--|
| **생성 결과 파일명** | `scene05_ending.mp4` |

---

## 6. 프롬프트 수정 전/후 기록 / Prompt Revision Log

> 과제 필수 : 최소 1개 씬에서 프롬프트 수정 전/후 비교 기록

**대상 씬 : 씬 2 — AI 학습 시각화**

| 항목 | 내용 |
|------|------|
| **수정 전 프롬프트** | `many images and text flowing into an AI icon` |
| **수정 전 문제** | 결과물이 단순한 카툰 스타일로 생성되어 시네마틱 광고 톤과 불일치. 파티클의 규모감·긴장감이 부족 |
| **수정 방향** | ① 시네마틱 키워드 추가 ② 배경 색상 명시 ③ 파티클 종류와 발광 속성 구체화 ④ 수렴 행위를 동사로 명확히 표현 |
| **수정 후 프롬프트** | `An abstract digital visualization of thousands of tiny artworks, music notes, handwritten text, and painting fragments all flowing and converging into a single glowing AI neural network icon at the center. Deep dark navy space background, electric blue and white luminous particles, flowing data streams, cinematic, high contrast, dramatic, 4K.` |
| **수정 결과** | 어두운 우주 배경 위 파란 발광 파티클이 AI 아이콘으로 수렴하는 이미지 확보. 광고 톤앤매너와 일치 |

---

## 7. 타임라인 요약 / Timeline Summary

| 씬 | 구간 | 길이 | 핵심 내용 | 주요 도구 |
|----|------|------|-----------|-----------|
| 1 | 0~7초 | 7초 | 창작자의 손 (화가·피아니스트·작가 3컷) | Gemini + Runway |
| 2 | 7~17초 | 10초 | 창작물 → AI로 수렴하는 시각화 + 내레이션 | Gemini + Runway + ElevenLabs |
| 3 | 17~25초 | 8초 | 실루엣 창작자 + 분위기 전환 + 내레이션 | Gemini + Runway + ElevenLabs |
| 4 | 25~35초 | 10초 | 출처·허락·존중 3단계 행동 지침 | Gemini + Runway + ElevenLabs + CapCut |
| 5 | 35~40초 | 5초 | 슬로건 엔딩 카드 + AI 워터마크 | ElevenLabs + CapCut |
| **합계** | | **40초** | | |

---

## 8. 제작 체크리스트 / Production Checklist

**사전 준비**
- [ ] 공모전 공식 지정 음원 다운로드 → `04_audio/bgm_official.mp3`
- [ ] 공식 AI 워터마크 다운로드 → `etc/watermark_official.png`

**이미지 생성 (Gemini)**
- [ ] 씬 1-A : 화가의 손 → `02_text to img/v2(디벨롭)/scene01A_painter_v3_tight.png`
- [ ] 씬 1-B : 피아니스트의 손 → `02_text to img/v2(디벨롭)/scene01B_pianist_v3.png`
- [ ] 씬 1-C : 작가의 손 → `02_text to img/v2(디벨롭)/scene01C_writer_v3.png`
- [ ] 씬 2 : AI 파티클 수렴 → `02_text to img/v2(디벨롭)/scene02_ai_learning_v3.png`
- [ ] 씬 3 : 실루엣 창작자 → `02_text to img/v2(디벨롭)/scene03_creator_v3.png`
- [ ] 씬 4 : 공존 일러스트 → `02_text to img/v2(디벨롭)/scene04_coexist_v3.png`

**영상 변환 (Runway)**
- [ ] 씬 1-A → `03_img to vid/v2(디벨롭)_씬별영상/scene01A_painter_v3_motion.mp4`
- [ ] 씬 1-B → `03_img to vid/v2(디벨롭)_씬별영상/scene01B_pianist_v3_motion.mp4`
- [ ] 씬 1-C → `03_img to vid/v2(디벨롭)_씬별영상/scene01C_writer_v3_motion.mp4`
- [ ] 씬 2 → `03_img to vid/v2(디벨롭)_씬별영상/scene02_ai_learning_v3_motion.mp4`
- [ ] 씬 3 → `03_img to vid/v2(디벨롭)_씬별영상/scene03_creator_v3_motion.mp4`
- [ ] 씬 4 → `03_img to vid/v2(디벨롭)_씬별영상/scene04_coexist_v3_motion.mp4`

**내레이션 (ElevenLabs)**
- [ ] 씬 2 내레이션 → `04_audio/scene02_narration.mp3`
- [ ] 씬 3 내레이션 → `04_audio/scene03_narration.mp3`
- [ ] 씬 4 내레이션 → `04_audio/scene04_narration.mp3`
- [ ] 씬 5 내레이션 → `04_audio/scene05_narration.mp3`

**편집 통합 (CapCut)**
- [ ] 씬 1~5 컷 편집 및 연결
- [ ] 씬 4 텍스트 3단계 페이드인 삽입
- [ ] 씬 5 엔딩 카드 제작
- [ ] BGM 삽입 및 씬 5에서 페이드아웃
- [ ] AI 워터마크 우측 하단 삽입
- [ ] 최종 스펙 확인 : 40초 / 16:9 / 1920×1080 / H.264
- [ ] 최종 파일 저장 → `05_master/master_final_v1.mp4`

**출품 준비**
- [ ] SNS (유튜브 / 인스타그램 / 틱톡 중 택1) 업로드
- [ ] 해시태그 11개 등록
- [ ] URL 기록
- [ ] 홈페이지 접수 (2026.07.01~07.15)

---

*K-AI 콘텐츠 공모전 2026 | Track A. 대학(원)/일반부 AI 영상(광고)*
*문서 작성일 : 2026-06-14*
