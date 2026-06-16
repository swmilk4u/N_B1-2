"""
Google Cloud Text-to-Speech Chirp3-HD 음성으로 내레이션 생성
캠페인: 만들기 전에, 한 번 더 (K-AI 콘텐츠 공모전 2026)
씬 2·3·4·5 내레이션 MP3 생성 → 04_audio/
"""

import base64
import json
from pathlib import Path

import google.auth
import google.auth.transport.requests
import requests

# ─────────────────────────────────────────────────────────
# 설정
# ─────────────────────────────────────────────────────────
PROJECT_ID = "project-d889d417-cdf3-442b-9b3"
TTS_URL    = "https://texttospeech.googleapis.com/v1/text:synthesize"

BASE_DIR  = Path(__file__).parent.parent
OUT_DIR   = BASE_DIR / "04_audio"
OUT_DIR.mkdir(exist_ok=True)

# ─────────────────────────────────────────────────────────
# 씬별 내레이션 설정
# Chirp3-HD: Google 최신 HD 한국어 신경망 음성
#   남성(중후, 차분): Charon / Algenib / Umbriel
#   여성(따뜻, 부드): Aoede / Kore / Leda
# Note: Chirp3-HD는 speakingRate/pitch 파라미터 미지원
#       → SSML prosody 태그 또는 Neural2로 대체
# ─────────────────────────────────────────────────────────
NARRATIONS = [
    {
        "output": "scene02_narration.mp3",
        "ssml": (
            "<speak>"
            "이 모든 창작물이,"
            "<break time='800ms'/>"
            "AI를 만들었습니다."
            "</speak>"
        ),
        "voice":  "ko-KR-WaveNet-C",     # 남성 WaveNet-C (다큐멘터리 성우 톤, 신뢰감 있고 부드러움)
        "rate":   0.94,
        "pitch":  0.0,
        "desc":   "씬 2 — AI 학습 시각화 (차분, 낮음, 감성적)",
    },
    {
        "output": "scene03_narration.mp3",
        "ssml": (
            "<speak>"
            "이제,"
            "<break time='200ms'/>"
            "당신도 창작자입니다."
            "</speak>"
        ),
        "voice":  "ko-KR-WaveNet-A",     # 여성 WaveNet-A (차분하고 성숙한 인간다운 톤)
        "rate":   0.95,
        "pitch":   0.0,
        "desc":   "씬 3 — 당신도 창작자 (따뜻하고 부드러운, 확신)",
    },
    {
        "output": "scene04_narration.mp3",
        "ssml": (
            "<speak>"
            "출처를 밝히고,"
            "<break time='600ms'/>"
            "허락을 구하고,"
            "<break time='600ms'/>"
            "창작자를 존중합니다."
            "</speak>"
        ),
        "voice":  "ko-KR-WaveNet-C",     # 남성 WaveNet-C (명확하고 신뢰감 높은 어조)
        "rate":   0.95,
        "pitch":   0.0,
        "desc":   "씬 4 — 행동 지침 (명확, 또렷, 문장 간 간격)",
    },
    {
        "output": "scene05_narration.mp3",
        "ssml": (
            "<speak>"
            "만들기 전에,"
            "<break time='900ms'/>"
            "한 번 더."
            "</speak>"
        ),
        "voice":  "ko-KR-WaveNet-C",     # 남성 WaveNet-C (여운 있는 깊은 엔딩)
        "rate":   0.92,
        "pitch":  0.0,
        "desc":   "씬 5 — 엔딩 슬로건 (여운, 낮음, 조용히)",
    },
]

# ─────────────────────────────────────────────────────────
# 인증
# ─────────────────────────────────────────────────────────
print("Google ADC 인증 중...")
creds, _ = google.auth.default(
    scopes=["https://www.googleapis.com/auth/cloud-platform"]
)
auth_req = google.auth.transport.requests.Request()
creds.refresh(auth_req)
print(f"  완료: {PROJECT_ID}\n")


def get_headers():
    if creds.expired or not creds.token:
        creds.refresh(auth_req)
    return {
        "Authorization": f"Bearer {creds.token}",
        "Content-Type": "application/json",
        "x-goog-user-project": PROJECT_ID,
    }


def synthesize(narr: dict) -> bytes:
    """TTS API 호출, MP3 bytes 반환"""
    input_field = {"ssml": narr["ssml"]}

    payload = {
        "input": input_field,
        "voice": {
            "languageCode": "ko-KR",
            "name": narr["voice"],
        },
        "audioConfig": {
            "audioEncoding": "MP3",
            "speakingRate": narr["rate"],
            "pitch": narr["pitch"],
            "effectsProfileId": ["large-home-entertainment-class-device"],
        },
    }

    resp = requests.post(TTS_URL, headers=get_headers(), json=payload, timeout=30)
    if resp.status_code != 200:
        raise ValueError(f"HTTP {resp.status_code}: {resp.text[:400]}")
    audio_b64 = resp.json().get("audioContent", "")
    if not audio_b64:
        raise ValueError("audioContent 없음")
    return base64.b64decode(audio_b64)


# ─────────────────────────────────────────────────────────
# 생성
# ─────────────────────────────────────────────────────────
total = len(NARRATIONS)
success = 0

for idx, narr in enumerate(NARRATIONS, 1):
    out_path = OUT_DIR / narr["output"]
    print(f"[{idx}/{total}] {narr['desc']}")
    print(f"  음성: {narr['voice']}  |  속도: {narr['rate']}  |  피치: {narr['pitch']}")

    try:
        audio_bytes = synthesize(narr)
        out_path.write_bytes(audio_bytes)
        size_kb = len(audio_bytes) / 1024
        print(f"  [OK] 저장 완료: {out_path.name} ({size_kb:.0f} KB)")
        success += 1
    except Exception as e:
        print(f"  [ERR] {e}")
    print()

# ─────────────────────────────────────────────────────────
# 결과
# ─────────────────────────────────────────────────────────
print("=" * 55)
print(f"완료: {success}/{total}")
print("=" * 55)
for f in sorted(OUT_DIR.glob("*.mp3")):
    print(f"  [OK] {f.name} ({f.stat().st_size/1024:.0f} KB)")
print("\n[DONE]")
