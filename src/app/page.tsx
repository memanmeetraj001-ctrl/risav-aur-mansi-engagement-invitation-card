'use client';

import React, { useState } from 'react';
import {
  Film,
  MapPin,
  CalendarPlus,
  Share2,
  Download,
  RotateCcw,
  Heart,
  Sparkles,
} from 'lucide-react';

import InvitationEnvelope from '../components/InvitationEnvelope';
import GaneshBlessing from '../components/GaneshBlessing';
import CoupleReveal from '../components/CoupleReveal';
import FamilyIntroduction from '../components/FamilyIntroduction';
import TermsAndConditionsStory from '../components/TermsAndConditionsStory';
import EventDetails from '../components/EventDetails';
import VenueLocation from '../components/VenueLocation';
import VideoPlayerSection from '../components/VideoPlayerSection';
import ShareInvitation from '../components/ShareInvitation';
import MusicPlayer from '../components/MusicPlayer';
import { generateEngagementICS } from '../utils/calendar';

export default function EngagementPage() {
  const [isEnvelopeOpen, setIsEnvelopeOpen] = useState(false);
  const [startMusic, setStartMusic] = useState(false);

  const handleOpenEnvelope = () => {
    setIsEnvelopeOpen(true);
    setStartMusic(true);
  };

  const handlePlayAgain = () => {
    setIsEnvelopeOpen(false);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const handleWatchVideo = () => {
    const el = document.getElementById('video-invitation');
    if (el) {
      el.scrollIntoView({ behavior: 'smooth' });
    }
  };

  const handleViewVenue = () => {
    window.open('https://share.google/ltWlyblaDHHqS4iHx', '_blank');
  };

  return (
    <main className="min-h-screen relative bg-mandala-pattern pb-28 pt-3 sm:pt-4 overflow-hidden">
      {/* Floating Decorative Lanterns (Top Left & Top Right) */}
      <div className="fixed top-0 left-2 sm:left-10 z-20 pointer-events-none floating-lantern opacity-80 scale-90 sm:scale-100">
        <div className="w-[1.5px] h-14 sm:h-24 bg-gradient-to-b from-[#996515] to-[#D4AF37] mx-auto" />
        <div className="w-9 sm:w-14 h-12 sm:h-20 rounded-md bg-gradient-to-b from-[#D4AF37] via-[#AA771C] to-[#5B0616] p-1 border border-[#FFE29A] shadow-[0_0_15px_#D4AF37] flex flex-col items-center justify-between">
          <div className="w-5 h-1 bg-[#FFE29A] rounded-full" />
          <div className="w-3.5 h-3.5 rounded-full bg-[#FFE29A] animate-ping" />
          <div className="w-2 h-3.5 bg-[#AA771C]" />
        </div>
        <div className="w-[1.5px] h-5 bg-[#D4AF37] mx-auto" />
      </div>

      <div className="fixed top-0 right-2 sm:right-10 z-20 pointer-events-none floating-lantern opacity-80 scale-90 sm:scale-100" style={{ animationDelay: '1.5s' }}>
        <div className="w-[1.5px] h-16 sm:h-28 bg-gradient-to-b from-[#996515] to-[#D4AF37] mx-auto" />
        <div className="w-9 sm:w-14 h-12 sm:h-20 rounded-md bg-gradient-to-b from-[#D4AF37] via-[#AA771C] to-[#5B0616] p-1 border border-[#FFE29A] shadow-[0_0_15px_#D4AF37] flex flex-col items-center justify-between">
          <div className="w-5 h-1 bg-[#FFE29A] rounded-full" />
          <div className="w-3.5 h-3.5 rounded-full bg-[#FFE29A] animate-ping" />
          <div className="w-2 h-3.5 bg-[#AA771C]" />
        </div>
        <div className="w-[1.5px] h-5 bg-[#D4AF37] mx-auto" />
      </div>

      {/* Music Player Controller */}
      <MusicPlayer autoPlayTrigger={startMusic} />

      {/* Opening Screen Envelope Modal */}
      <InvitationEnvelope onOpen={handleOpenEnvelope} isOpen={isEnvelopeOpen} />

      {/* Main Invitation Container */}
      <div className="max-w-4xl mx-auto px-3 sm:px-6">
        {/* Top Quick Actions Bar (Visible after opening) */}
        {isEnvelopeOpen && (
          <div className="flex flex-col sm:flex-row items-center justify-between gap-2.5 py-2.5 px-4 mb-4 rounded-2xl bg-white/90 backdrop-blur-md border border-[#D4AF37]/50 shadow-sm text-xs font-serif">
            <div className="flex items-center gap-2 text-[#5B0616] font-cinzel font-bold tracking-wider text-center">
              <Sparkles className="w-4 h-4 text-[#D4AF37]" />
              <span>Mansi &amp; Risav • 6th Dec 2026</span>
            </div>

            <div className="flex items-center gap-2">
              <button
                onClick={handlePlayAgain}
                className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-[#FCFAF5] text-[#5B0616] border border-[#D4AF37] font-cinzel font-bold text-[11px] hover:bg-[#F3E5AB]/40 active:scale-95 transition-all"
                title="Play Opening Animation Again"
              >
                <RotateCcw className="w-3.5 h-3.5" />
                <span>PLAY AGAIN</span>
              </button>

              <button
                onClick={handleWatchVideo}
                className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-[#5B0616] text-[#D4AF37] font-cinzel font-bold text-[11px] hover:bg-[#801323] active:scale-95 transition-all"
              >
                <Film className="w-3.5 h-3.5" />
                <span>WATCH VIDEO</span>
              </button>
            </div>
          </div>
        )}

        {/* 1. Ganesha Blessing */}
        <GaneshBlessing />

        {/* 2. Couple Reveal & Proposal Story */}
        <CoupleReveal />

        {/* 3. Family Introductions */}
        <FamilyIntroduction />

        {/* 4. Romantic Terms & Conditions Story */}
        <TermsAndConditionsStory />

        {/* 5. Event Schedule & Live Countdown */}
        <EventDetails />

        {/* 6. Venue Location with Google Maps & Button */}
        <VenueLocation />

        {/* 7. 30-Second Video Player & Download (Clean & Mobile-Friendly, without the breakdown table) */}
        <VideoPlayerSection />

        {/* 8. Special Invitation by Gublu & Warm Blessing */}
        <section className="px-3 sm:px-4 py-6 sm:py-8 text-center max-w-2xl mx-auto">
          <div className="p-6 sm:p-8 rounded-3xl bg-gradient-to-b from-[#FCFAF5] to-[#F5F0E6] border-2 border-[#D4AF37] shadow-xl relative overflow-hidden">
            {/* Top decorative badge */}
            <div className="inline-flex items-center gap-1.5 px-3.5 py-1 bg-[#5B0616] text-[#D4AF37] text-[11px] font-cinzel uppercase tracking-widest rounded-full font-bold mb-4 shadow-sm">
              <Sparkles className="w-3.5 h-3.5" />
              <span>Special Invitation</span>
              <Sparkles className="w-3.5 h-3.5" />
            </div>

            {/* Gublu with Couple Image */}
            <div className="relative w-48 h-64 sm:w-56 sm:h-72 mx-auto mb-5 rounded-2xl overflow-hidden border-4 border-[#D4AF37] shadow-[0_10px_25px_rgba(91,6,22,0.25)] p-1 bg-[#FCFAF5]">
              <div className="w-full h-full rounded-xl overflow-hidden">
                {/* eslint-disable-next-line @next/next/no-img-element */}
                <img
                  src="/images/gublu-invitation.jpg"
                  alt="Mansi, Risav and Baby Gublu"
                  className="w-full h-full object-cover object-top hover:scale-105 transition-transform duration-500"
                />
              </div>
            </div>

            <Heart className="w-7 h-7 text-rose-500 fill-rose-500 mx-auto mb-2 animate-pulse" />
            
            <h3 className="text-xl sm:text-2xl font-cinzel font-bold text-[#5B0616] mb-2 leading-snug">
              &ldquo;Mere Massi ke Engagement me jarur se jarur aayean.&rdquo;
            </h3>
            
            <p className="text-base sm:text-lg font-serif font-semibold text-[#801323] italic mb-3">
              — Special request by Gublu ❤️
            </p>

            <p className="text-xl sm:text-3xl font-great-vibes text-[#801323] leading-relaxed max-w-md mx-auto">
              Your presence will make our special day even more memorable.<br />
              Reliving this moment forever ❤️
            </p>

            <div className="w-20 h-[1.5px] bg-[#D4AF37] mx-auto my-4" />

            <p className="text-xs sm:text-sm font-serif font-bold text-[#5B0616]">
              With Warm Blessings &amp; Regards:
            </p>
            <p className="text-[11px] sm:text-xs font-serif text-[#801323] mt-1">
              Gupta &amp; Suman Families • Bride&apos;s Brother: <span className="font-bold text-[#5B0616]">Mr. Manmeet Raj</span>
            </p>
          </div>
        </section>

        {/* 9. Share Invitation Section */}
        <ShareInvitation />

        {/* Footer */}
        <footer className="text-center pt-8 pb-14 text-xs font-serif text-[#8A9A86]">
          <p className="tracking-widest uppercase text-[#5B0616] font-cinzel font-bold">
            MANSI &amp; RISAV • ENGAGEMENT CEREMONY
          </p>
          <p className="mt-1 font-sans text-[11px]">
            Sunday, 6th December, 2026 • Giraffe Resort, Raiganj, West Bengal
          </p>
          <p className="mt-2.5 text-xs sm:text-sm text-[#801323] font-serif italic font-semibold">
            Crafted with love &amp; joy for Mansi &amp; Risav — by bride&apos;s brother Mr. Manmeet Raj ❤️
          </p>
        </footer>
      </div>

      {/* Sticky Bottom Navigation Bar for Mobile & Quick Access */}
      <div className="fixed bottom-0 inset-x-0 z-40 bg-[#5B0616]/95 backdrop-blur-lg border-t-2 border-[#D4AF37] py-2 px-2 sm:px-4 shadow-[0_-10px_25px_rgba(0,0,0,0.3)]">
        <div className="max-w-xl mx-auto flex items-center justify-around gap-1 text-[10px] sm:text-xs font-cinzel font-bold text-[#F3E5AB]">
          {/* Button: Watch Video */}
          <button
            onClick={handleWatchVideo}
            className="flex flex-col items-center gap-1 hover:text-white transition-colors p-1"
          >
            <Film className="w-4 h-4 text-[#D4AF37]" />
            <span>Video</span>
          </button>

          {/* Button: View Venue */}
          <button
            onClick={handleViewVenue}
            className="flex flex-col items-center gap-1 hover:text-white transition-colors p-1"
          >
            <MapPin className="w-4 h-4 text-[#D4AF37]" />
            <span>Venue</span>
          </button>

          {/* Button: Add to Calendar */}
          <button
            onClick={() => generateEngagementICS()}
            className="flex flex-col items-center gap-1 hover:text-white transition-colors p-1"
          >
            <CalendarPlus className="w-4 h-4 text-[#D4AF37]" />
            <span>Calendar</span>
          </button>

          {/* Button: Download Video */}
          <a
            href="/video/mansi-risav-engagement.mp4"
            download="Mansi-Risav-Engagement-Invitation.mp4"
            className="flex flex-col items-center gap-1 hover:text-white transition-colors p-1"
          >
            <Download className="w-4 h-4 text-[#D4AF37]" />
            <span>Download</span>
          </a>

          {/* Button: Play Again */}
          <button
            onClick={handlePlayAgain}
            className="flex flex-col items-center gap-1 hover:text-white transition-colors p-1"
          >
            <RotateCcw className="w-4 h-4 text-[#D4AF37]" />
            <span>Envelope</span>
          </button>
        </div>
      </div>
    </main>
  );
}
