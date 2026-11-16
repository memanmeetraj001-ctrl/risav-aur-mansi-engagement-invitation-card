import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  metadataBase: new URL('https://risav-aur-mansi-engagement-invitation-card.vercel.app'),
  title: 'Mansi ❤️ Risav — Engagement Invitation Ceremony | 6th Dec 2026',
  description:
    'With the blessings of Almighty & our beloved family, you are cordially invited to the auspicious Engagement Ceremony of Mansi & Risav on Sunday, 6th December, 2026 at Giraffe Resort, Raiganj.',
  keywords: [
    'Mansi and Risav Engagement',
    'Risav Gupta Engagement',
    'Mansi Suman Engagement',
    'Giraffe Resort Raiganj',
    'Indian Engagement Invitation',
    'Wedding Invitation Card',
  ],
  authors: [{ name: 'Mansi & Risav' }],
  openGraph: {
    title: 'Mansi ❤️ Risav — Engagement Invitation Ceremony',
    description:
      'We request your gracious presence at the auspicious Engagement celebrations of Mansi & Risav at Giraffe Resort, Raiganj.',
    url: 'https://risav-aur-mansi-engagement-invitation-card.vercel.app',
    siteName: 'Mansi & Risav Engagement',
    images: [
      {
        url: '/images/couple-proposal.jpg',
        width: 936,
        height: 1024,
        alt: 'Mansi and Risav Engagement Ceremony',
      },
    ],
    locale: 'en_IN',
    type: 'website',
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Mansi ❤️ Risav Engagement Invitation',
    description: 'Sunday, 6th December 2026 at Giraffe Resort, Raiganj.',
    images: ['/images/couple-proposal.jpg'],
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className="scroll-smooth">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
        <link rel="icon" href="/images/ganesha-gold.png" type="image/png" />
      </head>
      <body className="min-h-screen bg-[#F8F5EE] text-[#3B0612] antialiased selection:bg-[#D4AF37]/30 selection:text-[#5B0616]">
        {children}
      </body>
    </html>
  );
}
