"""
씬 5 엔딩 카드 Veo 영상 변환
만들기 전에, 한 번 더. - 타이포그래피 페이드인 5초 영상
"""

import time, base64, json
from pathlib import Path
import google.auth, google.auth.transport.requests, requests

PROJECT_ID = "project-d889d417-cdf3-442b-9b3"
LOCATION   = "us-central1"
MODEL      = "veo-2.0-generate-001"
API_BASE   = f"https://{LOCATION}-aiplatform.googleapis.com"

BASE_DIR = Path(__file__).parent.parent
IMG_PATH = BASE_DIR / "02_text to img" / "v2(디벨롭)" / "scene05_ending_card_v3.png"
OUT_PATH = BASE_DIR / "03_img to vid" / "v2(디벨롭)_씬별영상" / "scene05_ending_v3_motion.mp4"

PROMPT = (
    "Cinematic fade-in typography animation. The deep navy black screen slowly brightens from complete black, "
    "revealing the white Korean text 'Before You Create, Think Once More' glowing gently in the center. "
    "A very subtle ambient light pulses softly — warm amber from left, cool cyan-blue from right — "
    "illuminating the text edges with a barely visible glow. "
    "The text holds completely still, no movement except the initial fade-in. "
    "Camera absolutely static, locked off. Slow breathing atmosphere, cinematic, premium."
)

print("Google ADC 인증 중...")
creds, _ = google.auth.default(scopes=["https://www.googleapis.com/auth/cloud-platform"])
auth_req = google.auth.transport.requests.Request()
creds.refresh(auth_req)
print(f"  완료: {PROJECT_ID}")
print()

def get_headers():
    if credentials_expired():
        creds.refresh(auth_req)
    return {"Authorization": f"Bearer {creds.token}", "Content-Type": "application/json"}

def credentials_expired():
    return creds.expired or not creds.token

img_bytes = IMG_PATH.read_bytes()
print(f"[IMG] 이미지 로드: {len(img_bytes)//1024} KB")

# 작업 제출
url_submit = (
    f"{API_BASE}/v1beta1/projects/{PROJECT_ID}/locations/{LOCATION}"
    f"/publishers/google/models/{MODEL}:predictLongRunning"
)
payload = {
    "instances": [{
        "prompt": PROMPT,
        "image": {
            "bytesBase64Encoded": base64.b64encode(img_bytes).decode(),
            "mimeType": "image/png",
        },
    }],
    "parameters": {
        "aspectRatio": "16:9",
        "durationSeconds": 5,
        "sampleCount": 1,
        "personGeneration": "allow_adult",
    },
}
print("[VID] 작업 제출 중...")
resp = requests.post(url_submit, headers=get_headers(), json=payload, timeout=60)
resp.raise_for_status()
op_name = resp.json().get("name", "")
print(f"[OK] operation: ...{op_name[-50:]}")

# fetchPredictOperation 폴링
url_fetch_v1     = f"{API_BASE}/v1/projects/{PROJECT_ID}/locations/{LOCATION}/publishers/google/models/{MODEL}:fetchPredictOperation"
url_fetch_v1beta = f"{API_BASE}/v1beta1/projects/{PROJECT_ID}/locations/{LOCATION}/publishers/google/models/{MODEL}:fetchPredictOperation"

print("[VID] 완료 대기 중 (5초 영상)...")
waited = 0
response = None
while waited < 600:
    time.sleep(15)
    waited += 15
    for fetch_url in [url_fetch_v1, url_fetch_v1beta]:
        try:
            r = requests.post(fetch_url, headers=get_headers(), json={"operationName": op_name}, timeout=30)
            if r.status_code == 200:
                data = r.json()
                done = data.get("done", False)
                print(f"  [...] {waited}s 경과 (done={done})")
                if done:
                    response = data.get("response", {})
                break
        except Exception as e:
            print(f"  [WARN] {e}")
    if response is not None:
        break

if response is None:
    print("[ERR] 타임아웃 또는 응답 없음")
    exit(1)

# 저장
videos = response.get("videos", [])
if videos and videos[0].get("bytesBase64Encoded"):
    OUT_PATH.write_bytes(base64.b64decode(videos[0]["bytesBase64Encoded"]))
    size_mb = OUT_PATH.stat().st_size / (1024 * 1024)
    print(f"[OK] 저장 완료: {OUT_PATH.name} ({size_mb:.1f} MB)")
    print("[DONE]")
else:
    print(f"[ERR] 영상 데이터 없음. 응답 키: {list(response.keys())}")
    print(json.dumps(response, ensure_ascii=False)[:400])
