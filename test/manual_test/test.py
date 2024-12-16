import asyncio
import json
from pathlib import Path

from re_copilot import chat


async def main(jwt_token: str, cookies: list[dict], chat_text: str, reset_conversation: bool):
    bot_response = await chat(jwt_token=jwt_token, cookies=cookies, chat_text=chat_text,
                              reset_conversation=reset_conversation)
    print(bot_response)


if __name__ == "__main__":
    your_jwt_token = ""
    jwt_token = f"{your_jwt_token}"
    cookies: list[dict] = json.loads(open(
        str(Path(str(Path.cwd()) + "/bing_cookies.json")), encoding="utf-8").read())
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.get_event_loop()
    loop.run_until_complete(
        main(jwt_token=jwt_token, cookies=cookies, chat_text="Introduction yourself", reset_conversation=True))
