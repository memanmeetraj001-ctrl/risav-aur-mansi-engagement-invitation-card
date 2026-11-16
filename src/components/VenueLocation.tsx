'use client';

import React from 'react';
import { MapPin, ExternalLink, Navigation } from 'lucide-react';

export default function VenueLocation() {
  const googleMapsUrl = 'https://share.google/ltWlyblaDHHqS4iHx';
  const embedUrl =
    'https://maps.google.com/maps?q=Giraffe+Resort+Khalsi+Khoksa+Road+Mirual+Raiganj+West+Bengal+733130&t=&z=15&ie=UTF8&iwloc=&output=embed';

  return (
    <section id="venue" className="px-4 py-8 max-w-4xl mx-auto">
      <div className="bg-[#FCFAF5] rounded-3xl p-6 sm:p-10 border-2 border-[#D4AF37] shadow-xl text-center">
        {/* Header */}
        <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#5B0616] text-[#D4AF37] text-xs font-cinzel uppercase tracking-widest font-bold mb-3">
          <Navigation className="w-3.5 h-3.5" />
          <span>Interactive Location Guide</span>
        </div>

        <h2 className="text-2xl sm:text-4xl font-cinzel-dec font-black text-[#5B0616] mb-2">
          Giraffe Resort, Raiganj
        </h2>

        <p className="text-xs sm:text-sm text-[#801323] font-serif max-w-xl mx-auto mb-6">
          We eagerly await your gracious arrival to bless Mansi &amp; Risav. Click the button below to get turn-by-turn directions directly in Google Maps.
        </p>

        {/* PROMINENT GOLDEN/MAROON BUTTON */}
        <div className="mb-6">
          <a
            href={googleMapsUrl}
            target="_blank"
            rel="noopener noreferrer"
            className="group inline-flex items-center justify-center gap-3 px-8 py-4 rounded-full bg-gradient-to-r from-[#5B0616] via-[#801323] to-[#5B0616] text-[#F3E5AB] border-2 border-[#D4AF37] font-cinzel font-bold text-sm sm:text-base tracking-widest uppercase shadow-[0_10px_30px_rgba(91,6,22,0.4)] hover:shadow-[0_14px_35px_rgba(212,175,55,0.5)] hover:scale-105 active:scale-100 transition-all duration-300"
          >
            <MapPin className="w-5 h-5 text-[#D4AF37] group-hover:animate-bounce" />
            <span>VIEW VENUE LOCATION</span>
            <ExternalLink className="w-4 h-4 text-[#D4AF37]" />
          </a>
        </div>

        {/* Complete Address Below Button */}
        <div className="bg-[#F8F5EE] border border-[#D4AF37]/50 rounded-2xl p-4 max-w-lg mx-auto mb-8 text-xs sm:text-sm font-serif text-[#3B0612]">
          <p className="font-bold text-[#5B0616] mb-1 font-cinzel">
            Giraffe Resort
          </p>
          <p className="text-[#801323]">
            Khalsi - Khoksa Road, Mirual, Raiganj, Uttar Dinajpur, West Bengal – 733130.
          </p>
          <p className="text-[11px] text-gray-500 mt-2 font-sans">
            Preserved Google Maps Destination Link: {googleMapsUrl}
          </p>
        </div>

        {/* Embedded Google Map */}
        <div className="rounded-2xl overflow-hidden border-2 border-[#D4AF37] shadow-md relative w-full h-72 sm:h-96">
          <iframe
            title="Giraffe Resort Venue Map"
            src={embedUrl}
            width="100%"
            height="100%"
            style={{ border: 0 }}
            allowFullScreen={false}
            loading="lazy"
            referrerPolicy="no-referrer-when-downgrade"
            className="w-full h-full"
          />
          <div className="absolute top-2 right-2 bg-white/90 backdrop-blur-sm px-3 py-1.5 rounded-lg border border-[#D4AF37] shadow text-[11px] font-cinzel font-semibold text-[#5B0616]">
            Raiganj, West Bengal
          </div>
        </div>
      </div>
    </section>
  );
}
