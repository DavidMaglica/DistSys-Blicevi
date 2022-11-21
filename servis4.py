import aiohttp
from aiohttp import web
import asyncio

routes = web.RouteTableDef()

@routes.post("/storeData")
async def get_activity(request):
    try:
       pass

    except Exception as e:
        return web.json_response({ "Failed": str(e) }, status = 500)


app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port = 3)