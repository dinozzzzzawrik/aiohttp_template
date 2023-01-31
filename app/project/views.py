from aiohttp import web


async def index(request: web.Request) -> None:
    return web.json_response(text='hello world', status=200, content_type='application/json')
