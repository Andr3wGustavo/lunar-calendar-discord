# Astrological Lunar Matrix Bot

A hyper-precise, Python-based Discord Bot designed to bridge the gap between astronomical realities (the 3D Maya plane) and mystical, yogic, and astrological alignments. It functions as a daily cosmic calendar, feeding your Discord guild with exact calculations of the Moon's orbital phase, illumination, and spiritual geometry.

## 🌌 Core Features

- **Daily Lunar Drops**: Utilizes background tasks (`discord.ext.tasks`) to push automated, highly accurate lunar status updates to configured channels every day at 12:00 PM UTC.
- **Astronomical Precision Engine**: Powered by the `ephem` library to calculate:
  - Exact illumination percentage & phase.
  - Earth-to-Moon distance (Au & Km).
  - Sun-Moon angular separation.
  - Accurate Astrological placements (Tropical Zodiac Signs).
- **Vedic Yoga / Jyotish Integration**: Maps sidereal positions to the 27 Nakshatras (Lunar Mansions), pulling the exact energetic tone and meaning behind the current lunar placement.
- **Memory & Guild Tuning (`/painel`)**: An integrated SQLite registry (via `aiosqlite`) remembers your server's configuration, so the daily matrix signals are always routed to the right channel.

## 🛠️ Tech Stack & Architecture

- **Language:** Python 3.11+
- **API Wrapper:** `discord.py` (v2.x) with application slash commands (`app_commands`).
- **Database:** `aiosqlite` connected to an asynchronous SQLite local datastore (`lunar_db.sqlite`).
- **Astrodynamics:** `ephem` for pure, orbital mechanics-grade calculations out in space.
- **Bootstrapper:** Standalone `.bat` launch sequence ensuring an automated, hands-off virtual environment orchestration.

## 🚀 Installation & Deployment

1. Clone or clone this repository to your local server machine.
2. Ensure you have `Python 3.11+` installed and registered in your system PATH.
3. Rename the `.env.example` file to `.env` and paste your Discord bot token inside:
   ```ini
   DISCORD_TOKEN=your_secure_discord_token_here
   ```
4. Simply double-click the `start.bat` script.
   *The script will autonomously architect a Python virtual environment, pull down the required dependencies (`discord.py`, `ephem`, `aiosqlite`), establish a local database, and mount the bot.*

## ⚙️ Commands

- `/painel [channel]` : Guild Admins only. Binds the daily lunar drop to a specific text channel. If no channel is passed, it uses the channel where the command was executed.
- `/moon` : Instantly pulls the up-to-the-second planetary matrix calculation for the Moon and renders it locally in the chat.

## 🔮 Maya Plane Concept

This system operates under the notion that the physical 3D world (Maya) is structurally aligned with the harmonic frequencies of celestial bodies. By consistently tracking the Moon—the closest and most potent electromagnetic oscillator relative to Earthly life—users are aligned with the true rhythms of creation, beyond standard Gregorian chronometry.

---
*Created by a genius dev with one eye on the screen and one eye on the stars.*
