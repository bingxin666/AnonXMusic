import asyncio
import os
import re
from typing import Union

import yt_dlp

class BilibiliAPI:
    def __init__(self):
        self.regex = r"(?:bilibili\.com|b23\.tv)"

    async def exists(self, link: str, videoid: Union[bool, str] = None):
        if re.search(self.regex, link):
            return True
        return False

    async def details(self, link: str, videoid: Union[bool, str] = None):
        # 模仿 YouTube 中的获取方式，简单演示
        # ...existing code...
        ydl_opts = {"quiet": True}
        ydl = yt_dlp.YoutubeDL(ydl_opts)
        with ydl:
            info = ydl.extract_info(link, download=False)
        title = info.get("title", "Unknown Title")
        duration_sec = info.get("duration", 0)
        thumbnail = info.get("thumbnail", "")
        vidid = info.get("id", "")
        # ...existing code...
        return title, duration_sec, thumbnail, vidid

    async def download(
        self,
        link: str,
        mystic,
        video: Union[bool, str] = None,
        format_id: Union[bool, str] = None,
        title: Union[bool, str] = None,
    ) -> str:
        # 模仿 YouTube 中的下载方式
        # ...existing code...
        loop = asyncio.get_running_loop()

        def run_dl():
            ydl_optssx = {
                "format": format_id if format_id else "bv*+ba/best",
                "outtmpl": "downloads/%(id)s.%(ext)s",
                "quiet": True,
                "no_warnings": True,
            }
            x = yt_dlp.YoutubeDL(ydl_optssx)
            info = x.extract_info(link, False)
            path = os.path.join("downloads", f"{info['id']}.{info['ext']}")
            if not os.path.exists(path):
                x.download([link])
            return path

        downloaded_file = await loop.run_in_executor(None, run_dl)
        # ...existing code...
        return downloaded_file