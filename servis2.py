import aiohttp
from aiohttp import web
import asyncio

routes = web.RouteTableDef()

@routes.post("/filterUser")
async def get_activity(request):
    try:
        data = await request.json()
        data = data[0]

        user_data.get("name")


        # user_data = data
        # user_data.append({
        #     **data["name"],
        #     **data["location"]["city"],
        #     **data["login"]["username"]
        # })

        # async with aiohttp.ClientSession() as session:
        #     tasks = []
        #     tasks.append(asyncio.create_task(session.post(
        #         "http://localhost:3/storeData",
        #         json = user_data
        #     )))

        return web.json_response({ "res": data }, status = 200)


    except Exception as e:
        return web.json_response({ "Failed": str(e) }, status = 500)


app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port = 1)