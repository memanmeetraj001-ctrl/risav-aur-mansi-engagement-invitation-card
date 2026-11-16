'use client';

import React, { useRef, useState } from 'react';
import { Film, Download, Play, Pause, Maximize } from 'lucide-react';

interface VideoPlayerSectionProps {
  onPlayModal?: () => void;
}

export default function VideoPlayerSection({ onPlayModal }: VideoPlayerSectionProps) {
  const videoRef = useRef<HTMLVideoElement | null>(null);
  const [isPlaying, setIsPlaying] = useState(false);

  const toggleVideoPlay = () => {
    if (!videoRef.current) return;
    if (isPlaying) {
      videoRef.current.pause();
      setIsPlaying(false);
    } else {
      videoRef.current.play();
      setIsPlaying(true);
    }
  };

  const handleFullscreen = () => {
    if (!videoRef.current) return;
    if (videoRef.current.requestFullscreen) {
      videoRef.current.requestFullscreen();
    }
  };

  return (
    <section id="video-invitation" className="px-3 sm:px-4 py-6 sm:py-8 max-w-4xl mx-auto">
      <div className="bg-[#FCFAF5] rounded-3xl p-5 sm:p-10 border-2 border-[#D4AF37] shadow-xl text-center">
        {/* Header Badge */}
        <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#5B0616] text-[#D4AF37] text-xs font-cinzel uppercase tracking-widest font-bold mb-3">
          <Film className="w-3.5 h-3.5" />
          <span>Cinematic 30s Invitation Film</span>
        </div>

        <h2 className="text-2xl sm:text-4xl font-cinzel-dec font-black text-[#5B0616] mb-2">
          Watch The Engagement Story
        </h2>

        <p className="text-xs sm:text-sm text-[#801323] font-serif max-w-xl mx-auto mb-6 px-2">
          A bespoke animated film celebrating the union of Mansi &amp; Risav, featuring their proposing story, blessings, and event details set to romantic music.
        </p>

        {/* Mobile-optimized Vertical 9:16 Video Player */}
        <div className="relative mx-auto w-full max-w-[280px] sm:max-w-xs md:max-w-sm rounded-[2rem] overflow-hidden border-4 border-[#D4AF37] shadow-[0_20px_45px_rgba(91,6,22,0.35)] bg-black aspect-[9/16]">
          <video
            ref={videoRef}
            src="/video/mansi-risav-engagement.mp4"
            className="w-full h-full object-cover"
            playsInline
            controls
            onPlay={() => setIsPlaying(true)}
            onPause={() => setIsPlaying(false)}
          />

          {/* Quick Play Overlay if not playing */}
          {!isPlaying && (
            <div
              onClick={toggleVideoPlay}
              className="absolute inset-0 bg-black/40 flex flex-col items-center justify-center cursor-pointer transition-opacity hover:bg-black/30"
            >
              <div className="w-14 h-14 sm:w-16 sm:h-16 rounded-full bg-[#D4AF37] text-[#5B0616] flex items-center justify-center shadow-2xl transform hover:scale-110 active:scale-95 transition-transform">
                <Play className="w-7 h-7 sm:w-8 sm:h-8 fill-current ml-1" />
              </div>
              <p className="mt-3 text-white font-cinzel text-xs sm:text-sm font-bold tracking-wider drop-shadow px-4 text-center">
                Tap to Watch 30s Film
              </p>
            </div>
          )}
        </div>

        {/* Video Controls & Download Action - Fully Responsive on Mobile */}
        <div className="mt-6 flex flex-col sm:flex-row items-center justify-center gap-3 max-w-md mx-auto">
          <div className="flex items-center justify-center gap-2 w-full sm:w-auto">
            <button
              onClick={toggleVideoPlay}
              className="flex-1 sm:flex-none inline-flex items-center justify-center gap-2 px-4 py-2.5 rounded-full bg-[#5B0616] text-[#D4AF37] border border-[#D4AF37] font-cinzel font-bold text-xs uppercase tracking-wider hover:bg-[#801323] transition-colors"
            >
              {isPlaying ? <Pause className="w-4 h-4" /> : <Play className="w-4 h-4 fill-current" />}
              <span>{isPlaying ? 'Pause Film' : 'Play Film'}</span>
            </button>

            <button
              onClick={handleFullscreen}
              className="inline-flex items-center justify-center gap-2 px-4 py-2.5 rounded-full bg-white text-[#5B0616] border border-[#D4AF37] font-cinzel font-bold text-xs uppercase tracking-wider hover:bg-[#F8F5EE] transition-colors"
            >
              <Maximize className="w-4 h-4" />
              <span>Full Screen</span>
            </button>
          </div>

          {/* PROMINENT DOWNLOAD VIDEO BUTTON */}
          <a
            href="/video/mansi-risav-engagement.mp4"
            download="Mansi-Risav-Engagement-Invitation.mp4"
            className="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-6 py-3 rounded-full bg-gradient-to-r from-[#D4AF37] via-[#F3E5AB] to-[#AA771C] text-[#5B0616] font-cinzel font-black text-xs uppercase tracking-wider shadow-[0_4px_15px_rgba(212,175,55,0.4)] hover:shadow-[0_6px_20px_rgba(212,175,55,0.6)] hover:scale-105 active:scale-95 transition-all text-center"
          >
            <Download className="w-4 h-4 text-[#5B0616]" />
            <span>DOWNLOAD VIDEO (MP4)</span>
          </a>
        </div>
      </div>
    </section>
  );
}
