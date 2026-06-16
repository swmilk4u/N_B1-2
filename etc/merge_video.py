"""
K-AI 콘텐츠 공모전 2026 출품 광고 영상 자동 렌더러
FFmpeg 활용 비디오 클립 병합 + BGM 믹스 + 내레이션 합성 + 자막 오버레이 + 워터마크 추가
스펙: 40초, 1920x1080 (1080p), 24fps, H.264 / AAC
"""

import subprocess
import sys
from pathlib import Path

# ─────────────────────────────────────────────────────────
# 경로 정의
# ─────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).parent.parent
SOURCE_DIR = BASE_DIR / "02_sorce"
AUDIO_DIR = BASE_DIR / "04_audio"
OUTPUT_DIR = BASE_DIR / "05_PJ"
OUTPUT_DIR.mkdir(exist_ok=True)

MASTER_DIR = BASE_DIR / "99_master"
MASTER_DIR.mkdir(exist_ok=True)

# 1. 비디오 클립 경로
VIDEOS = [
    SOURCE_DIR / "scene01A_painter_v3_motion.mp4",        # [0] 씬 1-A 타이트
    SOURCE_DIR / "scene01A_painter_v3_full_motion.mp4",   # [1] 씬 1-A 풀
    SOURCE_DIR / "scene01B_pianist_v3_motion.mp4",        # [2] 씬 1-B 건반
    SOURCE_DIR / "scene01C_writer_v3_motion.mp4",         # [3] 씬 1-C 타이핑
    SOURCE_DIR / "scene02_ai_learning_v3_motion.mp4",      # [4] 씬 2 AI 수렴 (8s)
    SOURCE_DIR / "scene03_creator_v3_motion.mp4",         # [5] 씬 3 창작자 (6s)
    SOURCE_DIR / "scene03_creator_silhouette_v3_motion.mp4", # [6] 씬 3 실루엣 (6s)
    SOURCE_DIR / "scene04_coexist_v3_motion.mp4",         # [7] 씬 4 공존 (8s)
    SOURCE_DIR / "scene05_ending_v3_motion.mp4",          # [8] 씬 5 엔딩 (5s)
]

# 2. 이미지 및 오디오 리소스
WATERMARK = SOURCE_DIR / "01 KT공모전 워터마크 및 지정음원" / "imgview.png"
BGM = SOURCE_DIR / "01 KT공모전 워터마크 및 지정음원" / "숏폼영상_지정음원v1.mp3"

NARRATIONS = [
    AUDIO_DIR / "scene02_narration.mp3",
    AUDIO_DIR / "scene03_narration.mp3",
    AUDIO_DIR / "scene04_narration.mp3",
    AUDIO_DIR / "scene05_narration.mp3",
]

def get_unique_output_path(base_path: Path) -> Path:
    """파일이 이미 존재할 경우 접미사(_1, _2 등)를 붙여 유니크한 경로 반환"""
    if not base_path.exists():
        return base_path
    
    parent = base_path.parent
    stem = base_path.stem
    ext = base_path.suffix
    
    counter = 1
    while True:
        new_path = parent / f"{stem}_{counter}{ext}"
        if not new_path.exists():
            return new_path
        counter += 1

BASE_OUTPUT = MASTER_DIR / "master_final_v3.mp4"
OUTPUT_V3_MASTER = get_unique_output_path(BASE_OUTPUT)

# ─────────────────────────────────────────────────────────
# 리소스 검증
# ─────────────────────────────────────────────────────────
print("에셋 존재 여부 확인 중...")
missing_files = []

for idx, v in enumerate(VIDEOS):
    if not v.exists():
        missing_files.append(f"비디오 씬{idx+1}: {v}")

if not WATERMARK.exists():
    missing_files.append(f"워터마크: {WATERMARK}")

if not BGM.exists():
    missing_files.append(f"지정 BGM: {BGM}")

