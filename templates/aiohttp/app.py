from aiohttp import web

async def hello(request):
    return web.Response(text="Hello, world")

routes = web.RouteTableDef()

@routes.get('/')
async def hello(request):
    return web.Response(text="Hello, world")

def start_app(args):
    app = web.Application()
    app.add_routes(routes)
    return app