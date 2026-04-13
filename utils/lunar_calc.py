import ephem
from datetime import datetime, timezone
import math

class LunarCalculator:
    def __init__(self):
        self.moon = ephem.Moon()
        self.sun = ephem.Sun()
        # Nakshatras (Lunar Mansions in Vedic Astrology) 13°20' each
        self.nakshatras = [
            "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira", "Ardra", 
            "Punarvasu", "Pushya", "Ashlesha", "Magha", "Purva Phalguni", 
            "Uttara Phalguni", "Hasta", "Chitra", "Swati", "Vishakha", 
            "Anuradha", "Jyeshtha", "Mula", "Purva Ashadha", "Uttara Ashadha", 
            "Shravana", "Dhanishta", "Shatabhisha", "Purva Bhadrapada", 
            "Uttara Bhadrapada", "Revati"
        ]
        
        self.nakshatra_meanings = {
            "Ashwini": "Speed, initiating action, healing energy.",
            "Bharani": "Transformation, bearing life, creative fire.",
            "Krittika": "Purification, cutting through illusions, determination.",
            "Rohini": "Growth, fertility, earthly desires, sensuality.",
            "Mrigashira": "Seeking, curiosity, exploring the mind.",
            "Ardra": "Storms, tears, intense emotional clearing, Shiva's destructive aspect.",
            "Punarvasu": "Return of the light, renewal, infinite potential.",
            "Pushya": "Nourishment, spiritual devotion, auspiciousness.",
            "Ashlesha": "Mysticism, kundalini serpent energy, embracing shadows.",
            "Magha": "Ancestral roots, royal authority, legacy.",
            "Purva Phalguni": "Relaxation, charm, creative bliss.",
            "Uttara Phalguni": "Patronage, vows, material success through alliance.",
            "Hasta": "Skillful hands, manifestation, mastery of details.",
            "Chitra": "Creating magic, divine architecture, striking beauty.",
            "Swati": "Independence, surviving the storm, breathing space (Prana).",
            "Vishakha": "Purpose, conquering obstacles, triumph.",
            "Anuradha": "Devotion to the divine, friendship, subtle exploration.",
            "Jyeshtha": "Eldest, leadership, facing mental battles.",
            "Mula": "Root, untying karmic knots, deep investigation.",
            "Purva Ashadha": "Invincible spirit, purification by water.",
            "Uttara Ashadha": "Universal victory, enduring strength.",
            "Shravana": "Listening to the cosmic sound (Aum), learning.",
            "Dhanishta": "Rhythm, abundance, musical alignment with spheres.",
            "Shatabhisha": "100 healers, cosmic medicine, veil of illusion (Maya).",
            "Purva Bhadrapada": "Fire dragon, ascending the spiritual ladder, penance.",
            "Uttara Bhadrapada": "Deep wisdom, foundation, balancing the cosmic waters.",
            "Revati": "Final journey, nourishment, dissolving into the infinite."
        }

        self.zodiac_signs = [
            "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
            "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
        ]

    def _is_retrograde(self, planet, date_obj):
        p1 = planet
        p2 = type(planet)()  # Create a fresh copy
        
        # Current position
        p1.compute(ephem.date(date_obj))
        lon1 = ephem.Ecliptic(p1).lon
        
        # Future position (0.1 days ahead)
        future_date = ephem.Date(ephem.date(date_obj) + 0.1)
        p2.compute(future_date)
        lon2 = ephem.Ecliptic(p2).lon
        
        # Difference in degrees
        diff = math.degrees(lon2 - lon1)
        if diff < -180: diff += 360
        elif diff > 180: diff -= 360
        
        return diff < 0  # Retrograde if apparent motion is backwards

    def get_lunar_data(self, date=None):
        if date is None:
            date = datetime.now(timezone.utc)
            
        observer = ephem.Observer()
        observer.date = ephem.date(date)
        
        self.moon.compute(observer)
        self.sun.compute(observer)

        # Retrograde Check for major planets affecting Earthly Maya
        planets_to_check = {
            "Mercury": ephem.Mercury(),
            "Venus": ephem.Venus(),
            "Mars": ephem.Mars(),
            "Jupiter": ephem.Jupiter(),
            "Saturn": ephem.Saturn()
        }
        retrogrades = []
        for name, p_obj in planets_to_check.items():
            if self._is_retrograde(p_obj, observer.date):
                retrogrades.append(name)
        
        retrograde_alert = None
        if retrogrades:
            pl_str = ", ".join(retrogrades)
            retrograde_alert = f"🔮 **RETROGRADE ACTIVE:** [{pl_str}] are traversing backwards in the Maya 3D plane. Re-evaluate, reflect, and avoid rushing in these domains."
        
        # Calculate Phase (0 to 1)
        phase = self.moon.phase / 100.0  # Percentage of illumination

        # Ecliptic longitude
        moon_lon = ephem.Ecliptic(self.moon).lon
        moon_lon_deg = math.degrees(moon_lon)
        if moon_lon_deg < 0:
            moon_lon_deg += 360

        # Tropical Zodiac Sign (0-30 Aries, etc.)
        sign_index = int(moon_lon_deg / 30)
        zodiac_sign = self.zodiac_signs[sign_index]

        # Vedic Astrology (Sidereal) approximation
        # Ayanamsa (precession of the equinoxes) is roughly 24 degrees currently.
        ayanamsa = 24.1
        sidereal_lon_deg = (moon_lon_deg - ayanamsa) % 360
        
        # Current Nakshatra (13 degrees 20 minutes = 13.333... degrees)
        nakshatra_index = int(sidereal_lon_deg / (360 / 27))
        nakshatra_name = self.nakshatras[nakshatra_index]

        # Determine Moon waxing/waning via solar angular separation
        sun_lon_deg = math.degrees(ephem.Ecliptic(self.sun).lon)
        if sun_lon_deg < 0: sun_lon_deg += 360
        
        angle_diff = (moon_lon_deg - sun_lon_deg) % 360
        is_waxing = angle_diff < 180

        # Phase Names
        if angle_diff < 12: phase_name = "New Moon"
        elif angle_diff < 90: phase_name = "Waxing Crescent"
        elif angle_diff < 105: phase_name = "First Quarter"
        elif angle_diff < 168: phase_name = "Waxing Gibbous"
        elif angle_diff < 192: phase_name = "Full Moon"
        elif angle_diff < 270: phase_name = "Waning Gibbous"
        elif angle_diff < 285: phase_name = "Last Quarter"
        elif angle_diff < 348: phase_name = "Waning Crescent"
        else: phase_name = "New Moon"

        # Vedic Tithi Calculation (Each Tithi is exactly 12 degrees of Moon-Sun phase difference)
        tithi_number = int((angle_diff % 360) / 12) + 1
        paksha = "Shukla Paksha (Waxing Bright)" if is_waxing else "Krishna Paksha (Waning Dark)"
        tithi_name = f"Tithi {tithi_number}"
        
        # Ekadashi check (11th Tithi is spiritually critical for fasting and meditation in yogic lore)
        tithi_event = None
        if tithi_number == 11 or tithi_number == 26:
            tithi_event = "⚠️ **EKADASHI ACTIVATED:** Extremely potent window for spiritual fasting and deep meditation."
        elif tithi_number == 15:
            tithi_event = "🌕 **PURNIMA ACTIVATED:** Peak illumination. Emotional tides are highest. Celebrate and manifest."
        elif tithi_number == 30:
            tithi_event = "🌑 **AMAVASYA ACTIVATED:** Absolute dark moon. Powerful for ancestral healing and quiet introspection."

        # Rahu / Ketu (Lunar Nodes & Eclipse Detection)
        # In the Maya 3D plane, an eclipse happens when Moon's ecliptic latitude is close to 0 at New/Full moons.
        moon_ecl_lat = math.degrees(ephem.Ecliptic(self.moon).lat)
        eclipse_alert = None
        if abs(moon_ecl_lat) < 1.5:
            if tithi_number == 15:
                eclipse_alert = "🔴 **LUNAR ECLIPSE ORB (RAHU/KETU AXIS):** The Moon is crossing the nodes during Purnima. Intense karmic clearing and emotional shadow work."
            elif tithi_number == 30 or tithi_number == 1:
                eclipse_alert = "🌑 **SOLAR ECLIPSE ORB (RAHU/KETU AXIS):** The New Moon aligns perfectly to obscure the Sun. Massive reality shifts and fated resets."
            else:
                eclipse_alert = "🌀 **NODAL ALIGNMENT:** The Moon is crossing the Ecliptic plane today (Entering Rahu/Ketu Domain). Fated encounters and timeline shifting."

        return {
            "date": date.strftime("%Y-%m-%d %H:%M:%S UTC"),
            "illumination": round(phase * 100, 2),
            "phase_name": phase_name,
            "is_waxing": is_waxing,
            "zodiac_sign": zodiac_sign,
            "nakshatra": nakshatra_name,
            "spiritual_message": self.nakshatra_meanings[nakshatra_name],
            "distance_au": self.moon.earth_distance,
            "distance_km": round(self.moon.earth_distance * 149597870.7, 2),
            "angle_diff": round(angle_diff, 2),
            "tithi_number": tithi_number,
            "tithi_paksha": paksha,
            "tithi_event": tithi_event,
            "eclipse_alert": eclipse_alert,
            "retrograde_alert": retrograde_alert
        }

lunar_calc = LunarCalculator()
