'use client';

import React, { useState, useEffect } from 'react';
import { Calendar, Clock, MapPin, Sparkles } from 'lucide-react';

export default function EventDetails() {
  const [timeLeft, setTimeLeft] = useState({
    days: 0,
    hours: 0,
    minutes: 0,
    seconds: 0,
  });

  useEffect(() => {
    // Target: Sunday, 6th December 2026 at 6:00 PM IST (+05:30)
    const targetDate = new Date('2026-12-06T18:00:00+05:30').getTime();

    const updateTimer = () => {
      const now = new Date().getTime();
      const difference = targetDate - now;

      if (difference > 0) {
        setTimeLeft({
          days: Math.floor(difference / (1000 * 60 * 60 * 24)),
          hours: Math.floor((difference / (1000 * 60 * 60)) % 24),
          minutes: Math.floor((difference / 1000 / 60) % 60),
          seconds: Math.floor((difference / 1000) % 60),
        });
      } else {
        setTimeLeft({ days: 0, hours: 0, minutes: 0, seconds: 0 });
      }
    };

    updateTimer();
    const interval = setInterval(updateTimer, 1000);
    return () => clearInterval(interval);
  }, []);

  return (
    <section className="px-4 py-8 max-w-4xl mx-auto">
      <div className="text-center mb-6">
        <h3 className="text-xs uppercase tracking-[0.25em] font-cinzel font-bold text-[#8A9A86] mb-1">
          Auspicious Schedule
        </h3>
        <h2 className="text-2xl sm:text-3xl font-cinzel-dec font-black text-[#5B0616]">
          Event Date, Time &amp; Venue
        </h2>
        <div className="w-20 h-[1.5px] bg-[#D4AF37] mx-auto mt-2" />
      </div>

      {/* Countdown Timer Banner */}
      <div className="mb-8 p-4 rounded-2xl bg-gradient-to-r from-[#5B0616] via-[#801323] to-[#5B0616] text-[#D4AF37] border-2 border-[#D4AF37] shadow-xl text-center">
        <div className="flex items-center justify-center gap-2 mb-3 text-xs font-cinzel uppercase tracking-widest text-[#F3E5AB] font-bold">
          <Sparkles className="w-3.5 h-3.5" />
          <span>Counting Down to the Auspicious Moment</span>
          <Sparkles className="w-3.5 h-3.5" />
        </div>
        <div className="grid grid-cols-4 gap-2 max-w-sm sm:max-w-md mx-auto">
          {[
            { label: 'Days', value: timeLeft.days },
            { label: 'Hours', value: timeLeft.hours },
            { label: 'Minutes', value: timeLeft.minutes },
            { label: 'Seconds', value: timeLeft.seconds },
          ].map((item, idx) => (
            <div
              key={idx}
              className="bg-[#3D030E]/80 rounded-xl p-2.5 border border-[#D4AF37]/40 flex flex-col items-center shadow-inner"
            >
              <span className="text-xl sm:text-3xl font-cinzel font-bold text-white">
                {String(item.value).padStart(2, '0')}
              </span>
              <span className="text-[10px] uppercase tracking-wider text-[#D4AF37] mt-0.5 font-sans">
                {item.label}
              </span>
            </div>
          ))}
        </div>
      </div>

      {/* Event Details Cards */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {/* Date Card */}
        <div className="bg-[#FCFAF5] rounded-3xl p-6 border-2 border-[#D4AF37] shadow-md text-center hover:scale-[1.02] transition-transform">
          <div className="w-12 h-12 rounded-full bg-[#5B0616] text-[#D4AF37] flex items-center justify-center mx-auto mb-3 shadow">
            <Calendar className="w-6 h-6" />
          </div>
          <h4 className="text-xs uppercase tracking-widest font-cinzel font-bold text-[#8A9A86] mb-1">
            DATE
          </h4>
          <p className="text-base sm:text-lg font-cinzel font-bold text-[#5B0616]">
            Sunday, 6th December
          </p>
          <p className="text-3xl font-cinzel-dec font-black text-[#801323]">
            2026
          </p>
          <p className="text-xs font-serif italic text-gray-500 mt-2 font-medium">
            Auspicious Muhurat
          </p>
        </div>

        {/* Time Card */}
        <div className="bg-[#FCFAF5] rounded-3xl p-6 border-2 border-[#D4AF37] shadow-md text-center hover:scale-[1.02] transition-transform">
          <div className="w-12 h-12 rounded-full bg-[#5B0616] text-[#D4AF37] flex items-center justify-center mx-auto mb-3 shadow">
            <Clock className="w-6 h-6" />
          </div>
          <h4 className="text-xs uppercase tracking-widest font-cinzel font-bold text-[#8A9A86] mb-1">
            TIME
          </h4>
          <p className="text-lg sm:text-xl font-cinzel font-bold text-[#5B0616]">
            6:00 PM Onwards
          </p>
          <p className="text-xs font-serif italic text-gray-500 mt-3 font-medium">
            Followed by dinner &amp; musical celebration
          </p>
        </div>

        {/* Venue Card */}
        <div className="bg-[#FCFAF5] rounded-3xl p-6 border-2 border-[#D4AF37] shadow-md text-center hover:scale-[1.02] transition-transform">
          <div className="w-12 h-12 rounded-full bg-[#5B0616] text-[#D4AF37] flex items-center justify-center mx-auto mb-3 shadow">
            <MapPin className="w-6 h-6" />
          </div>
          <h4 className="text-xs uppercase tracking-widest font-cinzel font-bold text-[#8A9A86] mb-1">
            VENUE
          </h4>
          <p className="text-lg sm:text-xl font-cinzel-dec font-bold text-[#5B0616]">
            Giraffe Resort
          </p>
          <p className="text-xs font-serif text-[#801323] mt-1 leading-snug">
            Khalsi - Khoksa Road, Mirual, Raiganj, Uttar Dinajpur, West Bengal – 733130
          </p>
        </div>
      </div>
    </section>
  );
}
