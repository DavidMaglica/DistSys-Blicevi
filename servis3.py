import aiohttp
from aiohttp import web
import asyncio

routes = web.RouteTableDef()

@routes.post("/filterJoke")
async def get_activity(request):
    try:
        data =  await request.json()
        data = data[0]

        # joke_data = []
        # joke_data.append({
        #     **data[0]["setup"],
        #     **data[0]["punchline"]
        # })
        
        # async with aiohttp.ClientSession() as session:
        #     tasks = []
        #     tasks.append(asyncio.create_task(session.post(
        #         "http://localhost:3/storeData",
        #         json = joke_data
        #     )))


        res = data

        return web.json_response({ "res": res }, status = 200)

    except Exception as e:
        return web.json_response({ "Failed": str(e) }, status = 500)


app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port = 2)