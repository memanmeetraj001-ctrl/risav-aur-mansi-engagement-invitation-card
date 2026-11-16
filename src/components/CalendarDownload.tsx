'use client';

import React, { useState } from 'react';
import { CalendarPlus, Check } from 'lucide-react';
import { generateEngagementICS } from '../utils/calendar';

export default function CalendarDownload() {
  const [downloaded, setDownloaded] = useState(false);

  const handleDownload = () => {
    generateEngagementICS();
    setDownloaded(true);
    setTimeout(() => setDownloaded(false), 4000);
  };

  return (
    <div className="inline-block">
      <button
        onClick={handleDownload}
        className="group inline-flex items-center gap-2.5 px-6 py-3.5 rounded-full bg-gradient-to-r from-[#D4AF37] via-[#F3E5AB] to-[#AA771C] text-[#5B0616] font-serif font-bold text-xs sm:text-sm tracking-wider uppercase shadow-[0_8px_20px_rgba(212,175,55,0.4)] hover:shadow-[0_10px_25px_rgba(212,175,55,0.6)] hover:scale-105 active:scale-100 transition-all duration-300"
      >
        {downloaded ? (
          <>
            <Check className="w-4 h-4 text-emerald-800" />
            <span>Calendar Saved!</span>
          </>
        ) : (
          <>
            <CalendarPlus className="w-4 h-4 text-[#5B0616] group-hover:rotate-12 transition-transform" />
            <span>ADD TO CALENDAR</span>
          </>
        )}
      </button>
    </div>
  );
}
