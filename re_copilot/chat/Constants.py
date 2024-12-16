import uuid

HEADERS = {
    "accept": "application/json",
    "accept-language": "en;q=0.9,en-US;q=0.8",
    "accept-encoding": "gzip, deflate, br, zsdch",
    "content-type": "application/json",
    "sec-ch-ua": '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    "sec-ch-ua-arch": '"x86"',
    "sec-ch-ua-bitness": '"64"',
    "sec-ch-ua-full-version": '"131.0.2903.86"',
    "sec-ch-ua-full-version-list": '"Microsoft Edge";v="131.0.2903.86", "Not=A?Brand";v="8.0.0.0", "Chromium";v="129.0.6668.71"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": '"Windows"',
    "sec-ch-ua-platform-version": '"15.0.0"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sec-ms-gec-version": "1-131.0.2903.86",
    "x-ms-client-request-id": str(uuid.uuid4()),
    "x-ms-useragent": "azsdk-js-api-client-factory/1.0.0-beta.1 core-rest-pipeline/1.16.0 OS/Windows",
    "Referer": "https://www.bing.com/search?form=NTPCHB&q=Bing+AI&showconv=1",
    "Referrer-Policy": "origin-when-cross-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
}
DELIMITER = "\x1e"