import httpx


def get_ip() -> str:
    response = httpx.get('https://httpbin.org/ip')
    return response.json()['origin']


if __name__ == '__main__':
    print(f"Current IP: {get_ip()}")