'use client';

import React from 'react';
import { Heart } from 'lucide-react';

export default function FamilyIntroduction() {
  return (
    <section className="px-4 py-8 max-w-4xl mx-auto">
      <div className="text-center mb-6">
        <h3 className="text-xs uppercase tracking-[0.25em] font-cinzel font-bold text-[#8A9A86] mb-1">
          With Love &amp; Respect
        </h3>
        <h2 className="text-2xl sm:text-3xl font-cinzel-dec font-black text-[#5B0616]">
          The Happy Couple &amp; Families
        </h2>
        <div className="w-20 h-[1.5px] bg-[#D4AF37] mx-auto mt-2" />
      </div>

      <div className="grid grid-cols-1 md:grid-cols-12 gap-6 items-center">
        {/* Groom's Family Card */}
        <div className="md:col-span-4 bg-[#FCFAF5] rounded-3xl p-6 border-2 border-[#D4AF37] shadow-lg text-center hover:shadow-xl transition-shadow relative">
          <div className="inline-block px-3 py-1 bg-[#5B0616] text-[#D4AF37] text-[10px] font-cinzel uppercase tracking-widest rounded-full font-bold mb-3">
            The Groom
          </div>
          <h4 className="text-2xl sm:text-3xl font-cinzel-dec font-black text-[#5B0616] tracking-wide mb-2">
            RISAV
          </h4>
          <div className="text-xs text-[#801323] space-y-1 font-serif leading-relaxed">
            <p className="font-semibold text-gray-500 uppercase tracking-wider text-[10px] font-sans">
              Beloved Son of
            </p>
            <p className="font-bold text-sm sm:text-base text-[#3B0612] font-serif">
              Mr. Binod Prasad Gupta
            </p>
            <p className="text-xs text-gray-600">&amp;</p>
            <p className="font-bold text-sm sm:text-base text-[#3B0612] font-serif">
              Mrs. Pushpa Devi
            </p>
          </div>
        </div>

        {/* Center Couple Portrait Card */}
        <div className="md:col-span-4 flex flex-col items-center">
          <div className="relative w-48 h-64 sm:w-56 sm:h-72 rounded-full overflow-hidden border-4 border-[#D4AF37] shadow-[0_15px_35px_rgba(91,6,22,0.3)] p-1 bg-[#FCFAF5]">
            <div className="w-full h-full rounded-full overflow-hidden">
              {/* eslint-disable-next-line @next/next/no-img-element */}
              <img
                src="/images/couple-portrait.jpg"
                alt="Risav and Mansi"
                className="w-full h-full object-cover object-top hover:scale-105 transition-transform duration-500"
              />
            </div>
            <div className="absolute -bottom-1 left-1/2 -translate-x-1/2 bg-[#5B0616] text-[#D4AF37] p-2 rounded-full border border-[#D4AF37] shadow-md">
              <Heart className="w-5 h-5 fill-rose-500 text-rose-500" />
            </div>
          </div>
          <p className="mt-3 text-xl font-great-vibes text-[#801323]">
            Mansi &amp; Risav
          </p>
        </div>

        {/* Bride's Family Card */}
        <div className="md:col-span-4 bg-[#FCFAF5] rounded-3xl p-6 border-2 border-[#D4AF37] shadow-lg text-center hover:shadow-xl transition-shadow relative">
          <div className="inline-block px-3 py-1 bg-[#801323] text-[#F3E5AB] text-[10px] font-cinzel uppercase tracking-widest rounded-full font-bold mb-3">
            The Bride
          </div>
          <h4 className="text-2xl sm:text-3xl font-cinzel-dec font-black text-[#5B0616] tracking-wide mb-2">
            MANSI
          </h4>
          <div className="text-xs text-[#801323] space-y-1 font-serif leading-relaxed">
            <p className="font-semibold text-gray-500 uppercase tracking-wider text-[10px] font-sans">
              Beloved Daughter of
            </p>
            <p className="font-bold text-sm sm:text-base text-[#3B0612] font-serif">
              Mr. Sanjeev Kumar Suman
            </p>
            <p className="text-xs text-gray-600">&amp;</p>
            <p className="font-bold text-sm sm:text-base text-[#3B0612] font-serif">
              Mrs. Manorama Devi
            </p>
            <div className="w-12 h-[1px] bg-[#D4AF37] mx-auto my-2" />
            <p className="font-semibold text-gray-500 uppercase tracking-wider text-[10px] font-sans">
              Loving Brother
            </p>
            <p className="font-bold text-sm text-[#801323] font-serif">
              Mr. Manmeet Raj
            </p>
          </div>
        </div>
      </div>
    </section>
  );
}
