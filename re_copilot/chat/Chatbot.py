import asyncio
import json
from pathlib import Path

import aiohttp
import httpx
import requests

from re_copilot.chat.Constants import HEADERS, DELIMITER


def append_identifier(msg: dict) -> str:
    # Convert dict to json string
    return json.dumps(msg, ensure_ascii=False) + DELIMITER


async def _initial_handshake(wss) -> None:
    await wss.send_json({
        "event": "setOptions",
        "ads": {
            "supportedTypes": ["text", "propertyPromotion", "tourActivity", "product", "multimedia"]
        }})


async def chat(jwt_token: str, cookies: list[dict], chat_text: str, reset_conversation: bool = False):
    wss_link = f"wss://copilot.microsoft.com/c/api/chat?api-version=2&accessToken={jwt_token}&dpwa=1"
    aio_session = aiohttp.ClientSession()
    wss = await aio_session.ws_connect(wss_link)
    await _initial_handshake(wss)
    headers = {"Authorization": f"Bearer {jwt_token}"}
    start_data = requests.post(url="https://copilot.microsoft.com/c/api/start?dpwa=1", headers=headers)
    if start_data.json()["currentConversationId"] is not None and not reset_conversation:
        conversation_data = start_data.json()["currentConversationId"]
        conversation_id = conversation_data
    else:
        conversation_data = requests.post(url="https://copilot.microsoft.com/c/api/conversations?dpwa=1", headers=headers)
        conversation_id = conversation_data.json()["id"]
    transport = httpx.AsyncHTTPTransport(retries=900)
    formatted_cookies = None
    if cookies:
        formatted_cookies = httpx.Cookies()
        for cookie in cookies:
            formatted_cookies.set(cookie["name"], cookie["value"])
    async with httpx.AsyncClient(
            timeout=30,
            headers=HEADERS,
            transport=transport,
            cookies=formatted_cookies,
    ) as client:
        response = await client.post("https://copilot.microsoft.com/cl/eus2/collect", json=json.loads(
            """{"e":["0.7.58",2,117,2227,"n59ae4ieqq","1rj2obg","12rmrha",1,1,1],"a":[[1817,12,39,55,510],
            [1825,12,39,68,525],[1835,12,39,81,540],[1844,12,39,93,555],[1845,12,45,94,556],[1854,12,45,105,570],
            [1863,12,45,116,584],[1864,12,61,118,586],[1865,12,61,119,587],[1866,12,51,121,588],[1876,12,51,134,602],
            [1885,12,51,148,616],[1897,12,51,163,628],[1903,12,51,170,633],[1904,12,81,171,634],[1922,12,81,188,644],
            [1924,12,81,190,645],[1925,12,113,191,646],[1945,12,113,207,651],[1946,12,92,208,651],[1947,12,92,209,651],
            [1949,12,114,210,652],[1972,12,114,225,652],[1993,12,114,235,650],[2017,12,114,241,650],
            [2025,12,114,245,650],[2027,12,92,247,650],[2029,12,92,248,651],[2030,12,81,249,651],[2036,12,81,255,652],
            [2037,12,147,256,652],[2039,12,147,258,652],[2039,12,148,259,653],[2047,12,148,269,656],
            [2048,12,151,272,656],[2059,12,151,290,660],[2069,12,151,309,663],[2079,12,151,328,667],
            [2090,12,151,347,669],[2103,12,151,366,669],[2121,12,151,385,669],[2143,12,151,396,667],
            [2167,12,151,399,665],[2245,13,151,399,665],[2253,12,151,401,665],[2265,12,151,402,665],
            [2340,14,151,402,665],[2340,9,151,402,665,7099,15123,0,0,0,null,null,"r7f6em84.r7f6em84",1],
            [117,4,1,1065,730,1065,730,0,0,0,0,0,0],[2343,1,4,
            ["graph.microsoft.com","browser.events.data.microsoft.com","eu-mobile.events.data.microsoft.com"]],
            [2344,0,2,740,3,3,4,13,5,5,25,54],[2344,36,6,[549,6,2253,0]]]}"""))
        while response.status_code != 200:
            response = await client.post("https://copilot.microsoft.com/cl/eus2/collect", json=json.loads(
                """{"e":["0.7.58",2,117,2227,"n59ae4ieqq","1rj2obg","12rmrha",1,1,1],"a":[[1817,12,39,55,510],
                [1825,12,39,68,525],[1835,12,39,81,540],[1844,12,39,93,555],[1845,12,45,94,556],[1854,12,45,105,570]
                ,[1863,12,45,116,584],[1864,12,61,118,586],[1865,12,61,119,587],[1866,12,51,121,588],
                [1876,12,51,134,602],[1885,12,51,148,616],[1897,12,51,163,628],[1903,12,51,170,633],
                [1904,12,81,171,634],[1922,12,81,188,644],[1924,12,81,190,645],[1925,12,113,191,646],
                [1945,12,113,207,651],[1946,12,92,208,651],[1947,12,92,209,651],[1949,12,114,210,652],
                [1972,12,114,225,652],[1993,12,114,235,650],[2017,12,114,241,650],[2025,12,114,245,650],
                [2027,12,92,247,650],[2029,12,92,248,651],[2030,12,81,249,651],[2036,12,81,255,652],
                [2037,12,147,256,652],[2039,12,147,258,652],[2039,12,148,259,653],[2047,12,148,269,656],
                [2048,12,151,272,656],[2059,12,151,290,660],[2069,12,151,309,663],[2079,12,151,328,667],
                [2090,12,151,347,669],[2103,12,151,366,669],[2121,12,151,385,669],[2143,12,151,396,667],
                [2167,12,151,399,665],[2245,13,151,399,665],[2253,12,151,401,665],[2265,12,151,402,665],
                [2340,14,151,402,665],[2340,9,151,402,665,7099,15123,0,0,0,null,null,"r7f6em84.r7f6em84",1],
                [117,4,1,1065,730,1065,730,0,0,0,0,0,0],[2343,1,4,
                ["graph.microsoft.com","browser.events.data.microsoft.com","eu-mobile.events.data.microsoft.com"]],
                [2344,0,2,740,3,3,4,13,5,5,25,54],[2344,36,6,[549,6,2253,0]]]}"""))
        token_text = response.text
        token_text = token_text.replace("SIGNAL ", "")
        token_text = json.loads(token_text)
        token_text = json.loads(token_text)
        token_text = token_text[0]["value"]
    await wss.send_json({
        "event": "challengeResponse",
        "method": "clarity",
        "token": f"{token_text}"
    })
    await wss.send_json({
        "event": "send",
        "conversationId": f"{conversation_id}",
        "content": [{"type": "text", "text": f"{chat_text}"}],
        "mode": "chat"})
    total_text = ""
    while not wss.closed:
        message = await wss.receive_str()
        message_json: dict = json.loads(message)
        if message_json.get("text", None) is not None:
            total_text += message_json["text"]
        elif message_json.get("text", None) is None and message_json.get("event", None) == "done":
            await wss.close()
            await aio_session.close()
            break
        else:
            continue

    return total_text
