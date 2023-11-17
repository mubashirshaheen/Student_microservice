# api_consumer/views.py
import aiohttp
import asyncio
from django.http import JsonResponse

import json


# some JSON:


async def get_call_api(url: str):
    async with aiohttp.ClientSession() as session:
        # url = 'http://127.0.0.1:8001/api/students/'
        async with session.get(url) as response:
            data = await response.json()
    # x = '{ "name":"John", "age":30, "city":"New York"}'
    #
    # # parse x:
    # y = json.loads(x)
    # return JsonResponse(y)
    return JsonResponse(data, safe=False)


async def getallstudents(response):
    url = 'http://127.0.0.1:8001/api/students/'
    data = await get_call_api(url)
    return data


async def getallcourses(response):
    url = 'http://127.0.0.1:8001/api/courses/'
    data = await get_call_api(url)
    return data


async def getallcolleges(response):
    url = 'http://127.0.0.1:8001/api/colleges/'
    data = await get_call_api(url)
    return data
