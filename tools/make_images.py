#!/usr/bin/env python3
"""AI 에이전트 실전 개발 - 표지 및 설명용 이미지 생성 (PIL)."""
from PIL import Image, ImageDraw, ImageFont
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "..", "assets")
os.makedirs(ASSETS, exist_ok=True)

def font(size, bold=True):
    for p in ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

NAVY = (15, 25, 55); TEAL = (0, 150, 135); LIGHT = (235, 245, 250)
WHITE = (255, 255, 255); GRAY = (90, 100, 115); ACCENT = (255, 140, 0)

def cover():
    img = Image.new("RGB", (1000, 1300), NAVY); d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 1000, 520], fill=TEAL)
    d.rectangle([0, 520, 1000, 528], fill=ACCENT)
    d.text((80, 150), "AI 에이전트", font=font(96), fill=WHITE)
    d.text((80, 270), "실전 개발", font=font(96), fill=WHITE)
    d.text((80, 420), "일을 끝까지 해내는 AI 시스템 만들기", font=font(38, False), fill=WHITE)
    d.text((80, 620), "5가지 워크플로우 패턴부터", font=font(44, False), fill=LIGHT)
    d.text((80, 690), "멀티 에이전트 운영까지", font=font(44, False), fill=LIGHT)
    d.text((80, 820), "설계 · 평가 · 가드레일 · 운영", font=font(40), fill=ACCENT)
    d.text((80, 1060), "저자 이준수", font=font(44, False), fill=GRAY)
    d.text((80, 1140), "기준일 2026-10-09", font=font(36, False), fill=GRAY)
    img.save(os.path.join(ASSETS, "cover.png"))

def diagram(name, title, boxes, arrows):
    img = Image.new("RGB", (1200, 700), WHITE); d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 1200, 110], fill=NAVY)
    d.text((60, 32), title, font=font(44), fill=WHITE)
    for (x, y, w, h, label, sub, color) in boxes:
        d.rectangle([x, y, x + w, y + h], fill=color, outline=NAVY, width=3)
        d.text((x + 20, y + 18), label, font=font(36), fill=NAVY)
        if sub: d.text((x + 20, y + 68), sub, font=font(28, False), fill=GRAY)
    for (x1, y1, x2, y2, label) in arrows:
        d.line([x1, y1, x2, y2], fill=ACCENT, width=5)
        d.polygon([(x2, y2), (x2 - 18, y2 - 10), (x2 - 18, y2 + 10)], fill=ACCENT)
        if label:
            mx, my = (x1 + x2) // 2, (y1 + y2) // 2 - 34
            d.text((mx - 60, my), label, font=font(26, False), fill=GRAY)
    img.save(os.path.join(ASSETS, name))

B1 = TEAL; B2 = (255, 200, 120); B3 = (150, 200, 255)

diagram("fig-agent-vs-workflow.png", "워크플로우와 에이전트",
    [(60, 200, 480, 140, "워크플로우", "정해진 경로 (기차)", B2),
     (660, 200, 480, 140, "에이전트", "스스로 정하는 경로 (택시)", B1)],
    [])

diagram("fig-patterns.png", "5가지 워크플로우 패턴",
    [(60, 160, 200, 110, "체이닝", "순서대로", B1),
     (280, 160, 200, 110, "라우팅", "분류 후 분기", B2),
     (500, 160, 200, 110, "병렬화", "동시 처리", B3),
     (720, 160, 200, 110, "오케-워커", "나누고 합치기", B1),
     (940, 160, 200, 110, "평가-최적", "반복 개선", B2),
     (400, 420, 400, 110, "복잡한 작업", "패턴을 조합해 설계", LIGHT)],
    [(160, 270, 500, 420, ""), (380, 270, 550, 420, ""),
     (600, 270, 600, 420, ""), (820, 270, 650, 420, ""), (1040, 270, 700, 420, "")])

diagram("fig-orchestration.png", "코디네이터-서브에이전트",
    [(450, 150, 300, 110, "코디네이터", "나누고 합치기", B2),
     (60, 400, 300, 110, "서브에이전트 A", "스스로 판단", B1),
     (450, 400, 300, 110, "서브에이전트 B", "스스로 판단", B1),
     (840, 400, 300, 110, "서브에이전트 C", "스스로 판단", B1)],
    [(600, 260, 210, 400, ""), (600, 260, 600, 400, ""), (600, 260, 990, 400, "")])

diagram("fig-eval-loop.png", "평가와 운영 사이클",
    [(60, 200, 260, 120, "설계", "패턴 선택", B1),
     (380, 200, 260, 120, "구축", "도구와 프롬프트", B2),
     (700, 200, 260, 120, "평가", "테스트 케이스", B3),
     (380, 450, 260, 120, "운영", "모니터링", LIGHT)],
    [(320, 260, 380, 260, ""), (640, 260, 700, 260, ""),
     (830, 320, 830, 450, ""), (380, 510, 190, 320, "")])

diagram("fig-project.png", "실전 프로젝트: 고객 문의 처리 에이전트",
    [(60, 170, 260, 120, "라우팅", "문의 분류", B1),
     (380, 170, 260, 120, "종류별 처리", "체이닝", B2),
     (700, 170, 260, 120, "휴먼인더루프", "낮은 확신은 사람에게", B3),
     (380, 430, 260, 120, "평가·운영", "통과율과 비용", LIGHT)],
    [(320, 230, 380, 230, ""), (640, 230, 700, 230, ""),
     (510, 290, 510, 430, "")])

cover()
print("done:", sorted(os.listdir(ASSETS)))
