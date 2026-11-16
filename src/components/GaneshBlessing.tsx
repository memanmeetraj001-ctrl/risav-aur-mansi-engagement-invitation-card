'use client';

import React from 'react';

export default function GaneshBlessing() {
  return (
    <section className="text-center pt-8 pb-4 px-4 max-w-2xl mx-auto">
      {/* Golden Ganesha Icon with Radiant Aura */}
      <div className="relative inline-block mb-3">
        <div className="absolute inset-0 bg-[#D4AF37]/30 blur-2xl rounded-full transform scale-125 animate-pulse" />
        {/* eslint-disable-next-line @next/next/no-img-element */}
        <img
          src="/images/ganesha-gold.png"
          alt="Lord Ganesha"
          className="relative w-24 h-24 sm:w-28 sm:h-28 mx-auto object-contain drop-shadow-[0_4px_16px_rgba(212,175,55,0.5)] hover:scale-105 transition-transform duration-500"
        />
      </div>

      <div className="space-y-2">
        <h3 className="text-base sm:text-xl font-cinzel-dec font-black tracking-[0.2em] text-[#5B0616] uppercase">
          || Shree Ganeshaya Namah ||
        </h3>

        <p className="text-sm sm:text-base font-serif italic text-[#801323] max-w-lg mx-auto opacity-95 leading-relaxed font-medium">
          वक्रतुण्ड महाकाय सूर्यकोटि समप्रभ ।<br />
          निर्विघ्नं कुरु मे देव सर्वकार्येषु सर्वदा ॥
        </p>

        {/* Ornate Gold Divider */}
        <div className="flex items-center justify-center gap-3 py-3">
          <div className="w-16 sm:w-24 h-[1.5px] bg-gradient-to-r from-transparent to-[#D4AF37]" />
          <div className="w-2.5 h-2.5 rotate-45 bg-[#D4AF37] border border-[#5B0616]" />
          <div className="w-16 sm:w-24 h-[1.5px] bg-gradient-to-l from-transparent to-[#D4AF37]" />
        </div>

        <p className="text-xs sm:text-sm uppercase tracking-[0.25em] font-cinzel font-bold text-[#8A9A86]">
          With the blessings of Almighty &amp; our beloved family
        </p>

        <p className="text-xs sm:text-sm font-serif text-[#5B0616] tracking-wide pt-1">
          We request your gracious presence at the auspicious engagement celebrations of
        </p>
      </div>
    </section>
  );
}
