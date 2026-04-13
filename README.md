<div align="center">
  <h1>🌌 Discord Lunar Matrix Engine</h1>
  <p><i>A Hyper-Precise Astronomical and Yogic Discord Bot</i></p>
  <p>Bridging the gap between the 3D Maya physical plane and ancient yogic and astrological matrices.</p>
</div>

---

## 📜 Overview

The **Discord Lunar Matrix Engine** is a cutting-edge bot that acts as a true celestial chronometer. Instead of tracking arbitrary Gregorian calendar dates, it aligns your community with the universal rhythm of nature: **The Lunar Cycle**. 

Built with the mentality of both a genius software architect and a mystic yogi, this system utilizes high-level orbital calculation libraries (like NASA-grade `ephem`) combined with ancient Ayurvedic and Jyotish principles (Vedic Astrological Mathematics). It tracks the physical movement of the Moon within the 3D Maya plane and translates its frequencies to spiritual, psychological, and cosmic insights for your Discord guild.

---

## ✨ Features

### 🔭 1. Astronomical Precision API Engine
Driven by the Python `ephem` library, the bot calculates orbital mechanics exactly exactly relative to the Earth:
- **Phase & Illumination**: Down to the exact percentage of the Moon's visible light (e.g., Waxing Crescent at 47.3%).
- **Earth-to-Moon Distance**: Tracks apogee and perigee in both Astronomical Units (AU) and Kilometers, giving a measure of physical "gravitational pull" intensity.
- **Sun-Moon Angular Separation**: Real-time phase shifting and ecliptic intersection mathematics.

### 🧘‍♂️ 2. The Mystic Yogi Matrix (Jyotish / Nakshatras)
Calculates the Moon's sidereal position to deliver ancient Vedic psychological algorithms:
- **Tropical Zodiac Position**: Understand the current western archetypal resonance.
- **Vedic Tithis (Lunar Days)**: Divides the cycle into 30 specific days. Automatically triggers high-voltage **Ekadashi**, **Purnima**, and **Amavasya** alerts.
- **The 27 Nakshatras (Lunar Mansions)**: The most profound yogic system of tracking the Moon's subtle emotional influence. Each mansion carries unique energy (e.g., *Ashwini* for healing, *Ardra* for emotional destruction, *Pushya* for nourishment).
- **Spiritual Alignment Messages**: Every drop translates the cosmic weather into actionable inner-wisdom.

### 💾 3. Asynchrony & SQLite Memory Persistence
- Equipped with `aiosqlite`, the bot maintains a flawless, corrupted-free asynchronous local database.
- Easily manages hundreds of guild configs concurrently. No thread blocking, no latency.

### ⚙️ 4. Plug-and-Play Server Dashboard (`/painel`)
Zero tedious commands. Server administrators utilize Discord Slash Commands to map dropping coordinates:
- `/painel [#channel]`: Sets exactly where the Lunar Engine should broadcast its daily updates.

### 📡 5. Automated Daily Matrix Delivery
A background loop (Task) automatically awakens every day precisely at `12:00 PM UTC` to broadcast a detailed embed containing the status of the Maya 3D plane directly into your chosen guild channel.

### 🌙 6. Eclipse Detection (Rahu & Ketu Axes)
- Integrates node calculation to detect when the Moon approaches the Ecliptic latitude orbital 0° during syzygy. 
- Fires **Solar** and **Lunar** Eclipse ORB alerts precisely when the Moon gets swallowed by the karmic nodes (Rahu & Ketu).

### 🔮 7. Instant Oracle Query (`/moon` & `/nakshatra`)
- `/moon`: An instant snapshot of the celestial orbit sent immediately to chat.
- `/nakshatra [name]`: A mystical encyclopedia built-in. Type any of the 27 lunar mansions and receive its ancient blueprint.

---

## 🚀 Deployment & Installation

The engineering emphasizes "zero-friction" deployment. You do not need to understand Python to run this server.

1. **Clone the Repository:** Download the project files.
2. **Environment Variables:** Rename `.env.example` to `.env`. Insert your Discord Bot Token:
   ```ini
   DISCORD_TOKEN=your_secure_discord_token_here
   ```
3. **Execute the Ignition Script:** Run the `start.bat` file.
   *The batch orchestration script will autonomously:*
   - Provision an isolated Python Virtual Environment (`venv`).
   - Pip-install all dependencies (`discord.py`, `ephem`, `aiosqlite`, `python-dotenv`).
   - Mount the asynchronous loop and login to Discord.

---

## 🔮 Future Roadmap & Suggested Enhancements

Even a perfect system can evolve. Here are highly recommended implementations to expand this matrix:

1. **User Natal Chart Integrations (Personal Astrological Hooks)**
   - Allow users to register their birth date/time/location.
   - The bot evaluates *Chandra Ashtama* (Moon transit over 8th house) or their *Lunar Return*, sending DMs to warn about high-stress days or high-manifestation periods.

2. **Retrograde Planet Detectors**
   - Implement astronomical triggers when major planets (Mercury, Saturn, etc.) shift orbital direction relative to Earth, sending collective energetic warnings.

3. **Visual NASA Image Embedding**
   - Hook into a planetary API to generate and send visually accurate depictions (or topological maps) of the Moon's current state on the daily drop embed.
   
4. **Dynamic Timezone Scaling**
   - Extend the SQLite schema to allow guilds to configure their specific timezone, delivering the daily lunar report exactly at Noon (or midnight) local time, instead of just universal UTC.

---
<div align="center">
  <i>"As above, so below. Decoding the Maya 3D plane line by line."</i><br>
  <b>Constructed flawlessly.</b>
</div>
