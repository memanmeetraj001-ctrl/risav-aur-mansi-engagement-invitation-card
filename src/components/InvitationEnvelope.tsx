'use client';

import React, { useState } from 'react';
import confetti from 'canvas-confetti';
import { MailOpen, Sparkles, Heart } from 'lucide-react';

interface InvitationEnvelopeProps {
  onOpen: () => void;
  isOpen: boolean;
}

export default function InvitationEnvelope({ onOpen, isOpen }: InvitationEnvelopeProps) {
  const [opening, setOpening] = useState(false);

  const handleOpen = () => {
    setOpening(true);

    try {
      confetti({
        particleCount: 100,
        spread: 75,
        origin: { y: 0.6 },
        colors: ['#D4AF37', '#FFD700', '#FAD2E1', '#800020', '#FFFFFF', '#AA771C'],
      });

      setTimeout(() => {
        confetti({
          particleCount: 60,
          angle: 60,
          spread: 60,
          origin: { x: 0 },
          colors: ['#D4AF37', '#FAD2E1', '#800020'],
        });
        confetti({
          particleCount: 60,
          angle: 120,
          spread: 60,
          origin: { x: 1 },
          colors: ['#D4AF37', '#FAD2E1', '#800020'],
        });
      }, 250);
    } catch (e) {
      console.log('Confetti effect:', e);
    }

    setTimeout(() => {
      onOpen();
    }, 700);
  };

  if (isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-[#1A0105]/85 backdrop-blur-md px-4 py-8 overflow-y-auto">
      {/* Background Floating Golden Lanterns & Lights */}
      <div className="absolute inset-0 pointer-events-none opacity-50 overflow-hidden">
        <div className="absolute top-4 left-8 w-24 h-36 border-t-2 border-[#D4AF37] flex flex-col items-center animate-pulse">
          <div className="w-[1px] h-12 bg-[#D4AF37]" />
          <div className="w-9 h-14 rounded-sm bg-gradient-to-b from-[#D4AF37] to-[#800020] shadow-[0_0_20px_#D4AF37]" />
        </div>
        <div className="absolute top-4 right-8 w-24 h-36 border-t-2 border-[#D4AF37] flex flex-col items-center animate-pulse">
          <div className="w-[1px] h-16 bg-[#D4AF37]" />
          <div className="w-9 h-14 rounded-sm bg-gradient-to-b from-[#D4AF37] to-[#800020] shadow-[0_0_20px_#D4AF37]" />
        </div>
      </div>

      {/* Royal Invitation Envelope Card */}
      <div
        className={`relative w-full max-w-lg bg-[#FCFAF5] rounded-3xl p-6 sm:p-10 border-4 border-[#D4AF37] shadow-[0_30px_70px_-15px_rgba(0,0,0,0.85)] text-center transition-all duration-700 transform ${
          opening ? 'scale-95 opacity-0 -translate-y-8' : 'scale-100 opacity-100 translate-y-0'
        }`}
      >
        {/* Ornate Corner Elements */}
        <div className="absolute top-3 left-3 w-8 h-8 border-t-2 border-l-2 border-[#D4AF37]" />
        <div className="absolute top-3 right-3 w-8 h-8 border-t-2 border-r-2 border-[#D4AF37]" />
        <div className="absolute bottom-3 left-3 w-8 h-8 border-b-2 border-l-2 border-[#D4AF37]" />
        <div className="absolute bottom-3 right-3 w-8 h-8 border-b-2 border-r-2 border-[#D4AF37]" />

        {/* Religious Ganesh Motif Top */}
        <div className="flex justify-center mb-2">
          {/* eslint-disable-next-line @next/next/no-img-element */}
          <img
            src="/images/ganesha-gold.png"
            alt="Lord Ganesha"
            className="w-16 h-16 object-contain drop-shadow-[0_2px_10px_rgba(212,175,55,0.5)]"
          />
        </div>

        <p className="text-xs uppercase tracking-[0.25em] text-[#801323] font-cinzel font-bold">
          || Shree Ganeshaya Namah ||
        </p>

        <div className="w-24 h-[1.5px] bg-gradient-to-r from-transparent via-[#D4AF37] to-transparent mx-auto my-3" />

        {/* Envelope Center Graphic with 3D Wax Seal Monogram */}
        <div className="relative my-6 mx-auto w-40 h-40 sm:w-44 sm:h-44 rounded-full bg-gradient-to-tr from-[#3D030E] via-[#801323] to-[#5B0616] p-1.5 shadow-[0_15px_30px_rgba(0,0,0,0.45)] flex items-center justify-center border-2 border-[#D4AF37]">
          {/* Inner Golden Ring */}
          <div className="w-full h-full rounded-full border border-dashed border-[#F3E5AB] flex flex-col items-center justify-center p-3 text-center">
            <span className="text-[10px] uppercase tracking-widest text-[#F3E5AB] font-cinzel font-semibold">
              Royal Seal
            </span>
            <div className="my-1 text-3xl sm:text-4xl font-cinzel-dec font-black tracking-wider text-[#FBF5B7] drop-shadow-[0_2px_4px_rgba(0,0,0,0.6)]">
              M <span className="text-xl font-great-vibes text-[#D4AF37]">&amp;</span> R
            </div>
            <div className="flex items-center gap-1 text-[#FAD2E1] text-[11px] font-medium font-serif">
              <Heart className="w-3 h-3 fill-current text-rose-400" />
              <span>Forever</span>
            </div>
          </div>

          {/* Golden Seal Ring Sparkle */}
          <div className="absolute -top-1 -right-1 w-6 h-6 rounded-full bg-[#D4AF37] flex items-center justify-center shadow-lg animate-ping">
            <Sparkles className="w-3.5 h-3.5 text-white" />
          </div>
        </div>

        <h2 className="text-xs sm:text-sm uppercase tracking-[0.25em] font-cinzel text-[#8A9A86] font-bold mb-1">
          Auspicious Engagement Invitation
        </h2>

        <h1 className="text-3xl sm:text-4xl font-cinzel-dec font-black text-[#5B0616] tracking-wide mb-1">
          MANSI &amp; RISAV
        </h1>

        <p className="text-xl sm:text-2xl font-great-vibes text-[#801323] mb-6">
          You Are Cordially Invited
        </p>

        {/* Open Button */}
        <button
          onClick={handleOpen}
          disabled={opening}
          className="group relative inline-flex items-center justify-center gap-3 px-8 py-3.5 rounded-full bg-gradient-to-r from-[#D4AF37] via-[#F3E5AB] to-[#AA771C] text-[#4A0412] font-cinzel font-bold text-sm tracking-wider uppercase shadow-[0_8px_25px_rgba(212,175,55,0.45)] hover:shadow-[0_12px_30px_rgba(212,175,55,0.6)] transform hover:-translate-y-0.5 active:translate-y-0 transition-all duration-300"
        >
          <MailOpen className="w-5 h-5 text-[#5B0616] group-hover:rotate-12 transition-transform duration-300" />
          <span>{opening ? 'Opening Celebration...' : 'OPEN INVITATION'}</span>
        </button>

        <p className="text-[11px] text-[#8A9A86] mt-4 font-sans font-medium">
          🎵 Tap to open with music &amp; full celebrations
        </p>
      </div>
    </div>
  );
}
