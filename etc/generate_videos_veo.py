"""
Veo API Image-to-Video 생성 스크립트 (fetchPredictOperation 방식)
캠페인: 만들기 전에, 한 번 더 (K-AI 콘텐츠 공모전 2026)
v3 셀렉티브 컬러 이미지 -> 씬별 MP4 영상 변환
"""

import time
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
LOCATION   = "us-central1"
MODEL      = "veo-2.0-generate-001"
API_BASE   = f"https://{LOCATION}-aiplatform.googleapis.com"

BASE_DIR   = Path(__file__).parent.parent
IMG_DIR    = BASE_DIR / "02_text to img" / "v2(디벨롭)"
OUT_DIR    = BASE_DIR / "03_img to vid" / "v2(디벨롭)_씬별영상"
OUT_DIR.mkdir(exist_ok=True)

# ─────────────────────────────────────────────────────────
# 씬별 설정
# ─────────────────────────────────────────────────────────
SCENES = [
    {
        "image":   "scene01A_painter_v3_tight.png",
        "output":  "scene01A_painter_v3_motion.mp4",
        "seconds": 5,
        "prompt": (
            "The hand slowly raises the brush and makes a single deliberate stroke on canvas. "
            "Gentle cinematic slow motion, warm amber paint particles catch the light. "
            "Selective color: only hand in warm amber tones, background stays monochrome grey."
        ),
    },
    {
        "image":   "scene01A_painter_v3_full.png",
        "output":  "scene01A_painter_v3_full_motion.mp4",
        "seconds": 5,
        "prompt": (
            "The Korean male painter steps back from the canvas, studies his work thoughtfully, "
            "then leans forward to add a bold decisive brush stroke. Camera gently pushes in. "
            "Cinematic slow motion. Warm amber colored figure moves against grey desaturated studio."
        ),
    },
    {
        "image":   "scene01B_pianist_v3.png",
        "output":  "scene01B_pianist_v3_motion.mp4",
        "seconds": 5,
        "prompt": (
            "The Korean female pianist's fingers gently press piano keys one by one, slow and deliberate. "
            "Her head sways slightly with the music. Cyan-blue glow pulses on fingertips with each key press. "
            "Cinematic slow motion. Vivid colored figure against completely grey background."
        ),
    },
    {
        "image":   "scene01C_writer_v3.png",
        "output":  "scene01C_writer_v3_motion.mp4",
        "seconds": 5,
        "prompt": (
            "The Korean female creator types rhythmically on a mechanical keyboard with precision. "
            "Cyan-blue monitor glow flickers softly on her face as content appears on screen. "
            "Subtle motion blur on fingers. Cinematic slow motion. Colored figure against grey background."
        ),
    },
    {
        "image":   "scene02_ai_learning_v3.png",
        "output":  "scene02_ai_learning_v3_motion.mp4",
        "seconds": 8,
        "prompt": (
            "Thousands of golden amber particle streams swirl and accelerate inward from all directions, "
            "converging into the central cyan-blue AI neural orb which pulses and expands with brilliant light. "
            "Epic cinematic VFX. Vivid amber and cyan particles animate against grey void background."
        ),
    },
    {
        "image":   "scene03_creator_v3.png",
        "output":  "scene03_creator_v3_motion.mp4",
        "seconds": 6,
        "prompt": (
            "Korean female creator slowly lifts her gaze from the keyboard, eyes rising to meet glowing laptop screen. "
            "A soft hopeful smile forms. Camera gently pushes in toward her face. "
            "Cinematic slow motion. Colorful figure warms against grey monochrome environment."
        ),
    },
    {
        "image":   "scene03_creator_silhouette_v3.png",
        "output":  "scene03_creator_silhouette_v3_motion.mp4",
        "seconds": 6,
        "prompt": (
            "Female silhouette slowly turns toward the windows, amber rim light traces her outline beautifully. "
            "Camera slowly zooms in. Golden dust particles drift upward in the light. "
            "Cyan-blue laptop screen glows softly. Epic cinematic slow motion."
        ),
    },
    {
        "image":   "scene04_coexist_v3.png",
        "output":  "scene04_coexist_v3_motion.mp4",
        "seconds": 8,
        "prompt": (
            "The warm amber painter on the left and the cyan-blue AI creator on the right "
            "simultaneously turn toward each other and nod gently with warm smiles. "
            "A soft white glow blooms between them. Camera slowly pulls back to show both fully. "
            "Cinematic smooth motion. Both colorful figures against grey desaturated background."
        ),
    },
]

# ─────────────────────────────────────────────────────────
# Google ADC 인증
# ─────────────────────────────────────────────────────────
print("Google ADC 인증 중...")
credentials, _ = google.auth.default(
    scopes=["https://www.googleapis.com/auth/cloud-platform"]
)
auth_req = google.auth.transport.requests.Request()
credentials.refresh(auth_req)
print(f"  인증 완료: {PROJECT_ID}")
print()


def get_headers():
    if credentials.expired or not credentials.token:
        credentials.refresh(auth_req)
    return {
        "Authorization": f"Bearer {credentials.token}",
        "Content-Type": "application/json",
    }


