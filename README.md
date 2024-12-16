# Setup

<summary>

<details open>

## Install package

```bash
python3 -m pip install re_copilot --upgrade
```
## Requirements

- python 3.9+
- A Microsoft Account with access to <https://bing.com/chat> (Optional, depending on your region)
- Required in a supported country or region with New Bing (Chinese mainland VPN required)

</details>
</summary>

## Authentication

<details open>

### Collect cookies

- a) (Easy) Install the latest version of Microsoft Edge
- b) (Advanced) Alternatively, you can use any browser and set the user-agent to look like you're using Edge (e.g., `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.51`). You can do this easily with an extension like "User-Agent Switcher and Manager" for [Chrome](https://chrome.google.com/webstore/detail/user-agent-switcher-and-m/bhchdcejhohfmigjafbampogmaanbfkg) and [Firefox](https://addons.mozilla.org/en-US/firefox/addon/user-agent-string-switcher/).

1. Get a browser that looks like Microsoft Edge.
2. Open [bing.com/chat](https://copilot.microsoft.com/chats)
3. If you see a chat feature, you are good to continue...
4. Install the cookie editor extension for [Chrome](https://chrome.google.com/webstore/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm) or [Firefox](https://addons.mozilla.org/en-US/firefox/addon/cookie-editor/)
5. Go to [bing.com/chat](https://copilot.microsoft.com/chats)
6. Open the extension
7. Click "Export" on the bottom right, then "Export as JSON" (This saves your cookies to clipboard)
8. Paste your cookies into a file `bing_cookies.json`.
   - NOTE: The **cookies file name MUST follow the regex pattern `bing_cookies.json`**, so that they could be recognized by internal cookie processing mechanisms

### Collect JWT Token

1. Open Edge (make sure you already enable developer tools)
2. Go to [bing.com/chat](https://copilot.microsoft.com/chats
3. Press F12 to open developer tools
4. Switch to network tab
5. Press Ctrl + F on developer tool window to search
6. Search authorization and find request header that include authorization
![Requests header that include authorization](/images/request_that_include_jwt.png)
7. Copy all JWT token string after Bearer 
![JWT Token](/images/jwt_token.png)

</details>

## Example

<details open>

```python
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
```

</details>
