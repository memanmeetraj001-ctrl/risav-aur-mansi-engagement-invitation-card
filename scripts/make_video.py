import os
import sys
import math
import random
import subprocess
from PIL import Image, ImageDraw, ImageFont, ImageFilter

WIDTH, HEIGHT = 1080, 1920
FPS = 30
TOTAL_SECONDS = 30
TOTAL_FRAMES = FPS * TOTAL_SECONDS

BASE_DIR = r"C:\Users\meman\.gemini\antigravity\scratch\risav-aur-mansi-engagement-invitation-card"
PUBLIC_DIR = os.path.join(BASE_DIR, "public")
AUDIO_PATH = os.path.join(PUBLIC_DIR, "audio", "mansi-risav-engagement-song.mp3")
OUTPUT_VIDEO = os.path.join(PUBLIC_DIR, "video", "mansi-risav-engagement.mp4")

# Load fonts
FONT_SCRIPT_LG = ImageFont.truetype(r"C:\Windows\Fonts\segoescb.ttf", 64)
FONT_SCRIPT_MD = ImageFont.truetype(r"C:\Windows\Fonts\segoescb.ttf", 46)
FONT_SERIF_TITLE = ImageFont.truetype(r"C:\Windows\Fonts\georgiab.ttf", 52)
FONT_SERIF_SUB = ImageFont.truetype(r"C:\Windows\Fonts\georgiab.ttf", 36)
FONT_SERIF_BODY = ImageFont.truetype(r"C:\Windows\Fonts\georgia.ttf", 30)
FONT_SERIF_SM = ImageFont.truetype(r"C:\Windows\Fonts\georgia.ttf", 24)
FONT_MONOGRAM = ImageFont.truetype(r"C:\Windows\Fonts\georgiab.ttf", 90)
FONT_HINDI = ImageFont.truetype(r"C:\Windows\Fonts\timesbd.ttf", 42)

# Colors
MAROON = (91, 6, 22)
ROYAL_MAROON = (128, 19, 35)
GOLD = (212, 175, 55)
BRIGHT_GOLD = (245, 215, 105)
DEEP_GOLD = (165, 125, 30)
IVORY = (252, 250, 245)
IVORY_DARK = (245, 238, 225)
SAGE = (138, 154, 134)
WHITE = (255, 255, 255)
PINK_HEART = (255, 105, 140)

# Load Images
img_proposal = Image.open(os.path.join(PUBLIC_DIR, "images", "couple-proposal.jpg")).convert("RGBA")
img_portrait = Image.open(os.path.join(PUBLIC_DIR, "images", "couple-portrait.jpg")).convert("RGBA")
img_terms = Image.open(os.path.join(PUBLIC_DIR, "images", "couple-terms.jpg")).convert("RGBA")
img_ganesha = Image.open(os.path.join(PUBLIC_DIR, "images", "ganesha-gold.png")).convert("RGBA")

