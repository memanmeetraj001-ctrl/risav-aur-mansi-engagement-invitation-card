'use client';

import React from 'react';
import { Heart, Sparkles } from 'lucide-react';

export default function CoupleReveal() {
  return (
    <section className="relative text-center px-4 py-6 max-w-3xl mx-auto">
      {/* Royal Monogram Medallion */}
      <div className="inline-flex items-center justify-center mb-5">
        <div className="relative w-20 h-20 rounded-full border-2 border-[#D4AF37] bg-gradient-to-br from-[#5B0616] to-[#3D030E] p-1 shadow-xl">
          <div className="w-full h-full rounded-full border border-dashed border-[#F3E5AB]/70 flex items-center justify-center">
            <span className="font-cinzel-dec font-black text-xl text-[#F3E5AB] tracking-widest">
              M <span className="text-xs font-great-vibes text-[#D4AF37]">&amp;</span> R
            </span>
          </div>
          <div className="absolute -bottom-1.5 left-1/2 -translate-x-1/2 bg-[#D4AF37] text-[#5B0616] text-[9px] uppercase px-2.5 py-0.5 rounded-full font-cinzel font-bold tracking-wider shadow">
            Forever
          </div>
        </div>
      </div>

      {/* Main Couple Names */}
      <div className="space-y-1 mb-4">
        <h1 className="text-4xl sm:text-6xl font-cinzel-dec font-black tracking-wide text-[#5B0616] drop-shadow-sm flex items-center justify-center gap-3">
          <span>MANSI</span>
          <Heart className="w-8 h-8 sm:w-11 sm:h-11 text-rose-600 fill-rose-600 animate-pulse" />
          <span>RISAV</span>
        </h1>

        <div className="flex items-center justify-center gap-3 py-2">
          <div className="w-12 sm:w-20 h-[1.5px] bg-[#D4AF37]" />
          <h2 className="text-sm sm:text-base font-cinzel font-bold uppercase tracking-[0.35em] text-[#801323]">
            ENGAGEMENT CEREMONY
          </h2>
          <div className="w-12 sm:w-20 h-[1.5px] bg-[#D4AF37]" />
        </div>
      </div>

      {/* Couple Proposal Cartoon Picture with Animated Frame & Sparkles */}
      <div className="relative mx-auto max-w-md sm:max-w-lg my-6 group">
        {/* Glowing Backdrop */}
        <div className="absolute -inset-2 bg-gradient-to-r from-[#D4AF37]/40 via-rose-300/35 to-[#D4AF37]/40 rounded-[2.5rem] blur-xl opacity-85 group-hover:opacity-100 transition-opacity duration-700" />

        {/* Ornate Arch Frame Container */}
        <div className="relative rounded-[2.5rem] overflow-hidden border-4 border-[#D4AF37] bg-[#FCFAF5] shadow-[0_20px_50px_rgba(91,6,22,0.35)]">
          {/* Couple Proposal Image */}
          {/* eslint-disable-next-line @next/next/no-img-element */}
          <img
            src="/images/couple-proposal.jpg"
            alt="Risav proposing to Mansi - Cartoon Couple"
            className="w-full h-auto object-cover transform hover:scale-105 transition-transform duration-700"
          />

          {/* Interactive Sparkle over the Diamond Ring */}
          <div
            className="absolute top-[48%] left-[54%] -translate-x-1/2 -translate-y-1/2 pointer-events-none"
            title="Diamond Ring Sparkle"
          >
            <div className="relative">
              <div className="w-8 h-8 rounded-full bg-white/95 blur-[2px] animate-ping" />
              <Sparkles className="absolute inset-0 w-7 h-7 text-amber-200 fill-white drop-shadow-[0_0_15px_#FFF]" />
            </div>
          </div>

          {/* Floating Hearts Animation overlay */}
          <div className="absolute inset-0 pointer-events-none overflow-hidden">
            <Heart className="absolute top-10 left-8 w-5 h-5 text-rose-500 fill-rose-500/70 animate-bounce" style={{ animationDuration: '3s' }} />
            <Heart className="absolute top-20 right-10 w-6 h-6 text-rose-500 fill-rose-500/70 animate-bounce" style={{ animationDuration: '4s' }} />
            <Heart className="absolute bottom-24 left-12 w-4 h-4 text-rose-400 fill-rose-400/70 animate-bounce" style={{ animationDuration: '2.5s' }} />
          </div>

          {/* Bottom Card Ribbon */}
          <div className="absolute bottom-0 inset-x-0 bg-gradient-to-t from-[#5B0616]/95 via-[#5B0616]/80 to-transparent pt-8 pb-4 px-4 text-center">
            <p className="text-white font-great-vibes text-2xl sm:text-3xl drop-shadow-md">
              &ldquo;She said YES! Two souls unite in eternal love.&rdquo;
            </p>
          </div>
        </div>
      </div>

      <p className="text-xs sm:text-sm font-serif italic text-[#8A9A86] max-w-md mx-auto">
        Together with our families, we take the first step towards a lifetime of happiness, laughter, and companionship.
      </p>
    </section>
  );
}
