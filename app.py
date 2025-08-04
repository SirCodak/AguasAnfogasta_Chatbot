import sys
import traceback
import asyncio
from datetime import datetime
from http import HTTPStatus
from aiohttp import web
from aiohttp.web import Request, Response, json_response
from botbuilder.core import (
    TurnContext,
)
from botbuilder.core.integration import aiohttp_error_middleware
from botbuilder.core import MemoryStorage, ConversationState
from botbuilder.integration.aiohttp import CloudAdapter, ConfigurationBotFrameworkAuthentication
from botbuilder.schema import Activity, ActivityTypes
from bots.OpenAI_Connection import (tarea_periodica_async, sincronizar_vector_storage_async)
from bots.Auth_ApiGraph import get_names_sharepoint
import schedule
import time
import threading
import os

from bots.Bot_Asistente import EchoBot
from config import DefaultConfig, ApiGrah_Config, UsersTemp

CONFIG = DefaultConfig()
CONFIG_Api = ApiGrah_Config()
CONFIG_TEMP = UsersTemp()

# Create adapter.
ADAPTER = CloudAdapter(ConfigurationBotFrameworkAuthentication(CONFIG))

# Catch-all for errors.
async def on_error(context: TurnContext, error: Exception):
    print(f"\n [on_turn_error] unhandled error: {error}", file=sys.stderr)
    traceback.print_exc()

    # Send a message to the user
    await context.send_activity("The bot encountered an error or bug.")
    await context.send_activity(
        "To continue to run this bot, please fix the bot source code."
    )

ADAPTER.on_turn_error = on_error

# Create the Bot
memory = MemoryStorage()
conversation_state = ConversationState(memory)
BOT = EchoBot(conversation_state)

# Función que se ejecutará cada 2 minutos
async def ACT_tarea_periodica():
    print("Actualizar")
    UpdatePrompt = await get_names_sharepoint()
    print("Se inició la actualización manual. Favor, esperé hasta que el sistema mande una validación.")
    Actualizar_Manual = await tarea_periodica_async()
    print("Se inició la validación de documentos en el almacén. Si un elemento se encuentra en el almacén, pero no en SharePoint, será eliminado.")
    Actualizar_VectoreStorage = await sincronizar_vector_storage_async()
    print("Se inició la validación de documentos en el almacén. Si un elemento se encuentra en el almacén, pero no en SharePoint, será eliminado.")
    return  # Retorna sin continuar con el flujo normal



# Wrapper para llamar a la función asíncrona desde el scheduler
def run_async_task():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(ACT_tarea_periodica())
    loop.close()

# Programar la tarea cada 90 minutos
schedule.every(90).minutes.do(run_async_task)

# Ejecutar el scheduler en un hilo separado para que no bloquee el bot
def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

# Iniciar el scheduler en un hilo separado
scheduler_thread = threading.Thread(target=run_scheduler)
scheduler_thread.daemon = True  # Esto permite que se cierre al terminar el programa principal
scheduler_thread.start()

# Escuchar solicitudes entrantes en /api/messages
async def messages(req: Request) -> Response:
    return await ADAPTER.process(req, BOT)

APP = web.Application(middlewares=[aiohttp_error_middleware])
APP.router.add_post("/api/messages", messages)

if __name__ == "__main__":
    try:
        web.run_app(APP, host="0.0.0.0", port=CONFIG.PORT)
    except Exception as error:
        raise error