def submit_job(image_bytes: bytes, prompt: str, seconds: int) -> str:
    """predictLongRunning 제출, operation name 반환"""
    url = (
        f"{API_BASE}/v1beta1/projects/{PROJECT_ID}/locations/{LOCATION}"
        f"/publishers/google/models/{MODEL}:predictLongRunning"
    )
    payload = {
        "instances": [{
            "prompt": prompt,
            "image": {
                "bytesBase64Encoded": base64.b64encode(image_bytes).decode(),
                "mimeType": "image/png",
            },
        }],
        "parameters": {
            "aspectRatio": "16:9",
            "durationSeconds": seconds,
            "sampleCount": 1,
            "personGeneration": "allow_adult",
        },
    }
    resp = requests.post(url, headers=get_headers(), json=payload, timeout=60)
    resp.raise_for_status()
    data = resp.json()
    op_name = data.get("name", "")
    if not op_name:
        raise ValueError(f"operation name 없음. 응답: {json.dumps(data)[:400]}")
    return op_name


def fetch_operation(op_name: str) -> dict:
    """fetchPredictOperation으로 작업 상태 조회"""
    # v1 먼저, 실패 시 v1beta1
    for version in ("v1", "v1beta1"):
        url = (
            f"{API_BASE}/{version}/projects/{PROJECT_ID}/locations/{LOCATION}"
            f"/publishers/google/models/{MODEL}:fetchPredictOperation"
        )
        try:
            resp = requests.post(
                url,
                headers=get_headers(),
                json={"operationName": op_name},
                timeout=30,
            )
            if resp.status_code == 200:
                return resp.json()
        except Exception:
            continue
    raise RuntimeError(f"fetchPredictOperation 실패 (op={op_name[-40:]})")


def poll_until_done(op_name: str, interval: int = 20, max_wait: int = 600) -> dict:
    """완료까지 폴링, response 반환"""
    waited = 0
    while waited < max_wait:
        time.sleep(interval)
        waited += interval
        try:
            data = fetch_operation(op_name)
            done = data.get("done", False)
            print(f"    [...] {waited}s 경과 (done={done})")
            if done:
                if "error" in data:
                    raise RuntimeError(f"작업 실패: {data['error']}")
                return data.get("response", {})
        except RuntimeError:
            raise
        except Exception as e:
            print(f"    [WARN] 폴링 오류: {e}")
    raise TimeoutError(f"최대 대기 시간({max_wait}s) 초과")


def save_video(response: dict, out_path: Path) -> bool:
    """response에서 비디오 추출 후 저장"""
    videos = response.get("videos", [])
    for v in videos:
        b64 = v.get("bytesBase64Encoded")
        if b64:
            out_path.write_bytes(base64.b64decode(b64))
            return True
    # fallback: predictions
    for pred in response.get("predictions", []):
        b64 = pred.get("bytesBase64Encoded") or pred.get("videoBytes")
        if b64:
            out_path.write_bytes(base64.b64decode(b64))
            return True
    print(f"    [WARN] 비디오 데이터 없음. 응답 키: {list(response.keys())}")
    return False


# ─────────────────────────────────────────────────────────
# 씬별 실행
# ─────────────────────────────────────────────────────────
total = len(SCENES)
success = 0

for idx, scene in enumerate(SCENES, 1):
    img_path = IMG_DIR / scene["image"]
    out_path = OUT_DIR / scene["output"]

    print(f"[{idx}/{total}] {scene['image']}")

    if not img_path.exists():
        print(f"  [WARN] 이미지 없음 -- 건너뜁니다.\n")
        continue

    if out_path.exists() and out_path.stat().st_size > 10000:
        print(f"  [OK] 이미 존재: {out_path.name} -- 건너뜁니다.\n")
        success += 1
        continue

    img_bytes = img_path.read_bytes()
    print(f"  [IMG] 로드 완료 ({len(img_bytes)//1024} KB)")

    try:
        print("  [VID] 작업 제출 중...")
        op_name = submit_job(img_bytes, scene["prompt"], scene["seconds"])
        print(f"  [OK] operation: ...{op_name[-50:]}")

        print(f"  [VID] 완료 대기 중 ({scene['seconds']}초 영상)...")
        response = poll_until_done(op_name, interval=15, max_wait=600)

        if save_video(response, out_path):
            size_mb = out_path.stat().st_size / (1024 * 1024)
            print(f"  [OK] 저장 완료: {out_path.name} ({size_mb:.1f} MB)")
            success += 1
        else:
            print(f"  [ERR] 저장 실패")

    except Exception as e:
        print(f"  [ERR] {e}")

    print()

# ─────────────────────────────────────────────────────────
# 결과 요약
# ─────────────────────────────────────────────────────────
print("=" * 55)
print(f"완료: {success}/{total}")
print("=" * 55)
for f in sorted(OUT_DIR.glob("*.mp4")):
    print(f"  [OK] {f.name} ({f.stat().st_size/1024/1024:.1f} MB)")
print("[DONE]")
