'use client';

import React, { useState } from 'react';
import { Share2, Check, Copy, MessageCircle } from 'lucide-react';

export default function ShareInvitation() {
  const [copied, setCopied] = useState(false);

  const shareData = {
    title: 'Mansi ❤️ Risav — Engagement Invitation',
    text: 'You are cordially invited to the Engagement Ceremony of Mansi & Risav on Sunday, 6th December 2026 at Giraffe Resort, Raiganj. Watch the animated invitation card here:',
    url: typeof window !== 'undefined' ? window.location.href : 'https://risav-aur-mansi-engagement-invitation-card.vercel.app',
  };

  const handleNativeShare = async () => {
    if (typeof navigator !== 'undefined' && navigator.share) {
      try {
        await navigator.share(shareData);
      } catch (err) {
        if ((err as Error).name !== 'AbortError') {
          copyToClipboard();
        }
      }
    } else {
      copyToClipboard();
    }
  };

  const copyToClipboard = () => {
    const url = typeof window !== 'undefined' ? window.location.href : shareData.url;
    if (navigator.clipboard) {
      navigator.clipboard.writeText(url).then(() => {
        setCopied(true);
        setTimeout(() => setCopied(false), 3000);
      });
    } else {
      const input = document.createElement('input');
      input.value = url;
      document.body.appendChild(input);
      input.select();
      document.execCommand('copy');
      document.body.removeChild(input);
      setCopied(true);
      setTimeout(() => setCopied(false), 3000);
    }
  };

  const openWhatsApp = () => {
    const text = encodeURIComponent(
      `💍 *Mansi ❤️ Risav Engagement Invitation*\n\nWith the blessings of Almighty & our families, you are cordially invited to celebrate our Engagement on *Sunday, 6th December 2026* at *Giraffe Resort, Raiganj*.\n\n✨ Open your personal invitation card & watch the 30s film here:\n${shareData.url}`
    );
    window.open(`https://api.whatsapp.com/send?text=${text}`, '_blank');
  };

  return (
    <section className="px-3 sm:px-4 py-6 max-w-4xl mx-auto">
      <div className="bg-gradient-to-r from-[#5B0616] via-[#801323] to-[#5B0616] rounded-3xl p-6 sm:p-8 text-center border-2 border-[#D4AF37] shadow-xl text-[#F3E5AB]">
        <h3 className="text-xl sm:text-3xl font-cinzel-dec font-black text-white mb-2">
          Share This Joy With Loved Ones
        </h3>
        <p className="text-xs sm:text-sm font-serif text-[#F3E5AB] max-w-lg mx-auto mb-6 opacity-90">
          Forward this digital invitation to family, relatives, and friends across WhatsApp and social media.
        </p>

        <div className="flex flex-col sm:flex-row items-center justify-center gap-3 max-w-md mx-auto">
          {/* Main Share Button */}
          <button
            onClick={handleNativeShare}
            className="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-6 py-3 rounded-full bg-[#D4AF37] text-[#5B0616] font-cinzel font-black text-xs uppercase tracking-wider shadow-lg hover:bg-[#F3E5AB] hover:scale-105 active:scale-95 transition-all"
          >
            <Share2 className="w-4 h-4 text-[#5B0616]" />
            <span>SHARE INVITATION</span>
          </button>

          {/* WhatsApp Quick Share */}
          <button
            onClick={openWhatsApp}
            className="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-6 py-3 rounded-full bg-[#25D366] text-white font-cinzel font-bold text-xs uppercase tracking-wider shadow-lg hover:bg-[#20ba59] hover:scale-105 active:scale-95 transition-all"
          >
            <MessageCircle className="w-4 h-4 fill-current" />
            <span>WhatsApp Share</span>
          </button>

          {/* Copy Link Button */}
          <button
            onClick={copyToClipboard}
            className="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-5 py-3 rounded-full bg-white/10 text-white border border-[#D4AF37]/50 font-cinzel font-semibold text-xs uppercase tracking-wider hover:bg-white/20 active:scale-95 transition-all"
          >
            {copied ? (
              <>
                <Check className="w-4 h-4 text-emerald-400" />
                <span className="text-emerald-300">Link Copied!</span>
              </>
            ) : (
              <>
                <Copy className="w-4 h-4 text-[#D4AF37]" />
                <span>Copy Link</span>
              </>
            )}
          </button>
        </div>
      </div>
    </section>
  );
}
