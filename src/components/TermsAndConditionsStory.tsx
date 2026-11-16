'use client';

import React from 'react';
import { CheckCircle2, HeartHandshake, Heart, Sparkles } from 'lucide-react';

export default function TermsAndConditionsStory() {
  const vows = [
    'Daily Cuddles & Morning Chai',
    'Unlimited Selfies & Photo Sessions',
    'Dedicated Shopping Companion',
    'Weekend Movie Nights & Popcorn',
    'Unlimited Warm Hugs in all seasons',
    'Annoying Each Other with love forever',
    'Beside Each Other through every storm',
    'Late Night Conversations & Big Dreams',
    'Lifetime Mutual Support & Friendship',
    'Unconditional Respect & Understanding',
    'Growing Old Together Hand in Hand',
  ];

  return (
    <section className="px-4 py-8 max-w-4xl mx-auto">
      <div className="bg-gradient-to-br from-[#FCFAF5] to-[#F5EEDB] rounded-3xl p-6 sm:p-10 border-2 border-[#D4AF37] shadow-xl">
        <div className="text-center mb-6">
          <div className="inline-flex items-center gap-2 px-4 py-1 rounded-full bg-[#5B0616] text-[#D4AF37] text-xs font-cinzel font-bold uppercase tracking-wider mb-2">
            <HeartHandshake className="w-4 h-4 text-[#D4AF37]" />
            <span>Romantic Agreement</span>
          </div>
          <h2 className="text-2xl sm:text-4xl font-cinzel-dec font-black text-[#5B0616] flex items-center justify-center gap-2">
            <span>Terms &amp; Conditions Accepted</span>
            <Heart className="w-7 h-7 sm:w-9 sm:h-9 text-rose-600 fill-rose-600 animate-pulse" />
          </h2>
          <p className="text-xl sm:text-2xl font-great-vibes text-[#801323] mt-1">
            Signed for a lifetime of boundless happiness, laughter and adventure
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-12 gap-8 items-center">
          {/* Couple Image with Scroll */}
          <div className="md:col-span-5 text-center">
            <div className="relative rounded-2xl overflow-hidden border-2 border-[#D4AF37] shadow-lg max-w-xs mx-auto">
              {/* eslint-disable-next-line @next/next/no-img-element */}
              <img
                src="/images/couple-terms.jpg"
                alt="Risav & Mansi Terms and Conditions Accepted"
                className="w-full h-auto object-cover hover:scale-105 transition-transform duration-500"
              />
              <div className="absolute bottom-2 left-2 right-2 bg-white/95 backdrop-blur-sm rounded-lg py-1 px-2 text-[11px] font-cinzel font-bold text-[#5B0616] border border-[#D4AF37]">
                Official Agreement • Signed: Mansi &amp; Risav
              </div>
            </div>
          </div>

          {/* Vow Checklist */}
          <div className="md:col-span-7 space-y-2.5">
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs font-serif">
              {vows.map((vow, i) => (
                <div
                  key={i}
                  className="flex items-center gap-2 bg-white/90 p-2.5 rounded-xl border border-[#D4AF37]/40 shadow-sm"
                >
                  <CheckCircle2 className="w-4 h-4 text-emerald-600 flex-shrink-0" />
                  <span className="text-[#3B0612] font-medium">{vow}</span>
                </div>
              ))}
            </div>

            <div className="mt-4 p-3 bg-[#5B0616] text-white rounded-xl text-center font-cinzel text-xs border border-[#D4AF37] flex items-center justify-center gap-2">
              <Sparkles className="w-4 h-4 text-[#D4AF37]" />
              <span className="tracking-widest font-black uppercase text-[#F3E5AB]">
                STATUS: OFFICIALLY ACCEPTED &amp; SEALED FOREVER
              </span>
              <Sparkles className="w-4 h-4 text-[#D4AF37]" />
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
