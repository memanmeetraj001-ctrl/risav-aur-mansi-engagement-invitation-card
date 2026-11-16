'use client';

import React, { useState, useEffect, useRef } from 'react';
import { Volume2, VolumeX, Music, Play, Pause } from 'lucide-react';

interface MusicPlayerProps {
  autoPlayTrigger?: boolean;
}

export default function MusicPlayer({ autoPlayTrigger }: MusicPlayerProps) {
  const audioRef = useRef<HTMLAudioElement | null>(null);
  const [isPlaying, setIsPlaying] = useState(false);
  const [isMuted, setIsMuted] = useState(false);
  const [hasInteracted, setHasInteracted] = useState(false);

  useEffect(() => {
    if (audioRef.current) {
      audioRef.current.volume = 0.75;
    }
  }, []);

  useEffect(() => {
    if (autoPlayTrigger && !hasInteracted && audioRef.current) {
      audioRef.current
        .play()
        .then(() => {
          setIsPlaying(true);
          setHasInteracted(true);
        })
        .catch((err) => {
          console.log('Autoplay deferred until explicit click:', err);
        });
    }
  }, [autoPlayTrigger, hasInteracted]);

  const togglePlay = () => {
    if (!audioRef.current) return;
    if (isPlaying) {
      audioRef.current.pause();
      setIsPlaying(false);
    } else {
      audioRef.current
        .play()
        .then(() => {
          setIsPlaying(true);
          setHasInteracted(true);
        })
        .catch((e) => console.log('Playback error:', e));
    }
  };

  const toggleMute = () => {
    if (!audioRef.current) return;
    audioRef.current.muted = !isMuted;
    setIsMuted(!isMuted);
  };

  return (
    <>
      <audio
        ref={audioRef}
        src="/audio/mansi-risav-engagement-song.mp3"
        loop
        preload="auto"
      />

      {/* Floating Music Control Badge */}
      <div className="fixed bottom-24 right-4 sm:bottom-6 sm:right-6 z-50 flex items-center gap-2 bg-[#5B0616]/90 backdrop-blur-md text-[#D4AF37] px-3.5 py-2.5 rounded-full border border-[#D4AF37]/50 shadow-2xl transition-all duration-300 hover:scale-105">
        <button
          onClick={togglePlay}
          className="flex items-center gap-2 text-xs font-serif font-semibold tracking-wide uppercase focus:outline-none"
          title={isPlaying ? 'Pause Music' : 'Play Music'}
        >
          <div
            className={`w-7 h-7 rounded-full bg-[#D4AF37] text-[#5B0616] flex items-center justify-center transition-transform ${
              isPlaying ? 'animate-spin' : ''
            }`}
            style={{ animationDuration: '6s' }}
          >
            <Music className="w-4 h-4" />
          </div>
          <span className="hidden sm:inline">
            {isPlaying ? 'Music Playing' : 'Play Song'}
          </span>
          {isPlaying ? (
            <Pause className="w-4 h-4 text-[#D4AF37]" />
          ) : (
            <Play className="w-4 h-4 text-[#D4AF37] fill-current" />
          )}
        </button>

        <div className="h-4 w-[1px] bg-[#D4AF37]/30" />

        <button
          onClick={toggleMute}
          className="text-[#D4AF37] hover:text-white transition-colors focus:outline-none p-1"
          title={isMuted ? 'Unmute' : 'Mute'}
        >
          {isMuted ? (
            <VolumeX className="w-4 h-4" />
          ) : (
            <Volume2 className="w-4 h-4" />
          )}
        </button>
      </div>
    </>
  );
}
