# 💍 MANSI & RISAV — Premium Animated Engagement Invitation

A cinematic, interactive, and mobile-first Indian Engagement Invitation website and 30-second vertical video for **MANSI & RISAV**.

---

## ✨ Features & Highlights

- **🌸 Royal Indian Aesthetics**: Ivory and sage-green background with royal maroon & champagne-gold accents, hanging golden lanterns, Lord Ganesha blessing, and glowing particle effects.
- **✉️ Interactive Envelope Opening**: Full-screen royal invitation envelope with an ornate golden wax seal monogram ("M & R"). Tapping **OPEN INVITATION** triggers a 3D opening animation, golden confetti and rose petal shower, and begins background music playback.
- **💍 Proposing Couple Reveal**: Uses the exact supplied cartoon characters featuring Groom Risav (in formal black suit, curly hair & glasses) kneeling with a diamond engagement ring, and Bride Mansi (in traditional pink lehenga) jumping with joy, complete with animated ring sparkles and floating hearts!
- **📜 Romantic "Terms & Conditions Accepted" Story**: Includes the playful and heartwarming agreement signed by the couple with official checklist vows.
- **👨‍👩‍👧‍👦 Family Introductions**:
  - **GROOM**: RISAV (S/o. Mr. Binod Prasad Gupta & Mrs. Pushpa Gupta)
  - **BRIDE**: MANSI (D/o. Mr. Sanjeev Kumar Suman & Mrs. Manorama Devi)
- **⏳ Auspicious Schedule & Live Countdown**:
  - **Date**: Sunday, 6th December, 2026
  - **Time**: 6:00 PM Onwards
  - **Live Countdown Timer** ticking down to the exact auspicious Muhurat.
- **📍 Interactive Google Maps Venue Location**:
  - Prominent golden/maroon **VIEW VENUE LOCATION** button opening the official Google Maps link: [https://share.google/ltWlyblaDHHqS4iHx](https://share.google/ltWlyblaDHHqS4iHx)
  - Complete address: *Giraffe Resort, Khalsi - Khoksa Road, Mirual, Raiganj, Uttar Dinajpur, West Bengal – 733130*.
  - Embedded responsive Google Map.
- **🎬 30-Second 1080×1920 Vertical Invitation Video**:
  - Exact 9:16 vertical resolution (1080×1920) at 30 FPS.
  - Video Codec: H.264, Audio Codec: AAC.
  - 6 cinematic scenes synchronized to the supplied romantic song with smooth audio fade-in and fade-out.
  - **DOWNLOAD VIDEO** button to save the MP4 directly to camera roll/desktop.
- **📅 Add to Calendar (.ics Generator)**:
  - Generates and downloads a `.ics` calendar invitation for Apple Calendar, Google Calendar, Outlook, and Android.
- **📲 Multi-Platform Sharing**:
  - Native Web Share API + WhatsApp 1-tap share with custom prefilled message + copy-to-clipboard with instant toast confirmation.
- **🎵 Music Controls**:
  - Floating music badge with Play/Pause, Mute/Unmute, and rotation animation.

---

## 🚀 How to Run Locally

```bash
# 1. Navigate to the project directory
cd risav-aur-mansi-engagement-invitation-card

# 2. Run the development server
npm run dev

# 3. Open in your browser
http://localhost:3000
```

---

## 🌐 Free Hosting on Vercel (1-Click Deployment)

You can host this invitation card completely **FREE** on Vercel with a custom subdomain like:
`https://risav-aur-mansi-engagement-invitation-card.vercel.app`

### Option 1: Via Vercel CLI (Fastest)

```bash
# In the project directory:
npx vercel
```
- Select your account.
- When prompted for project name, enter: `risav-aur-mansi-engagement-invitation-card`
- Your invitation will be live instantly!

### Option 2: Via GitHub + Vercel Dashboard

1. Push this folder to a GitHub repository named `risav-aur-mansi-engagement-invitation-card`.
2. Go to [vercel.com](https://vercel.com) and click **"Add New Project"**.
3. Import the repository.
4. In the Project Name field, type: `risav-aur-mansi-engagement-invitation-card`.
5. Click **"Deploy"**.
6. Your card is live at:
   `https://risav-aur-mansi-engagement-invitation-card.vercel.app`

---

## 📁 Project Structure

```
risav-aur-mansi-engagement-invitation-card/
├── public/
│   ├── audio/
│   │   └── mansi-risav-engagement-song.mp3   # Supplied background song
│   ├── images/
│   │   ├── couple-proposal.jpg               # Proposing cartoon couple
│   │   ├── couple-portrait.jpg               # Couple romantic portrait
│   │   ├── couple-terms.jpg                  # Terms & Conditions accepted
│   │   └── ganesha-gold.png                  # Lord Ganesha golden emblem
│   └── video/
│       └── mansi-risav-engagement.mp4        # 30-second 1080x1920 MP4 film
├── scripts/
│   └── make_video.py                         # FFmpeg & Python video engine
├── src/
│   ├── app/
│   │   ├── globals.css                       # Luxury styling & animations
│   │   ├── layout.tsx                        # Metadata & fonts
│   │   └── page.tsx                          # Interactive invitation page
│   ├── components/
│   │   ├── InvitationEnvelope.tsx            # 3D Wax seal envelope
│   │   ├── GaneshBlessing.tsx                # Religious blessing & shloka
│   │   ├── CoupleReveal.tsx                  # Proposing couple & sparkles
│   │   ├── FamilyIntroduction.tsx            # Groom & Bride parents
│   │   ├── TermsAndConditionsStory.tsx       # Romantic vows & checklist
│   │   ├── EventDetails.tsx                  # Date, time & live countdown
│   │   ├── VenueLocation.tsx                 # Google maps & address
│   │   ├── VideoPlayerSection.tsx            # Video player & download
│   │   ├── ShareInvitation.tsx               # Web share & WhatsApp
│   │   └── MusicPlayer.tsx                   # Background audio controller
│   └── utils/
│       └── calendar.ts                       # .ics calendar event generator
├── package.json
├── tailwind.config.js
├── tsconfig.json
└── vercel.json                               # Vercel deployment & media config
```
