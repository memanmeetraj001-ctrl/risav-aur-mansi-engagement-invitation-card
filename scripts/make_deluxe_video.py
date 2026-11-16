import os
import math
import random
import subprocess
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BASE_DIR = r"C:\Users\meman\.gemini\antigravity\scratch\risav-aur-mansi-engagement-invitation-card"
PUBLIC_DIR = os.path.join(BASE_DIR, "public")
FONT_DIR = os.path.join(BASE_DIR, "assets", "fonts")
BRAIN_DIR = r"C:\Users\meman\.gemini\antigravity\brain\7967065d-c585-4328-922a-43713e722ed7"

WIDTH, HEIGHT = 1080, 1920
FPS = 30
DURATION = 30
TOTAL_FRAMES = FPS * DURATION

OUTPUT_VIDEO = os.path.join(PUBLIC_DIR, "video", "mansi-risav-engagement.mp4")
AUDIO_FILE = os.path.join(PUBLIC_DIR, "audio", "mansi-risav-engagement-song.mp3")

# Load Fonts
FONT_CINZEL_XL = ImageFont.truetype(os.path.join(FONT_DIR, "CinzelDecorative-Bold.ttf"), 68)
FONT_CINZEL_LG = ImageFont.truetype(os.path.join(FONT_DIR, "CinzelDecorative-Bold.ttf"), 50)
FONT_CINZEL_MD = ImageFont.truetype(os.path.join(FONT_DIR, "CinzelDecorative-Bold.ttf"), 38)
FONT_CINZEL_SM = ImageFont.truetype(os.path.join(FONT_DIR, "CinzelDecorative-Bold.ttf"), 26)

FONT_VIBES_HERO = ImageFont.truetype(os.path.join(FONT_DIR, "GreatVibes-Regular.ttf"), 105)
FONT_VIBES_LG = ImageFont.truetype(os.path.join(FONT_DIR, "GreatVibes-Regular.ttf"), 80)
FONT_VIBES_MD = ImageFont.truetype(os.path.join(FONT_DIR, "GreatVibes-Regular.ttf"), 58)

FONT_ALEX_LG = ImageFont.truetype(os.path.join(FONT_DIR, "AlexBrush-Regular.ttf"), 64)
FONT_ALEX_MD = ImageFont.truetype(os.path.join(FONT_DIR, "AlexBrush-Regular.ttf"), 50)

FONT_SERIF_BOLD = ImageFont.truetype(r"C:\Windows\Fonts\georgiab.ttf", 30)
FONT_SERIF_REG = ImageFont.truetype(r"C:\Windows\Fonts\georgia.ttf", 28)
FONT_SERIF_SM = ImageFont.truetype(r"C:\Windows\Fonts\georgia.ttf", 24)
FONT_SANS_BOLD = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 26)

# Colors
MAROON_DEEP = (45, 2, 9)
MAROON_ROYAL = (92, 8, 26)
MAROON_RICH = (125, 16, 38)
GOLD_LIGHT = (255, 242, 190)
GOLD_BRIGHT = (250, 220, 115)
GOLD_METALLIC = (218, 175, 60)
GOLD_DARK = (165, 125, 30)
IVORY_CREAM = (255, 252, 245)
WHITE = (255, 255, 255)
ROSE_RED = (235, 45, 80)
ROSE_PINK = (255, 160, 185)

# Load Media
img_proposal = Image.open(os.path.join(PUBLIC_DIR, "images", "couple-proposal.jpg")).convert("RGBA")
img_portrait = Image.open(os.path.join(PUBLIC_DIR, "images", "couple-portrait.jpg")).convert("RGBA")
img_terms = Image.open(os.path.join(PUBLIC_DIR, "images", "couple-terms.jpg")).convert("RGBA")
img_ganesha = Image.open(os.path.join(PUBLIC_DIR, "images", "ganesha-gold.png")).convert("RGBA")
img_gublu = Image.open(os.path.join(PUBLIC_DIR, "images", "gublu-invitation.jpg")).convert("RGBA")

# Vector Math Functions to Draw Smooth Red Hearts & Rings (NO EMOJI FONT DEPENDENCY!)
def draw_vector_heart(d, cx, cy, size, fill_color=ROSE_RED, outline_color=ROSE_PINK):
    pts = []
    scale = size / 16.0
    for i in range(40):
        t = (2 * math.pi * i) / 40
        x = cx + (16 * (math.sin(t) ** 3)) * scale
        y = cy - (13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)) * scale
        pts.append((x, y))
    d.polygon(pts, fill=fill_color, outline=outline_color)

def draw_golden_ring(d, cx, cy, radius=20):
    d.ellipse([cx - radius, cy - radius, cx + radius, cy + radius], outline=GOLD_BRIGHT, width=4)
    d.ellipse([cx - radius + 3, cy - radius + 3, cx + radius - 3, cy + radius - 3], outline=GOLD_DARK, width=1)
    dx, dy = cx, cy - radius
    d.polygon([(dx, dy - 14), (dx + 11, dy - 3), (dx, dy + 5), (dx - 11, dy - 3)], fill=WHITE, outline=GOLD_BRIGHT)
    d.ellipse([dx - 16, dy - 18, dx + 16, dy + 14], fill=(255, 245, 200, 80))

