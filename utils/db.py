import aiosqlite
import os

DB_PATH = 'lunar_db.sqlite'

async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS guild_settings (
                guild_id INTEGER PRIMARY KEY,
                channel_id INTEGER,
                timezone TEXT DEFAULT 'UTC',
                language TEXT DEFAULT 'en'
            )
        ''')
        await db.commit()

async def get_guild_channel(guild_id: int):
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute('SELECT channel_id FROM guild_settings WHERE guild_id = ?', (guild_id,)) as cursor:
            row = await cursor.fetchone()
            if row:
                return row[0]
            return None

async def set_guild_channel(guild_id: int, channel_id: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute('''
            INSERT INTO guild_settings (guild_id, channel_id) 
            VALUES (?, ?)
            ON CONFLICT(guild_id) DO UPDATE SET channel_id = excluded.channel_id
        ''', (guild_id, channel_id))
        await db.commit()

async def get_all_guilds():
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute('SELECT guild_id, channel_id FROM guild_settings WHERE channel_id IS NOT NULL') as cursor:
            return await cursor.fetchall()
