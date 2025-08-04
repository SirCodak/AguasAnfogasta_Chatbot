
# """ Bot Configuration """

import os
import json

# """ Bot Configuration """

class DefaultConfig:

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    APP_TYPE = os.environ.get("MicrosoftAppType", "")
    APP_TENANTID = os.environ.get("MicrosoftAppTenantId", "")
    

class ApiGrah_Config: 

    Tenant_ID = os.environ.get("Tenant_ID", "")
    Client_ID = os.environ.get("Client_ID", "")
    Client_Secret = os.environ.get("Client_Secret", "")
    SiteID = os.environ.get("SiteID", "")

class Redis_Config:

    REDIS_HOST = os.environ.get("REDIS_HOST", "")
    REDIS_PORT = os.environ.get("REDIS_PORT", 6380)  # Puerto SSL
    REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD", "")

class OpenAI_Config:

    AZURE_API_VERSION = os.environ.get("AZURE_API_VERSION", "" )
    DEPLOYMENT_NAME = os.environ.get("DEPLOYMENT_NAME", "")
    AZURE_ENDPOINT = os.environ.get("AZURE_ENDPOINT", "" )
    AZURE_API_KEY = os.environ.get("AZURE_API_KEY", "")
    ASISTENTE_ID = os.environ.get("ASISTENTE_ID", "")
    GPT_API_VERSION = os.environ.get("AZURE_API_VERSION", "" )

class UsersTemp:
 
    Correos_CONFIABILIDAD = "smunoz@tooxs.com"
    Corres_TI = ""
    pares=[
        ["01RDCUULXL3Z5UE3G6CBA3G6F2WITVMCLG", "vs_L6hFifSIJg0bHnJYb5idSJAG"], 
        ["01RDCUULSEFO4ZHSQOTZBIGNGL5J4Z4VDO", "vs_L6hFifSIJg0bHnJYb5idSJAG"],
        ["01RDCUULQSNKJP5RG3PJDITLGW2IP6CMUB", "vs_j3y1stqA8fVuJerPx5QqVBTs"]
    ]

    # default_pares = [
    #     ["01RDCUULXL3Z5UE3G6CBA3G6F2WITVMCLG", "vs_L6hFifSIJg0bHnJYb5idSJAG"], 
    #     ["01RDCUULSEFO4ZHSQOTZBIGNGL5J4Z4VDO", "vs_L6hFifSIJg0bHnJYb5idSJAG"],
    #     ["01RDCUULQSNKJP5RG3PJDITLGW2IP6CMUB", "vs_j3y1stqA8fVuJerPx5QqVBTs"]
    # ]
    
    # # Try to get and parse PARES from environment variables, or use default if not available
    # pares = json.loads(os.environ.get("PARES", json.dumps(default_pares)))