for idx, n in enumerate(NARRATIONS, 2):
    if not n.exists():
        missing_files.append(f"내레이션 씬{idx}: {n}")

if missing_files:
    print("\n[오류] 다음 에셋 파일이 존재하지 않습니다:")
    for f in missing_files:
        print(f"  - {f}")
    sys.exit(1)

print("  모든 리소스 확인 완료! 렌더링 작업을 시작합니다.\n")

# ─────────────────────────────────────────────────────────
# FFmpeg 필터그래프 조립
# ─────────────────────────────────────────────────────────

# 1. 입력 인자 조립
# 비디오 인풋: 0 ~ 8
# 워터마크 인풋: 9
# BGM 인풋: 10
# 내레이션 인풋: 11 ~ 14
cmd = ["ffmpeg", "-y"]
for v in VIDEOS:
    cmd.extend(["-i", str(v)])
cmd.extend(["-i", str(WATERMARK)])
cmd.extend(["-i", str(BGM)])
for n in NARRATIONS:
    cmd.extend(["-i", str(n)])

# 2. 비디오 필터 구성
# 각 씬별 trim 및 스케일(1920x1080), setsar=1 처리
# 씬 2(8초 -> 10초)와 씬 4(8초 -> 10초)는 setpts=1.25*PTS를 적용하여 0.8배속 연장
v_filter = (
    # 씬 1-A 타이트 (0 ~ 1.75초)
    "[0:v]trim=0:1.75,setpts=PTS-STARTPTS,scale=1920:1080,setsar=1[v0];"
    # 씬 1-A 풀 (0 ~ 1.75초)
    "[1:v]trim=0:1.75,setpts=PTS-STARTPTS,scale=1920:1080,setsar=1[v1];"
    # 씬 1-B 건반 (0 ~ 1.75초)
    "[2:v]trim=0:1.75,setpts=PTS-STARTPTS,scale=1920:1080,setsar=1[v2];"
    # 씬 1-C 타이핑 (0 ~ 1.75초)
    "[3:v]trim=0:1.75,setpts=PTS-STARTPTS,scale=1920:1080,setsar=1[v3];"
    # 씬 2 AI 수렴 (8초 -> 10초)
    "[4:v]scale=1920:1080,setsar=1,setpts=1.25*PTS[v4];"
    # 씬 3 창작자 (0 ~ 4.0초)
    "[5:v]trim=0:4.0,setpts=PTS-STARTPTS,scale=1920:1080,setsar=1[v5];"
    # 씬 3 실루엣 (0 ~ 4.0초)
    "[6:v]trim=0:4.0,setpts=PTS-STARTPTS,scale=1920:1080,setsar=1[v6];"
    # 씬 4 공존 (8초 -> 10초)
    "[7:v]scale=1920:1080,setsar=1,setpts=1.25*PTS[v7];"
    # 씬 5 엔딩 (5.0초)
    "[8:v]scale=1920:1080,setsar=1,setpts=PTS-STARTPTS[v8];"
    
    # 9개 비디오 연결 (총 40.0초)
    "[v0][v1][v2][v3][v4][v5][v6][v7][v8]concat=n=9:v=1:a=0[v_concat];"
)

# 자막 폰트 파일 경로 이스케이프 처리 (Windows 백슬래시를 슬래시로 변경하고 콜론 이스케이프)
font_path = "C\\:/Windows/Fonts/malgunbd.ttf"

# 자막 오버레이 (씬 4 구간 25~35초 내에 3단계 순차 강조 - 오디오 발화 싱크 보정)
v_filter += (
    f"[v_concat]drawtext=fontfile='{font_path}':text='출처를 밝히고,':fontcolor=white:fontsize=56"
    ":bordercolor=black:borderw=3:x=(w-text_w)/2:y=h-180:enable='between(t,25.5,27.6)',"
    f"drawtext=fontfile='{font_path}':text='허락을 구하고,':fontcolor=white:fontsize=56"
    ":bordercolor=black:borderw=3:x=(w-text_w)/2:y=h-180:enable='between(t,27.6,29.2)',"
    f"drawtext=fontfile='{font_path}':text='창작자를 존중합니다.':fontcolor=white:fontsize=56"
    ":bordercolor=black:borderw=3:x=(w-text_w)/2:y=h-180:enable='between(t,29.2,35.0)'[v_sub];"
)

