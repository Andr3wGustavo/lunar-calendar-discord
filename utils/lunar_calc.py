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

    def get_lunar_data(self, date=None):
        if date is None:
            date = datetime.now(timezone.utc)
            
        observer = ephem.Observer()
        observer.date = ephem.date(date)
        
        self.moon.compute(observer)
        self.sun.compute(observer)
        
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
            "angle_diff": round(angle_diff, 2)
        }

lunar_calc = LunarCalculator()
