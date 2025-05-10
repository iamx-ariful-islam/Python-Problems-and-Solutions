# pip install aiofiles

import os
import time
import asyncio
import aiofiles


async def clean_up(folder_path, days_old):
    now = time.time()
    cutoff_time = now - (days_old * 86400)
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.getmtime(file_path) < cutoff_time:
            await aiofiles.os.remove(file_path)
            print(f"Deleted {filename}")


folder_path = '/path/to/your/folder'
asyncio.run(clean_up(folder_path, 30))