# 3D Royal Velvet Background with Vignette & Golden Ornate Borders
def make_velvet_bg():
    bg = Image.new("RGBA", (WIDTH, HEIGHT), MAROON_DEEP)
    d = ImageDraw.Draw(bg)
    cx, cy = WIDTH // 2, HEIGHT // 2
    max_radius = math.sqrt(cx**2 + cy**2)
    for r in range(0, int(max_radius), 25):
        ratio = r / max_radius
        red = int(MAROON_ROYAL[0] * (1.0 - ratio * 0.75))
        green = int(MAROON_ROYAL[1] * (1.0 - ratio * 0.8))
        blue = int(MAROON_ROYAL[2] * (1.0 - ratio * 0.8))
        d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(red, green, blue, 255), width=26)
    
    overlay = Image.new("RGBA", (WIDTH, HEIGHT), (0,0,0,0))
    od = ImageDraw.Draw(overlay)
    
    m = 48
    od.rectangle([m, m, WIDTH - m, HEIGHT - m], outline=(218, 175, 60, 230), width=5)
    od.rectangle([m + 12, m + 12, WIDTH - m - 12, HEIGHT - m - 12], outline=(250, 220, 115, 120), width=2)
    od.rectangle([m + 22, m + 22, WIDTH - m - 22, HEIGHT - m - 22], outline=(218, 175, 60, 80), width=1)
    
    corner_size = 90
    corners = [
        (m, m, 1, 1),
        (WIDTH - m, m, -1, 1),
        (m, HEIGHT - m, 1, -1),
        (WIDTH - m, HEIGHT - m, -1, -1)
    ]
    for x, y, dx, dy in corners:
        od.arc([x - corner_size if dx == -1 else x,
                y - corner_size if dy == -1 else y,
                x if dx == -1 else x + corner_size,
                y if dy == -1 else y + corner_size],
               0, 360, fill=(250, 220, 115, 230), width=4)
        for step in [24, 48, 72]:
            od.line([(x, y + dy * step), (x + dx * (corner_size - step), y + dy * step)], fill=(218, 175, 60, 160), width=2)
            od.line([(x + dx * step, y), (x + dx * step, y + dy * (corner_size - step))], fill=(218, 175, 60, 160), width=2)
        od.polygon([(x + dx * 28, y + dy * 12), (x + dx * 34, y + dy * 28), (x + dx * 28, y + dy * 44), (x + dx * 22, y + dy * 28)], fill=(255, 230, 140, 240))
        
    od.line([(WIDTH//2 - 180, m + 35), (WIDTH//2 + 180, m + 35)], fill=(218, 175, 60, 190), width=2)
    od.polygon([(WIDTH//2, m + 26), (WIDTH//2 + 14, m + 35), (WIDTH//2, m + 44), (WIDTH//2 - 14, m + 35)], fill=(250, 220, 115, 255))
    
    od.line([(WIDTH//2 - 180, HEIGHT - m - 35), (WIDTH//2 + 180, HEIGHT - m - 35)], fill=(218, 175, 60, 190), width=2)
    od.polygon([(WIDTH//2, HEIGHT - m - 44), (WIDTH//2 + 14, HEIGHT - m - 35), (WIDTH//2, HEIGHT - m - 26), (WIDTH//2 - 14, HEIGHT - m - 35)], fill=(250, 220, 115, 255))

    return Image.alpha_composite(bg, overlay)

ROYAL_BG = make_velvet_bg()

# Precompute Rotating Sacred Mandala
def make_mandala(size=650):
    m = Image.new("RGBA", (size, size), (0,0,0,0))
    d = ImageDraw.Draw(m)
    cx, cy = size//2, size//2
    for r in range(40, size//2 - 20, 30):
        d.ellipse([cx-r, cy-r, cx+r, cy+r], outline=(250, 220, 115, 70), width=2)
    num_petals = 24
    for i in range(num_petals):
        angle = (2 * math.pi / num_petals) * i
        r1, r2 = size//2 - 80, size//2 - 20
        x1, y1 = cx + math.cos(angle) * r1, cy + math.sin(angle) * r1
        x2, y2 = cx + math.cos(angle) * r2, cy + math.sin(angle) * r2
        d.line([(x1, y1), (x2, y2)], fill=(218, 175, 60, 90), width=2)
        d.ellipse([x2-4, y2-4, x2+4, y2+4], fill=(255, 240, 180, 120))
    return m

MANDALA_IMG = make_mandala(700)

# 3D Dust Particles & Floating Rose Petals
random.seed(101)
PARTICLES = [
    {
        'x': random.randint(60, WIDTH - 60),
        'base_y': random.randint(50, HEIGHT),
        'speed': random.uniform(1.0, 2.8),
        'size': random.randint(3, 8),
        'type': random.choice(['gold_bokeh', 'star', 'sparkle', 'petal'])
    }
    for _ in range(50)
]

def draw_lux_particles(im, frame_num):
    d = ImageDraw.Draw(im)
    for p in PARTICLES:
        y = (p['base_y'] - frame_num * p['speed']) % (HEIGHT - 120) + 60
        x = p['x'] + math.sin((frame_num * 0.04) + p['base_y']) * 18
        if p['type'] == 'petal':
            s = p['size'] * 2.2
            rot = (frame_num * 0.05 + p['x'])
            dx, dy = math.cos(rot)*s, math.sin(rot)*(s*0.6)
            d.polygon([
                (x, y - s),
                (x + dx, y),
                (x, y + s*0.8),
                (x - dx, y)
            ], fill=(235, 80, 115, 140))
        elif p['type'] == 'sparkle':
            s = p['size'] * 2.2
            d.line([(x - s, y), (x + s, y)], fill=GOLD_LIGHT, width=2)
            d.line([(x, y - s), (x, y + s)], fill=GOLD_LIGHT, width=2)
            d.line([(x - s*0.5, y - s*0.5), (x + s*0.5, y + s*0.5)], fill=GOLD_LIGHT, width=1)
            d.line([(x - s*0.5, y + s*0.5), (x + s*0.5, y - s*0.5)], fill=GOLD_LIGHT, width=1)
        elif p['type'] == 'star':
            r = p['size'] * 1.5
            d.ellipse([x - r*2, y - r*2, x + r*2, y + r*2], fill=(255, 230, 140, 50))
            d.ellipse([x - r, y - r, x + r, y + r], fill=(255, 245, 200, 180))
        else: # gold_bokeh
            r = p['size'] * 2.5
            d.ellipse([x - r, y - r, x + r, y + r], fill=(218, 175, 60, 60))

# Ornate Golden Chandelier / Hanging Lanterns
def draw_royal_lanterns(im, frame_num):
    d = ImageDraw.Draw(im)
    lantern_positions = [
        (130, 110, 0.0),
        (WIDTH - 130, 110, 1.6),
        (220, 80, 0.8),
        (WIDTH - 220, 80, 2.4),
    ]
    for lx, chain_len, phase in lantern_positions:
        sway = math.sin((frame_num * 0.05) + phase) * 7
        bottom_x = lx + sway
        d.line([(lx, 48), (bottom_x, 48 + chain_len)], fill=GOLD_METALLIC, width=2)
        ly = 48 + chain_len
        d.polygon([(bottom_x - 18, ly), (bottom_x + 18, ly), (bottom_x + 14, ly + 8), (bottom_x - 14, ly + 8)], fill=GOLD_BRIGHT)
        d.rectangle([bottom_x - 16, ly + 8, bottom_x + 16, ly + 46], fill=(70, 5, 18, 220), outline=GOLD_BRIGHT, width=2)
        d.line([(bottom_x - 16, ly + 8), (bottom_x + 16, ly + 46)], fill=GOLD_METALLIC, width=1)
        d.line([(bottom_x + 16, ly + 8), (bottom_x - 16, ly + 46)], fill=GOLD_METALLIC, width=1)
        flicker = 1.0 + 0.3 * math.sin(frame_num * 0.2 + phase)
        glow_r = int(14 * flicker)
        d.ellipse([bottom_x - glow_r, ly + 27 - glow_r, bottom_x + glow_r, ly + 27 + glow_r], fill=(255, 235, 150, 90))
        d.ellipse([bottom_x - 4, ly + 27 - 4, bottom_x + 4, ly + 27 + 4], fill=WHITE)
        d.polygon([(bottom_x - 12, ly + 46), (bottom_x + 12, ly + 46), (bottom_x, ly + 62)], fill=GOLD_BRIGHT)
        d.line([(bottom_x, ly + 62), (bottom_x, ly + 72)], fill=GOLD_METALLIC, width=2)
        d.ellipse([bottom_x - 3, ly + 72, bottom_x + 3, ly + 78], fill=GOLD_BRIGHT)

# Helper: Golden Foil 3D Embossed Text
def draw_gold_text(d, pos, text, font, anchor="mm"):
    x, y = pos
    # Soft deep shadow
    d.text((x + 3, y + 4), text, fill=(20, 0, 5, 240), font=font, anchor=anchor)
    # Metallic gold bevel
    d.text((x + 1, y + 2), text, fill=GOLD_DARK, font=font, anchor=anchor)
    # Primary gold body
    d.text((x, y), text, fill=GOLD_BRIGHT, font=font, anchor=anchor)
    # Top highlight
    d.text((x - 1, y - 1), text, fill=GOLD_LIGHT, font=font, anchor=anchor)

# Helper: Jharokha Arch Picture Frame with Intricate Gold Border
def draw_jharokha_frame(im, src_img, box, zoom=1.0):
    x1, y1, x2, y2 = box
    bw = x2 - x1
    bh = y2 - y1
    
    sw = int(bw * zoom)
    sh = int(bh * zoom)
    scale = max(sw / src_img.width, sh / src_img.height)
    resized = src_img.resize((int(src_img.width * scale), int(src_img.height * scale)), Image.Resampling.LANCZOS)
    
    left = (resized.width - bw) // 2
    top = (resized.height - bh) // 2
    cropped = resized.crop((left, top, left + bw, top + bh))
    
    mask = Image.new("L", (bw, bh), 0)
    dm = ImageDraw.Draw(mask)
    arch_height = int(bw * 0.45)
    dm.ellipse([0, 0, bw, arch_height * 2], fill=255)
    dm.rectangle([0, arch_height, bw, bh], fill=255)
    
    cropped.putalpha(mask)
    im.paste(cropped, (x1, y1), cropped)
    
    d = ImageDraw.Draw(im)
    d.arc([x1, y1, x2, y1 + arch_height * 2], 180, 360, fill=GOLD_BRIGHT, width=7)
    d.line([(x1, y1 + arch_height), (x1, y2)], fill=GOLD_BRIGHT, width=7)
    d.line([(x2, y1 + arch_height), (x2, y2)], fill=GOLD_BRIGHT, width=7)
    d.line([(x1, y2), (x2, y2)], fill=GOLD_BRIGHT, width=7)
    
    off = 8
    d.arc([x1 + off, y1 + off, x2 - off, y1 + arch_height * 2 - off], 180, 360, fill=GOLD_LIGHT, width=2)
    d.line([(x1 + off, y1 + arch_height), (x1 + off, y2 - off)], fill=GOLD_LIGHT, width=2)
    d.line([(x2 - off, y1 + arch_height), (x2 - off, y2 - off)], fill=GOLD_LIGHT, width=2)
    d.line([(x1 + off, y2 - off), (x2 - off, y2 - off)], fill=GOLD_LIGHT, width=2)
    
    top_x, top_y = (x1 + x2)//2, y1
    d.polygon([(top_x, top_y - 28), (top_x + 18, top_y), (top_x, top_y + 12), (top_x - 18, top_y)], fill=GOLD_BRIGHT, outline=GOLD_DARK)

# Helper: Intense Diamond Ring Sparkle
def draw_intense_diamond_flare(im, cx, cy, frame_num):
    d = ImageDraw.Draw(im)
    pulse = 1.0 + 0.4 * math.sin(frame_num * 0.35)
    r = 28 * pulse
    
    d.ellipse([cx - r*3.0, cy - r*3.0, cx + r*3.0, cy + r*3.0], fill=(255, 230, 160, 50))
    d.ellipse([cx - r*1.8, cy - r*1.8, cx + r*1.8, cy + r*1.8], fill=(255, 250, 210, 120))
    d.ellipse([cx - r*0.7, cy - r*0.7, cx + r*0.7, cy + r*0.7], fill=(255, 255, 255, 220))
    
    beam_len = 65 * pulse
    for angle_deg in [0, 45, 90, 135]:
        rad = math.radians(angle_deg + (frame_num * 1.5))
        bx1 = cx - math.cos(rad) * beam_len
        by1 = cy - math.sin(rad) * beam_len
        bx2 = cx + math.cos(rad) * beam_len
        by2 = cy + math.sin(rad) * beam_len
        d.line([(bx1, by1), (bx2, by2)], fill=(255, 255, 240, 200), width=2)

print("Starting Complete Deluxe Video Rendering...")

ffmpeg_cmd = [
    "ffmpeg", "-y",
    "-f", "rawvideo",
    "-vcodec", "rawvideo",
    "-s", f"{WIDTH}x{HEIGHT}",
    "-pix_fmt", "rgb24",
    "-r", str(FPS),
    "-i", "-",
    "-i", AUDIO_FILE,
    "-c:v", "libx264",
    "-preset", "medium",
    "-crf", "18",
    "-pix_fmt", "yuv420p",
    "-c:a", "aac",
    "-b:a", "256k",
    "-t", "30.0",
    "-filter_complex", "[1:0]afade=t=in:st=0:d=1.5,afade=t=out:st=28.0:d=2.0[a]",
    "-map", "0:v:0",
    "-map", "[a]",
    OUTPUT_VIDEO
]

pipe = subprocess.Popen(ffmpeg_cmd, stdin=subprocess.PIPE)

sample_saved = {1: False, 2: False, 3: False, 4: False, 5: False, 6: False}

for f in range(TOTAL_FRAMES):
    sec = f / FPS
    frame = ROYAL_BG.copy()
    d = ImageDraw.Draw(frame)
    
    # Universal Royal Effects
    draw_royal_lanterns(frame, f)
    draw_lux_particles(frame, f)
    
    # -------------------------------------------------------------
    # SLIDE 1: 0 to 4s (GANESHA BLESSING)
    # -------------------------------------------------------------
    if 0 <= sec < 4.0:
        rot_angle = f * 0.8
        rotated_mandala = MANDALA_IMG.rotate(rot_angle, resample=Image.Resampling.BICUBIC)
        mx = (WIDTH - rotated_mandala.width) // 2
        my = 280
        frame.paste(rotated_mandala, (mx, my), rotated_mandala)
        
        gw, gh = 440, 440
        gx = (WIDTH - gw) // 2
        gy = 410
        ganesha_scaled = img_ganesha.resize((gw, gh), Image.Resampling.LANCZOS)
        frame.paste(ganesha_scaled, (gx, gy), ganesha_scaled)
        
        draw_gold_text(d, (WIDTH//2, 990), "|| Shree Ganeshaya Namah ||", FONT_CINZEL_LG, anchor="mm")
        
        # Sanskrit Shloka in clear English Transliteration (ZERO SQUARE BOXES!)
        d.text((WIDTH//2, 1075), '"Vakratunda Mahakaya Suryakoti Samaprabha"', fill=GOLD_LIGHT, font=FONT_SERIF_BOLD, anchor="mm")
        d.text((WIDTH//2, 1130), '"Nirvighnam Kuru Me Deva Sarvakaryeshu Sarvada"', fill=GOLD_LIGHT, font=FONT_SERIF_BOLD, anchor="mm")
        
        d.line([(WIDTH//2 - 200, 1195), (WIDTH//2 + 200, 1195)], fill=GOLD_METALLIC, width=3)
        d.polygon([(WIDTH//2, 1188), (WIDTH//2 + 14, 1195), (WIDTH//2, 1202), (WIDTH//2 - 14, 1195)], fill=GOLD_BRIGHT)
        
        draw_gold_text(d, (WIDTH//2, 1270), "With the Divine Blessings of Lord Ganesha", FONT_ALEX_MD, anchor="mm")
        draw_gold_text(d, (WIDTH//2, 1340), "An Auspicious Journey of Love Begins", FONT_VIBES_MD, anchor="mm")
        
        if not sample_saved[1] and f == 45:
            frame.convert("RGB").save(os.path.join(BRAIN_DIR, "preview_slide_1_ganesha.jpg"))
            sample_saved[1] = True

    # -------------------------------------------------------------
    # SLIDE 2: 4 to 8s (THE AUSPICIOUS INVITATION & MONOGRAM)
    # -------------------------------------------------------------
    elif 4.0 <= sec < 8.0:
        draw_gold_text(d, (WIDTH//2, 330), "WITH THE BLESSINGS OF ALMIGHTY", FONT_CINZEL_SM, anchor="mm")
        draw_gold_text(d, (WIDTH//2, 375), "& OUR BELOVED FAMILIES", FONT_CINZEL_SM, anchor="mm")
        
        d.line([(WIDTH//2 - 160, 420), (WIDTH//2 + 160, 420)], fill=GOLD_METALLIC, width=2)
        
        d.text((WIDTH//2, 480), "We cordially invite you to grace the", fill=IVORY_CREAM, font=FONT_SERIF_REG, anchor="mm")
        d.text((WIDTH//2, 525), "auspicious engagement celebrations of", fill=IVORY_CREAM, font=FONT_SERIF_REG, anchor="mm")
        
        mcx, mcy = WIDTH//2, 790
        d.ellipse([mcx - 180, mcy - 180, mcx + 180, mcy + 180], outline=GOLD_METALLIC, width=4)
        d.ellipse([mcx - 165, mcy - 165, mcx + 165, mcy + 165], outline=GOLD_BRIGHT, width=2)
        d.ellipse([mcx - 150, mcy - 150, mcx + 150, mcy + 150], fill=(70, 5, 18, 240), outline=GOLD_LIGHT, width=3)
        
        d.text((mcx - 50, mcy - 20), "M", fill=GOLD_LIGHT, font=FONT_CINZEL_XL, anchor="mm")
        d.text((mcx, mcy + 10), "&", fill=GOLD_BRIGHT, font=FONT_VIBES_LG, anchor="mm")
        d.text((mcx + 55, mcy - 20), "R", fill=GOLD_LIGHT, font=FONT_CINZEL_XL, anchor="mm")
        
        # Red vector hearts flanking FOREVER
        draw_vector_heart(d, mcx - 85, mcy + 105, 12, ROSE_RED, ROSE_PINK)
        d.text((mcx, mcy + 105), "FOREVER", fill=GOLD_LIGHT, font=FONT_SANS_BOLD, anchor="mm")
        draw_vector_heart(d, mcx + 85, mcy + 105, 12, ROSE_RED, ROSE_PINK)
        
        draw_gold_text(d, (WIDTH//2, 1100), "MANSI & RISAV", FONT_CINZEL_LG, anchor="mm")
        d.line([(WIDTH//2 - 220, 1160), (WIDTH//2 + 220, 1160)], fill=GOLD_METALLIC, width=3)
        d.polygon([(WIDTH//2, 1152), (WIDTH//2 + 12, 1160), (WIDTH//2, 1168), (WIDTH//2 - 12, 1160)], fill=GOLD_BRIGHT)
        
        draw_gold_text(d, (WIDTH//2, 1230), "ENGAGEMENT CEREMONY", FONT_CINZEL_MD, anchor="mm")
        draw_gold_text(d, (WIDTH//2, 1315), "Sunday, 6th December 2026", FONT_VIBES_MD, anchor="mm")
        d.text((WIDTH//2, 1375), "GIRAFFE RESORT - RAIGANJ", fill=GOLD_LIGHT, font=FONT_SANS_BOLD, anchor="mm")
        
        if not sample_saved[2] and f == 180:
            frame.convert("RGB").save(os.path.join(BRAIN_DIR, "preview_slide_2_monogram.jpg"))
            sample_saved[2] = True

    # -------------------------------------------------------------
    # SLIDE 3: 8 to 13s (THE COUPLE REVEAL - PROPOSAL)
    # -------------------------------------------------------------
    elif 8.0 <= sec < 13.0:
        draw_gold_text(d, (WIDTH//2, 260), "|| Shree Ganeshaya Namah ||", FONT_CINZEL_SM, anchor="mm")
        draw_gold_text(d, (WIDTH//2, 315), "THE PROMISE OF FOREVER", FONT_CINZEL_MD, anchor="mm")
        
        zoom_factor = 1.0 + 0.08 * ((sec - 8.0) / 5.0)
        arch_box = (110, 370, WIDTH - 110, 1330)
        draw_jharokha_frame(frame, img_proposal, arch_box, zoom=zoom_factor)
        
        ring_x = int(110 + (WIDTH - 220) * 0.54)
        ring_y = int(370 + (1330 - 370) * 0.44)
        draw_intense_diamond_flare(frame, ring_x, ring_y, f)
        
        # Floating RED VECTOR HEARTS rising from the ring! (NO EMOJI RECTANGLES!)
        for hi, phase in enumerate([0.0, 1.2, 2.4, 3.6]):
            hy = ring_y - int(((f * 2.8 + hi * 80) % 360))
            hx = ring_x + int(math.sin((f * 0.08) + phase) * 35)
            hs = 14 + int(4 * math.sin(f * 0.1 + phase))
            draw_vector_heart(d, hx, hy, hs, ROSE_RED, (255, 190, 210))
            
        draw_gold_text(d, (WIDTH//2, 1420), "Mansi & Risav", FONT_VIBES_HERO, anchor="mm")
        draw_gold_text(d, (WIDTH//2, 1515), "ENGAGEMENT CEREMONY", FONT_CINZEL_MD, anchor="mm")
        draw_gold_text(d, (WIDTH//2, 1580), '"Two hearts in love, together forever"', FONT_ALEX_MD, anchor="mm")
        
        if not sample_saved[3] and f == 315:
            frame.convert("RGB").save(os.path.join(BRAIN_DIR, "preview_slide_3_proposal.jpg"))
            sample_saved[3] = True

    # -------------------------------------------------------------
    # SLIDE 4: 13 to 18s (FAMILY INTRODUCTIONS - WITH BROTHER MANMEET RAJ)
    # -------------------------------------------------------------
    elif 13.0 <= sec < 18.0:
        draw_gold_text(d, (WIDTH//2, 240), "WITH THE BLESSINGS OF OUR FAMILIES", FONT_CINZEL_SM, anchor="mm")
        d.line([(WIDTH//2 - 180, 275), (WIDTH//2 + 180, 275)], fill=GOLD_METALLIC, width=2)
        
        portrait_box = (WIDTH//2 - 210, 310, WIDTH//2 + 210, 810)
        draw_jharokha_frame(frame, img_portrait, portrait_box, zoom=1.03)
        
        # Groom Card
        gy = 880
        d.rectangle([90, gy - 60, WIDTH - 90, gy + 130], fill=(55, 3, 12, 245), outline=GOLD_BRIGHT, width=3)
        d.rectangle([98, gy - 52, WIDTH - 98, gy + 122], outline=GOLD_METALLIC, width=1)
        draw_gold_text(d, (WIDTH//2, gy - 25), "THE GROOM", FONT_CINZEL_SM, anchor="mm")
        draw_gold_text(d, (WIDTH//2, gy + 18), "RISAV", FONT_CINZEL_LG, anchor="mm")
        d.text((WIDTH//2, gy + 65), "S/o. Mr. Binod Prasad Gupta", fill=IVORY_CREAM, font=FONT_SERIF_BOLD, anchor="mm")
        d.text((WIDTH//2, gy + 102), "& Mrs. Pushpa Gupta", fill=IVORY_CREAM, font=FONT_SERIF_BOLD, anchor="mm")
        
        # Vector Hearts & Golden Ring between Cards
        draw_vector_heart(d, WIDTH//2 - 95, 1055, 20, ROSE_RED, (255, 190, 210))
        draw_golden_ring(d, WIDTH//2, 1055, 22)
        draw_vector_heart(d, WIDTH//2 + 95, 1055, 20, ROSE_RED, (255, 190, 210))
        
        # Bride Card with Brother (PERFECTLY FITTED, ZERO OVERFLOW!)
        by = 1205
        d.rectangle([90, by - 60, WIDTH - 90, by + 175], fill=(55, 3, 12, 245), outline=GOLD_BRIGHT, width=3)
        d.rectangle([98, by - 52, WIDTH - 98, by + 167], outline=GOLD_METALLIC, width=1)
        draw_gold_text(d, (WIDTH//2, by - 25), "THE BRIDE", FONT_CINZEL_SM, anchor="mm")
        draw_gold_text(d, (WIDTH//2, by + 18), "MANSI", FONT_CINZEL_LG, anchor="mm")
        d.text((WIDTH//2, by + 65), "D/o. Mr. Sanjeev Kumar Suman", fill=IVORY_CREAM, font=FONT_SERIF_BOLD, anchor="mm")
        d.text((WIDTH//2, by + 102), "& Mrs. Manorama Devi", fill=IVORY_CREAM, font=FONT_SERIF_BOLD, anchor="mm")
        d.line([(WIDTH//2 - 140, by + 128), (WIDTH//2 + 140, by + 128)], fill=GOLD_METALLIC, width=1)
        d.text((WIDTH//2, by + 152), "Loving Brother: Mr. Manmeet Raj", fill=GOLD_LIGHT, font=FONT_SERIF_BOLD, anchor="mm")
        
        if not sample_saved[4] and f == 465:
            frame.convert("RGB").save(os.path.join(BRAIN_DIR, "preview_slide_4_families.jpg"))
            sample_saved[4] = True

    # -------------------------------------------------------------
    # SLIDE 5: 18 to 23s (EVENT DETAILS - DATE, TIME, VENUE)
    # -------------------------------------------------------------
    elif 18.0 <= sec < 23.0:
        draw_gold_text(d, (WIDTH//2, 240), "AUSPICIOUS CELEBRATIONS", FONT_CINZEL_SM, anchor="mm")
        draw_gold_text(d, (WIDTH//2, 305), "ENGAGEMENT CEREMONY", FONT_CINZEL_LG, anchor="mm")
        d.line([(WIDTH//2 - 200, 350), (WIDTH//2 + 200, 350)], fill=GOLD_METALLIC, width=2)
        
        # Card 1: DATE
        cy1 = 490
        d.rectangle([90, cy1 - 80, WIDTH - 90, cy1 + 80], fill=(55, 3, 12, 245), outline=GOLD_BRIGHT, width=3)
        d.rectangle([98, cy1 - 72, WIDTH - 98, cy1 + 72], outline=GOLD_METALLIC, width=1)
        draw_gold_text(d, (WIDTH//2, cy1 - 38), "-- DATE --", FONT_CINZEL_SM, anchor="mm")
        draw_gold_text(d, (WIDTH//2, cy1 + 22), "Sunday, 6th December, 2026", FONT_CINZEL_MD, anchor="mm")
        
        # Card 2: TIME
        cy2 = 715
        d.rectangle([90, cy2 - 75, WIDTH - 90, cy2 + 75], fill=(55, 3, 12, 245), outline=GOLD_BRIGHT, width=3)
        d.rectangle([98, cy2 - 67, WIDTH - 98, cy2 + 67], outline=GOLD_METALLIC, width=1)
        draw_gold_text(d, (WIDTH//2, cy2 - 32), "-- TIME --", FONT_CINZEL_SM, anchor="mm")
        draw_gold_text(d, (WIDTH//2, cy2 + 22), "6:00 PM Onwards", FONT_CINZEL_MD, anchor="mm")
        
        # Card 3: VENUE
        cy3 = 1060
        d.rectangle([90, cy3 - 195, WIDTH - 90, cy3 + 195], fill=(55, 3, 12, 245), outline=GOLD_BRIGHT, width=3)
        d.rectangle([98, cy3 - 187, WIDTH - 98, cy3 + 187], outline=GOLD_METALLIC, width=1)
        draw_gold_text(d, (WIDTH//2, cy3 - 145), "-- VENUE --", FONT_CINZEL_SM, anchor="mm")
        draw_gold_text(d, (WIDTH//2, cy3 - 80), "GIRAFFE RESORT", FONT_CINZEL_LG, anchor="mm")
        
        d.line([(WIDTH//2 - 160, cy3 - 35), (WIDTH//2 + 160, cy3 - 35)], fill=GOLD_METALLIC, width=2)
        
        d.text((WIDTH//2, cy3 + 15), "Khalsi - Khoksa Road, Mirual,", fill=IVORY_CREAM, font=FONT_SERIF_BOLD, anchor="mm")
        d.text((WIDTH//2, cy3 + 65), "Raiganj, Uttar Dinajpur,", fill=IVORY_CREAM, font=FONT_SERIF_BOLD, anchor="mm")
        d.text((WIDTH//2, cy3 + 115), "West Bengal - 733130", fill=IVORY_CREAM, font=FONT_SERIF_BOLD, anchor="mm")
        d.text((WIDTH//2, cy3 + 162), "* Interactive Google Maps Venue Location *", fill=GOLD_BRIGHT, font=FONT_SANS_BOLD, anchor="mm")
        
        draw_gold_text(d, (WIDTH//2, 1440), '"Your blessings are our greatest gift"', FONT_ALEX_MD, anchor="mm")
        
        if not sample_saved[5] and f == 610:
            frame.convert("RGB").save(os.path.join(BRAIN_DIR, "preview_slide_5_details.jpg"))
            sample_saved[5] = True

    # -------------------------------------------------------------
    # SLIDE 6: 23 to 30s (DEDICATED SLIDE: GUBLU'S SPECIAL INVITATION!)
    # -------------------------------------------------------------
    else:
        # Full Royal Jharokha Arch with Mansi, Risav and baby Gublu
        arch_box = (WIDTH//2 - 230, 240, WIDTH//2 + 230, 830)
        draw_jharokha_frame(frame, img_gublu, arch_box, zoom=1.02)
        
        draw_gold_text(d, (WIDTH//2, 885), "Mansi & Risav", FONT_VIBES_HERO, anchor="mm")
        d.line([(WIDTH//2 - 200, 950), (WIDTH//2 + 200, 950)], fill=GOLD_METALLIC, width=2)
        d.polygon([(WIDTH//2, 943), (WIDTH//2 + 12, 950), (WIDTH//2, 957), (WIDTH//2 - 12, 950)], fill=GOLD_BRIGHT)
        
        # Gublu's Heartfelt Invitation Card
        d.rectangle([90, 990, WIDTH - 90, 1180], fill=(55, 3, 12, 245), outline=GOLD_BRIGHT, width=3)
        d.rectangle([98, 998, WIDTH - 98, 1172], outline=GOLD_METALLIC, width=1)
        
        draw_gold_text(d, (WIDTH//2, 1038), '"Mere Massi ke Engagement me', FONT_CINZEL_SM, anchor="mm")
        draw_gold_text(d, (WIDTH//2, 1085), 'jarur se jarur aayean."', FONT_CINZEL_SM, anchor="mm")
        
        # Red vector hearts flanking Gublu's request
        draw_vector_heart(d, WIDTH//2 - 205, 1135, 14, ROSE_RED, (255, 190, 210))
        d.text((WIDTH//2, 1135), "-- Special Request by Gublu --", fill=GOLD_LIGHT, font=FONT_SERIF_BOLD, anchor="mm")
        draw_vector_heart(d, WIDTH//2 + 205, 1135, 14, ROSE_RED, (255, 190, 210))
        
        # Clean text with vector heart
        draw_gold_text(d, (WIDTH//2 - 20, 1240), "Reliving this moment forever", FONT_ALEX_LG, anchor="mm")
        draw_vector_heart(d, WIDTH//2 + 235, 1240, 18, ROSE_RED, (255, 190, 210))
        
        draw_gold_text(d, (WIDTH//2, 1330), "SUNDAY, 6TH DECEMBER 2026", FONT_CINZEL_SM, anchor="mm")
        d.text((WIDTH//2, 1375), "GIRAFFE RESORT - RAIGANJ", fill=GOLD_LIGHT, font=FONT_SANS_BOLD, anchor="mm")
        
        # Warm Blessings & Brother credit
        d.text((WIDTH//2, 1450), "With Warm Blessings from Gupta & Suman Families", fill=IVORY_CREAM, font=FONT_SERIF_REG, anchor="mm")
        d.text((WIDTH//2, 1505), "Crafted with love -- by Bride's Brother Mr. Manmeet Raj", fill=GOLD_BRIGHT, font=FONT_SERIF_BOLD, anchor="mm")
        
        # Smooth romantic fade out in the last 1.5 seconds
        if sec >= 28.5:
            fade_alpha = int(255 * (sec - 28.5) / 1.5)
            fade_overlay = Image.new("RGBA", (WIDTH, HEIGHT), (20, 1, 5, fade_alpha))
            frame = Image.alpha_composite(frame, fade_overlay)
            
        if not sample_saved[6] and f == 780:
            frame.convert("RGB").save(os.path.join(BRAIN_DIR, "preview_slide_6_gublu.jpg"))
            sample_saved[6] = True

    raw_bytes = frame.convert("RGB").tobytes()
    pipe.stdin.write(raw_bytes)
    
    if f % 90 == 0 or f == TOTAL_FRAMES - 1:
        print(f"Rendered Deluxe Frame {f+1}/{TOTAL_FRAMES} ({sec:.1f}s / 30.0s)")

pipe.stdin.close()
pipe.wait()
print(f"Video recreated successfully at: {OUTPUT_VIDEO}")