# 워터마크 오버레이 (imgview.png 크기를 150x150으로 줄이고 우측 상단 모서리에 배치)
v_filter += (
    "[9:v]scale=150:150[wm];"
    "[v_sub][wm]overlay=x=main_w-overlay_w-50:y=50[v_final];"
)

# 3. 오디오 필터 구성
# - BGM (10): 40초로 자르고, 볼륨 0.2로 낮춘 뒤, 엔딩 3초(37~40초) 동안 페이드아웃
# - 내레이션 (11~14): 모노 오디오를 스테레오로 믹싱, 볼륨을 1.6배로 올리고 각 씬 타이밍에 맞춰 딜레이
# - 믹싱 후 loudnorm 필터를 적용하여 최종 볼륨을 0dB ~ -5dB 표준(True Peak -1.5dB)으로 노멀라이즈
a_filter = (
    "[10:a]atrim=0:40,asetpts=PTS-STARTPTS,volume=0.20,afade=t=out:st=37:d=3[bgm];"
    "[11:a]pan=stereo|c0=c0|c1=c0,volume=1.6,adelay=7800|7800[n2];"      # 씬 2 내레이션 (7.8초에 재생)
    "[12:a]pan=stereo|c0=c0|c1=c0,volume=1.6,adelay=18000|18000[n3];"    # 씬 3 내레이션 (18.0초에 재생)
    "[13:a]pan=stereo|c0=c0|c1=c0,volume=1.6,adelay=26000|26000[n4];"    # 씬 4 내레이션 (26.0초에 재생)
    "[14:a]pan=stereo|c0=c0|c1=c0,volume=1.6,adelay=35500|35500[n5];"    # 씬 5 내레이션 (35.5초에 재생)
    
    # BGM과 내레이션 오디오 합성
    "[bgm][n2][n3][n4][n5]amix=inputs=5:duration=first:dropout_transition=0[a_mixed];"
    # EBU R128 표준에 의거하여 평균 음량을 조절하고 최대 피크를 -1.5dB로 제한하여 0dB ~ -5dB 수준으로 확보
    "[a_mixed]loudnorm=I=-14:TP=-1.5:LRA=11[a_final]"
)

# 4. 전체 필터 추가
cmd.extend(["-filter_complex", v_filter + a_filter])

# 5. 매핑 및 코덱 옵션 지정
cmd.extend([
    "-map", "[v_final]",
    "-map", "[a_final]",
    "-c:v", "libx264",
    "-pix_fmt", "yuv420p",
    "-r", "24",
    "-c:a", "aac",
    "-b:a", "192k",
    "-t", "40.0",
    str(OUTPUT_V3_MASTER)
])

# ─────────────────────────────────────────────────────────
# 실행
# ─────────────────────────────────────────────────────────
print("=" * 60)
print("FFmpeg 합성 프로세스를 시작합니다...")
print(f"출력 마스터 경로: {OUTPUT_V3_MASTER}")
print("=" * 60)

try:
    process = subprocess.run(cmd, capture_output=True, text=True, check=True)
    print("렌더링 성공! 마스터 파일이 정상적으로 생성되었습니다.")

except subprocess.CalledProcessError as e:
    print("\n[오류] FFmpeg 실행 실패:")
    print("Stdout:", e.stdout)
    print("Stderr:", e.stderr)
    sys.exit(1)

print("\n[DONE] 최종 광고 영상 합성 작업 완료!")