# Pre-render decorative elements
def get_base_background():
    bg = Image.new("RGBA", (WIDTH, HEIGHT), IVORY)
    d = ImageDraw.Draw(bg)
    
    # Subtle radial glow at center
    glow = Image.new("RGBA", (WIDTH, HEIGHT), (0,0,0,0))
    dg = ImageDraw.Draw(glow)
    dg.ellipse([WIDTH//2 - 600, HEIGHT//2 - 600, WIDTH//2 + 600, HEIGHT//2 + 600], fill=(255, 245, 215, 70))
    glow = glow.filter(ImageFilter.GaussianBlur(120))
    bg = Image.alpha_composite(bg, glow)
    d = ImageDraw.Draw(bg)

    # Royal Golden Double Border
    margin = 45
    d.rectangle([margin, margin, WIDTH - margin, HEIGHT - margin], outline=GOLD, width=4)
    d.rectangle([margin + 12, margin + 12, WIDTH - margin - 12, HEIGHT - margin - 12], outline=DEEP_GOLD, width=2)
    
    # Corner ornaments
    for cx in [margin, WIDTH - margin]:
        for cy in [margin, HEIGHT - margin]:
            d.ellipse([cx-10, cy-10, cx+10, cy+10], fill=BRIGHT_GOLD, outline=MAROON, width=2)
            d.rectangle([cx-4, cy-4, cx+4, cy+4], fill=MAROON)

    # Top & bottom central gold decorative divider
    d.line([(WIDTH//2 - 120, margin + 28), (WIDTH//2 + 120, margin + 28)], fill=GOLD, width=2)
    d.polygon([(WIDTH//2, margin + 24), (WIDTH//2 + 8, margin + 28), (WIDTH//2, margin + 32), (WIDTH//2 - 8, margin + 28)], fill=BRIGHT_GOLD)
    
    d.line([(WIDTH//2 - 120, HEIGHT - margin - 28), (WIDTH//2 + 120, HEIGHT - margin - 28)], fill=GOLD, width=2)
    d.polygon([(WIDTH//2, HEIGHT - margin - 32), (WIDTH//2 + 8, HEIGHT - margin - 28), (WIDTH//2, HEIGHT - margin - 24), (WIDTH//2 - 8, HEIGHT - margin - 28)], fill=BRIGHT_GOLD)

    return bg

BASE_BG = get_base_background()

# Pre-render Hanging Lanterns
def draw_lanterns(im, frame_num):
    d = ImageDraw.Draw(im)
    positions = [
        (120, 260, 0.9),
        (240, 210, 0.7),
        (WIDTH - 240, 210, 0.7),
        (WIDTH - 120, 260, 0.9)
    ]
    for lx, ly, scale in positions:
        swing = math.sin((frame_num * 0.05) + lx) * 3
        # Chain
        d.line([(lx, 45), (lx + swing, ly - 50)], fill=DEEP_GOLD, width=2)
        # Lantern body
        cx, cy = lx + swing, ly
        w, h = int(32 * scale), int(45 * scale)
        d.polygon([(cx, cy - h), (cx + w, cy - h//3), (cx + w*0.8, cy + h), (cx - w*0.8, cy + h), (cx - w, cy - h//3)],
                  fill=(255, 230, 140, 220), outline=DEEP_GOLD)
        # Lantern cap
        d.polygon([(cx - w*1.2, cy - h), (cx + w*1.2, cy - h), (cx, cy - h - 15*scale)], fill=DEEP_GOLD)
        # Light glow pulsing
        glow_alpha = int(90 + 35 * math.sin(frame_num * 0.1 + lx))
        d.ellipse([cx - w*1.6, cy - h*0.8, cx + w*1.6, cy + h*1.2], fill=(255, 220, 100, glow_alpha))
        # Tassel
        d.line([(cx, cy + h), (cx, cy + h + 25*scale)], fill=BRIGHT_GOLD, width=2)

# Floating hearts & dust
random.seed(42)
PARTICLES = [
    {
        'x': random.randint(80, WIDTH - 80),
        'base_y': random.randint(100, HEIGHT),
        'speed': random.uniform(1.2, 3.2),
        'size': random.randint(3, 8),
        'type': random.choice(['heart', 'sparkle', 'dot', 'dot'])
    }
    for _ in range(35)
]

def draw_particles(im, frame_num):
    d = ImageDraw.Draw(im)
    for p in PARTICLES:
        y = (p['base_y'] - frame_num * p['speed']) % (HEIGHT - 120) + 60
        x = p['x'] + math.sin((frame_num * 0.03) + p['base_y']) * 15
        if p['type'] == 'heart':
            s = p['size'] * 1.5
            # Draw cute small heart
            d.polygon([
                (x, y + s),
                (x - s, y - s*0.2),
                (x - s*0.6, y - s),
                (x, y - s*0.4),
                (x + s*0.6, y - s),
                (x + s, y - s*0.2)
            ], fill=(255, 120, 150, 140))
        elif p['type'] == 'sparkle':
            s = p['size'] * 1.8
            d.line([(x - s, y), (x + s, y)], fill=BRIGHT_GOLD, width=2)
            d.line([(x, y - s), (x, y + s)], fill=BRIGHT_GOLD, width=2)
            d.line([(x - s*0.5, y - s*0.5), (x + s*0.5, y + s*0.5)], fill=BRIGHT_GOLD, width=1)
            d.line([(x - s*0.5, y + s*0.5), (x + s*0.5, y - s*0.5)], fill=BRIGHT_GOLD, width=1)
        else:
            r = p['size'] * 0.8
            d.ellipse([x - r, y - r, x + r, y + r], fill=(245, 215, 110, 160))

def draw_arched_image(im, src_img, target_box, border_gold=True):
    # target_box = (x1, y1, x2, y2)
    bw = target_box[2] - target_box[0]
    bh = target_box[3] - target_box[1]
    
    # Resize & crop src_img to fit
    scaled = src_img.copy()
    scaled.thumbnail((bw, bh * 2), Image.Resampling.LANCZOS)
    if scaled.width < bw or scaled.height < bh:
        # Scale with aspect ratio cover
        scale = max(bw / scaled.width, bh / scaled.height)
        scaled = scaled.resize((int(scaled.width * scale), int(scaled.height * scale)), Image.Resampling.LANCZOS)
    
    # Center crop
    left = (scaled.width - bw) // 2
    top = (scaled.height - bh) // 2
    cropped = scaled.crop((left, top, left + bw, top + bh))
    
    # Arch mask
    mask = Image.new("L", (bw, bh), 0)
    dm = ImageDraw.Draw(mask)
    # Top arch: half-circle radius bw//2
    dm.pieslice([0, 0, bw, bw], 180, 360, fill=255)
    dm.rectangle([0, bw//2, bw, bh], fill=255)
    
    cropped.putalpha(mask)
    im.paste(cropped, (target_box[0], target_box[1]), cropped)
    
    if border_gold:
        d = ImageDraw.Draw(im)
        # Draw arched gold border
        d.arc([target_box[0], target_box[1], target_box[2], target_box[1] + bw], 180, 360, fill=GOLD, width=6)
        d.line([(target_box[0], target_box[1] + bw//2), (target_box[0], target_box[3])], fill=GOLD, width=6)
        d.line([(target_box[2], target_box[1] + bw//2), (target_box[2], target_box[3])], fill=GOLD, width=6)
        d.line([(target_box[0], target_box[3]), (target_box[2], target_box[3])], fill=GOLD, width=6)
        
        # Inner fine line
        offset = 6
        d.arc([target_box[0] + offset, target_box[1] + offset, target_box[2] - offset, target_box[1] + bw - offset], 180, 360, fill=BRIGHT_GOLD, width=2)
        d.line([(target_box[0] + offset, target_box[1] + bw//2), (target_box[0] + offset, target_box[3] - offset)], fill=BRIGHT_GOLD, width=2)
        d.line([(target_box[2] - offset, target_box[1] + bw//2), (target_box[2] - offset, target_box[3] - offset)], fill=BRIGHT_GOLD, width=2)
        d.line([(target_box[0] + offset, target_box[3] - offset), (target_box[2] - offset, target_box[3] - offset)], fill=BRIGHT_GOLD, width=2)

def draw_ring_sparkle(im, cx, cy, frame_num):
    d = ImageDraw.Draw(im)
    pulse = 1.0 + 0.35 * math.sin(frame_num * 0.3)
    r = 22 * pulse
    # Halo
    d.ellipse([cx - r*2.2, cy - r*2.2, cx + r*2.2, cy + r*2.2], fill=(255, 240, 180, 90))
    d.ellipse([cx - r*1.2, cy - r*1.2, cx + r*1.2, cy + r*1.2], fill=(255, 255, 220, 150))
    d.ellipse([cx - r*0.4, cy - r*0.4, cx + r*0.4, cy + r*0.4], fill=WHITE)
    # Diamond star rays
    ray_len = 40 * pulse
    angle = frame_num * 0.05
    for a in [angle, angle + math.pi/2, angle + math.pi/4, angle + 3*math.pi/4]:
        dx1, dy1 = math.cos(a) * ray_len, math.sin(a) * ray_len
        w = 3 if a in [angle, angle + math.pi/2] else 1.5
        d.line([(cx - dx1, cy - dy1), (cx + dx1, cy + dy1)], fill=WHITE, width=int(w))

print("Assets and helpers initialized. Starting video rendering...")

# FFmpeg Command
ffmpeg_cmd = [
    "ffmpeg",
    "-y",
    "-f", "rawvideo",
    "-vcodec", "rawvideo",
    "-s", f"{WIDTH}x{HEIGHT}",
    "-pix_fmt", "rgb24",
    "-r", str(FPS),
    "-i", "-",  # Video from stdin
    "-ss", "0",
    "-t", "30",
    "-i", AUDIO_PATH,  # Audio from file
    "-filter_complex", "[1:a]afade=t=in:ss=0:d=1.5,afade=t=out:st=28:d=2.0[aout]",
    "-map", "0:v",
    "-map", "[aout]",
    "-c:v", "libx264",
    "-preset", "medium",
    "-crf", "20",
    "-pix_fmt", "yuv420p",
    "-c:a", "aac",
    "-b:a", "192k",
    "-shortest",
    OUTPUT_VIDEO
]

pipe = subprocess.Popen(ffmpeg_cmd, stdin=subprocess.PIPE)

for f in range(TOTAL_FRAMES):
    sec = f / FPS
    frame = BASE_BG.copy()
    d = ImageDraw.Draw(frame)
    
    # Universal background effects: Lanterns & Floating particles
    draw_lanterns(frame, f)
    draw_particles(frame, f)
    
    # -------------------------------------------------------------
    # SCENE 1: 0 to 4s (Frames 0 to 120) - GANESHA BLESSING
    # -------------------------------------------------------------
    if 0 <= sec < 4.0:
        t = sec / 4.0
        # Ganesha image at top/center with glowing aura
        gw, gh = 420, 420
        gx = (WIDTH - gw) // 2
        gy = 480
        ganesha_scaled = img_ganesha.resize((gw, gh), Image.Resampling.LANCZOS)
        frame.paste(ganesha_scaled, (gx, gy), ganesha_scaled)
        
        # Religious blessing text
        d.text((WIDTH//2, 1020), "|| Shree Ganeshaya Namah ||", fill=MAROON, font=FONT_SERIF_TITLE, anchor="mm")
        
        # Auspicious quote
        d.text((WIDTH//2, 1130), "Vakratunda Mahakaya Suryakoti Samaprabha", fill=ROYAL_MAROON, font=FONT_SERIF_SUB, anchor="mm")
        d.text((WIDTH//2, 1180), "Nirvighnam Kuru Me Deva Sarvakaryeshu Sarvada", fill=ROYAL_MAROON, font=FONT_SERIF_SUB, anchor="mm")
        
        # Subtle glowing separator
        d.line([(WIDTH//2 - 180, 1260), (WIDTH//2 + 180, 1260)], fill=GOLD, width=3)
        d.polygon([(WIDTH//2, 1254), (WIDTH//2 + 12, 1260), (WIDTH//2, 1266), (WIDTH//2 - 12, 1260)], fill=BRIGHT_GOLD)
        
        d.text((WIDTH//2, 1340), "With the Divine Blessings of Lord Ganesha", fill=DEEP_GOLD, font=FONT_SERIF_BODY, anchor="mm")
        d.text((WIDTH//2, 1390), "A Journey of Eternal Love Begins", fill=MAROON, font=FONT_SCRIPT_MD, anchor="mm")

    # -------------------------------------------------------------
    # SCENE 2: 4 to 8s (Frames 120 to 240) - THE INVITATION
    # -------------------------------------------------------------
    elif 4.0 <= sec < 8.0:
        # Opening blessing text
        d.text((WIDTH//2, 360), "WITH THE BLESSINGS OF ALMIGHTY", fill=DEEP_GOLD, font=FONT_SERIF_BODY, anchor="mm")
        d.text((WIDTH//2, 410), "& OUR BELOVED FAMILY", fill=DEEP_GOLD, font=FONT_SERIF_BODY, anchor="mm")
        
        d.line([(WIDTH//2 - 140, 460), (WIDTH//2 + 140, 460)], fill=GOLD, width=2)
        
        d.text((WIDTH//2, 530), "We cordially invite you to celebrate the", fill=MAROON, font=FONT_SERIF_SUB, anchor="mm")
        d.text((WIDTH//2, 580), "auspicious engagement celebrations of", fill=MAROON, font=FONT_SERIF_SUB, anchor="mm")
        
        # Royal Monogram Seal M & R
        mcx, mcy = WIDTH//2, 850
        # Outer radiant circle
        d.ellipse([mcx - 170, mcy - 170, mcx + 170, mcy + 170], outline=GOLD, width=4)
        d.ellipse([mcx - 155, mcy - 155, mcx + 155, mcy + 155], outline=DEEP_GOLD, width=2)
        d.ellipse([mcx - 145, mcy - 145, mcx + 145, mcy + 145], fill=(255, 248, 230, 200), outline=BRIGHT_GOLD, width=3)
        
        # Monogram letters
        d.text((mcx - 45, mcy - 10), "M", fill=MAROON, font=FONT_MONOGRAM, anchor="mm")
        d.text((mcx, mcy + 20), "&", fill=GOLD, font=FONT_SCRIPT_LG, anchor="mm")
        d.text((mcx + 48, mcy - 10), "R", fill=MAROON, font=FONT_MONOGRAM, anchor="mm")
        
        # Little heart below seal
        d.text((mcx, mcy + 120), "❤️", fill=PINK_HEART, font=FONT_SERIF_SUB, anchor="mm")
        
        # Invitation declaration
        d.text((WIDTH//2, 1160), "MANSI & RISAV", fill=MAROON, font=FONT_SERIF_TITLE, anchor="mm")
        d.line([(WIDTH//2 - 200, 1220), (WIDTH//2 + 200, 1220)], fill=GOLD, width=3)
        d.polygon([(WIDTH//2, 1214), (WIDTH//2 + 10, 1220), (WIDTH//2, 1226), (WIDTH//2 - 10, 1220)], fill=BRIGHT_GOLD)
        
        d.text((WIDTH//2, 1290), "ENGAGEMENT CEREMONY", fill=ROYAL_MAROON, font=FONT_SERIF_SUB, anchor="mm")
        d.text((WIDTH//2, 1370), "Sunday, 6th December 2026", fill=DEEP_GOLD, font=FONT_SERIF_BODY, anchor="mm")
        d.text((WIDTH//2, 1420), "Raiganj, West Bengal", fill=MAROON, font=FONT_SERIF_SM, anchor="mm")

    # -------------------------------------------------------------
    # SCENE 3: 8 to 13s (Frames 240 to 390) - THE COUPLE REVEAL
    # -------------------------------------------------------------
    elif 8.0 <= sec < 13.0:
        d.text((WIDTH//2, 280), "|| Shree Ganeshaya Namah ||", fill=DEEP_GOLD, font=FONT_SERIF_SM, anchor="mm")
        d.text((WIDTH//2, 340), "THE PROMISE OF FOREVER", fill=ROYAL_MAROON, font=FONT_SERIF_SUB, anchor="mm")
        
        # Couple Proposing Cartoon Picture in Arch Frame
        arch_box = (140, 400, WIDTH - 140, 1320)
        draw_arched_image(frame, img_proposal, arch_box, border_gold=True)
        
        # Diamond Ring Sparkle animation!
        # The ring in couple-proposal.jpg is held by groom around 54% width, 49% height of original
        sparkle_x = int(140 + (WIDTH - 280) * 0.54)
        sparkle_y = int(400 + (1320 - 400) * 0.44)
        draw_ring_sparkle(frame, sparkle_x, sparkle_y, f)
        
        # Couple name banner below
        d.text((WIDTH//2, 1410), "MANSI  ❤️  RISAV", fill=MAROON, font=FONT_SERIF_TITLE, anchor="mm")
        
        d.line([(WIDTH//2 - 180, 1460), (WIDTH//2 + 180, 1460)], fill=GOLD, width=3)
        d.polygon([(WIDTH//2, 1454), (WIDTH//2 + 10, 1460), (WIDTH//2, 1466), (WIDTH//2 - 10, 1460)], fill=BRIGHT_GOLD)
        
        d.text((WIDTH//2, 1520), "ENGAGEMENT CEREMONY", fill=ROYAL_MAROON, font=FONT_SERIF_SUB, anchor="mm")
        d.text((WIDTH//2, 1590), "\"Two hearts in love, together forever\"", fill=DEEP_GOLD, font=FONT_SCRIPT_MD, anchor="mm")

    # -------------------------------------------------------------
    # SCENE 4: 13 to 18s (Frames 390 to 540) - FAMILY INTRODUCTION
    # -------------------------------------------------------------
    elif 13.0 <= sec < 18.0:
        d.text((WIDTH//2, 260), "WITH THE BLESSINGS OF OUR FAMILIES", fill=DEEP_GOLD, font=FONT_SERIF_BODY, anchor="mm")
        d.line([(WIDTH//2 - 160, 300), (WIDTH//2 + 160, 300)], fill=GOLD, width=2)
        
        # Portrait of couple in circular/oval frame
        arch_box = (WIDTH//2 - 220, 340, WIDTH//2 + 220, 840)
        draw_arched_image(frame, img_portrait, arch_box, border_gold=True)
        
        # Groom & Family Card
        gy = 960
        d.rectangle([140, gy - 60, WIDTH - 140, gy + 130], fill=(255, 248, 235, 220), outline=GOLD, width=2)
        d.text((WIDTH//2, gy - 25), "GROOM", fill=DEEP_GOLD, font=FONT_SERIF_SM, anchor="mm")
        d.text((WIDTH//2, gy + 20), "RISAV", fill=MAROON, font=FONT_SERIF_TITLE, anchor="mm")
        d.text((WIDTH//2, gy + 75), "S/o. Mr. Binod Prasad Gupta & Mrs. Pushpa Gupta", fill=ROYAL_MAROON, font=FONT_SERIF_BODY, anchor="mm")
        
        # Decorative Ring / Heart between cards
        d.text((WIDTH//2, gy + 175), "❤️  &  💍", fill=PINK_HEART, font=FONT_SERIF_SUB, anchor="mm")
        
        # Bride & Family Card
        by = gy + 270
        d.rectangle([140, by - 60, WIDTH - 140, by + 130], fill=(255, 248, 235, 220), outline=GOLD, width=2)
        d.text((WIDTH//2, by - 25), "BRIDE", fill=DEEP_GOLD, font=FONT_SERIF_SM, anchor="mm")
        d.text((WIDTH//2, by + 20), "MANSI", fill=MAROON, font=FONT_SERIF_TITLE, anchor="mm")
        d.text((WIDTH//2, by + 75), "D/o. Mr. Sanjeev Kumar Suman & Mrs. Manorama Devi", fill=ROYAL_MAROON, font=FONT_SERIF_BODY, anchor="mm")

    # -------------------------------------------------------------
    # SCENE 5: 18 to 25s (Frames 540 to 750) - EVENT DETAILS
    # -------------------------------------------------------------
    elif 18.0 <= sec < 25.0:
        d.text((WIDTH//2, 260), "JOIN US TO CELEBRATE", fill=DEEP_GOLD, font=FONT_SERIF_BODY, anchor="mm")
        d.text((WIDTH//2, 320), "ENGAGEMENT CEREMONY", fill=MAROON, font=FONT_SERIF_TITLE, anchor="mm")
        d.line([(WIDTH//2 - 200, 365), (WIDTH//2 + 200, 365)], fill=GOLD, width=2)
        
        # Card 1: DATE
        cy1 = 490
        d.rectangle([150, cy1 - 80, WIDTH - 150, cy1 + 80], fill=(255, 250, 240, 240), outline=GOLD, width=3)
        d.text((WIDTH//2, cy1 - 40), "📅  DATE", fill=DEEP_GOLD, font=FONT_SERIF_SUB, anchor="mm")
        d.text((WIDTH//2, cy1 + 25), "Sunday, 6th December, 2026", fill=MAROON, font=FONT_SERIF_TITLE, anchor="mm")
        
        # Card 2: TIME
        cy2 = 700
        d.rectangle([150, cy2 - 70, WIDTH - 150, cy2 + 70], fill=(255, 250, 240, 240), outline=GOLD, width=3)
        d.text((WIDTH//2, cy2 - 30), "⏰  TIME", fill=DEEP_GOLD, font=FONT_SERIF_SUB, anchor="mm")
        d.text((WIDTH//2, cy2 + 25), "6:00 PM Onwards", fill=MAROON, font=FONT_SERIF_TITLE, anchor="mm")
        
        # Card 3: VENUE
        cy3 = 1040
        d.rectangle([140, cy3 - 190, WIDTH - 140, cy3 + 190], fill=(255, 250, 240, 240), outline=GOLD, width=3)
        d.text((WIDTH//2, cy3 - 140), "📍  VENUE", fill=DEEP_GOLD, font=FONT_SERIF_SUB, anchor="mm")
        d.text((WIDTH//2, cy3 - 80), "GIRAFFE RESORT", fill=MAROON, font=FONT_SERIF_TITLE, anchor="mm")
        
        d.line([(WIDTH//2 - 140, cy3 - 35), (WIDTH//2 + 140, cy3 - 35)], fill=GOLD, width=2)
        
        d.text((WIDTH//2, cy3 + 15), "Khalsi - Khoksa Road, Mirual,", fill=ROYAL_MAROON, font=FONT_SERIF_BODY, anchor="mm")
        d.text((WIDTH//2, cy3 + 60), "Raiganj, Uttar Dinajpur,", fill=ROYAL_MAROON, font=FONT_SERIF_BODY, anchor="mm")
        d.text((WIDTH//2, cy3 + 105), "West Bengal – 733130", fill=ROYAL_MAROON, font=FONT_SERIF_BODY, anchor="mm")
        d.text((WIDTH//2, cy3 + 150), "★ Google Maps Venue Navigation Available ★", fill=DEEP_GOLD, font=FONT_SERIF_SM, anchor="mm")
        
        # Cute bottom reminder
        d.text((WIDTH//2, 1420), "\"Your blessings are our greatest gift\"", fill=MAROON, font=FONT_SCRIPT_MD, anchor="mm")

    # -------------------------------------------------------------
    # SCENE 6: 25 to 30s (Frames 750 to 900) - FINAL INVITATION
    # -------------------------------------------------------------
    else:
        # Terms & proposal couple highlight
        arch_box = (WIDTH//2 - 200, 280, WIDTH//2 + 200, 780)
        draw_arched_image(frame, img_terms, arch_box, border_gold=True)
        
        d.text((WIDTH//2, 860), "MANSI & RISAV", fill=MAROON, font=FONT_SERIF_TITLE, anchor="mm")
        d.line([(WIDTH//2 - 180, 910), (WIDTH//2 + 180, 910)], fill=GOLD, width=2)
        d.polygon([(WIDTH//2, 904), (WIDTH//2 + 10, 910), (WIDTH//2, 916), (WIDTH//2 - 10, 910)], fill=BRIGHT_GOLD)
        
        d.text((WIDTH//2, 980), "Your presence will make our", fill=ROYAL_MAROON, font=FONT_SERIF_SUB, anchor="mm")
        d.text((WIDTH//2, 1030), "special day even more memorable.", fill=ROYAL_MAROON, font=FONT_SERIF_SUB, anchor="mm")
        
        # Special Hindi warm invitation message requested by user
        d.rectangle([130, 1100, WIDTH - 130, 1220], fill=(255, 245, 230, 220), outline=GOLD, width=2)
        d.text((WIDTH//2, 1160), "\"Mansi and Risav ke Engagement me", fill=MAROON, font=FONT_SERIF_SUB, anchor="mm")
        d.text((WIDTH//2, 1205), "jarur se jarur aayean.\"", fill=MAROON, font=FONT_SERIF_SUB, anchor="mm")
        
        d.text((WIDTH//2, 1310), "Reliving this moment forever ❤️", fill=DEEP_GOLD, font=FONT_SCRIPT_MD, anchor="mm")
        
        d.text((WIDTH//2, 1420), "SUNDAY, 6TH DECEMBER 2026", fill=MAROON, font=FONT_SERIF_BODY, anchor="mm")
        d.text((WIDTH//2, 1465), "GIRAFFE RESORT • RAIGANJ", fill=ROYAL_MAROON, font=FONT_SERIF_SM, anchor="mm")
        
        # Final fade out at the very end
        if sec >= 28.5:
            fade_alpha = int(255 * (sec - 28.5) / 1.5)
            fade_overlay = Image.new("RGBA", (WIDTH, HEIGHT), (252, 250, 245, fade_alpha))
            frame = Image.alpha_composite(frame, fade_overlay)

    # Convert to RGB24 bytes and write directly to FFmpeg pipe
    raw_bytes = frame.convert("RGB").tobytes()
    pipe.stdin.write(raw_bytes)
    
    if f % 90 == 0 or f == TOTAL_FRAMES - 1:
        print(f"Rendered frame {f+1}/{TOTAL_FRAMES} ({sec:.1f}s / 30.0s)")

pipe.stdin.close()
pipe.wait()
print(f"Video created successfully at: {OUTPUT_VIDEO}")
