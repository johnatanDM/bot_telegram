import os
import json
import requests
from aiohttp import web
from banco_de_dados import resposta_jira_dump 

token = os.getenv("BOT_API_TOKEN")
URL = "https://api.telegram.org/bot{}/".format(token)


async def resposta_dump(request):
    resposta_jira = await request.json()
    mensagem, usuario = resposta_jira_dump(resposta_jira) 
    requests.post(URL + 'sendMessage' , data = {'chat_id' : usuario, 'text' : mensagem})
    return web.Response()




app = web.Application()
app.add_routes([web.post('/resposta_dump', resposta_dump)])
web.run_app(app,host='172.30.91.9', port=3030)



