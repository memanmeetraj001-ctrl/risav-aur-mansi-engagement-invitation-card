/**
 * Generates an iCalendar (.ics) file content and triggers download
 * for Mansi & Risav Engagement Ceremony.
 * Date: Sunday, 6 December 2026 at 6:00 PM
 * Venue: Giraffe Resort, Raiganj, West Bengal
 */

export function generateEngagementICS(): void {
  // 6 December 2026, 6:00 PM (18:00) IST
  // Format: YYYYMMDDTHHMMSS
  const startDate = "20261206T180000";
  const title = "Mansi & Risav Engagement";
  const description =
    "With the blessings of Almighty & our beloved family, you are cordially invited to the auspicious Engagement Ceremony of Mansi & Risav.\\n\\nVenue: Giraffe Resort, Raiganj, West Bengal\\nGoogle Maps: https://share.google/ltWlyblaDHHqS4iHx";
  const location =
    "Giraffe Resort, Khalsi - Khoksa Road, Mirual, Raiganj, Uttar Dinajpur, West Bengal – 733130";
  const url = "https://share.google/ltWlyblaDHHqS4iHx";
  const now = new Date()
    .toISOString()
    .replace(/[-:]/g, "")
    .replace(/\.\d{3}/, "");

  const icsLines = [
    "BEGIN:VCALENDAR",
    "VERSION:2.0",
    "PRODID:-//Mansi & Risav//Engagement Invitation//EN",
    "CALSCALE:GREGORIAN",
    "METHOD:PUBLISH",
    "BEGIN:VEVENT",
    `UID:engagement-mansi-risav-20261206@weddinginvite`,
    `DTSTAMP:${now}`,
    `DTSTART:${startDate}`,
    `SUMMARY:${title}`,
    `DESCRIPTION:${description}`,
    `LOCATION:${location}`,
    `URL:${url}`,
    "STATUS:CONFIRMED",
    "TRANSP:OPAQUE",
    "BEGIN:VALARM",
    "TRIGGER:-PT24H",
    "ACTION:DISPLAY",
    "DESCRIPTION:Reminder: Mansi & Risav Engagement Ceremony Tomorrow!",
    "END:VALARM",
    "END:VEVENT",
    "END:VCALENDAR",
  ];

  const icsContent = icsLines.join("\r\n");
  const blob = new Blob([icsContent], { type: "text/calendar;charset=utf-8" });
  const downloadUrl = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = downloadUrl;
  a.download = "Mansi-Risav-Engagement-6Dec2026.ics";
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(downloadUrl);
}
