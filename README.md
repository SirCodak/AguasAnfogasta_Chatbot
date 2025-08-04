# Aguas Antofagasta Asistente Bot

Un bot inteligente para Aguas Antofagasta que utiliza Microsoft Bot Framework, Teams, OpenAI Assistants y Azure OpenAI para ofrecer asistencia contextualizada según el departamento del usuario.

## Arquitectura del Sistema

Este bot ha sido desarrollado utilizando las siguientes tecnologías:

- **Microsoft Bot Framework v4**: Framework principal para la creación del bot
- **Azure OpenAI API**: Para mejorar preguntas incompletas o procesamiento inteligente
- **OpenAI Assistants API**: Para manejo de conversaciones contextualizadas
- **Redis**: Almacenamiento de estado de conversaciones
- **Microsoft Teams**: Integración con equipos y recuperación de información de usuario
- **SharePoint**: Almacenamiento de documentos y gestión de archivos
- **Vector Storage**: Para búsqueda semántica y gestión de conocimiento

## Características Principales

- **Asistencia Contextualizada**: El sistema selecciona diferentes asistentes según el departamento del usuario:
  - Departamento de Tecnología e Información
  - Departamento de Confiabilidad
  - Usuarios generales

- **Persistencia de Conversaciones**: Utiliza Redis para mantener el estado de las conversaciones, permitiendo retomar interacciones previas.

- **Integración con Documentos**: Sincronización automática con documentos de SharePoint y almacenamiento vectorial para búsquedas semánticas.

- **Mejora Inteligente de Preguntas**: Utiliza Azure OpenAI para mejorar preguntas incompletas y proporcionar respuestas más precisas.

- **Actualización Automática**: Actualización periódica (cada 90 minutos) de documentos desde SharePoint al vector store.

## Configuración

El sistema se configura a través de variables de entorno organizadas en diferentes clases en `config.py`:

- **DefaultConfig**: Configuración del Bot Framework
- **ApiGrah_Config**: Configuración para la integración con SharePoint
- **Redis_Config**: Configuración de conexión a Redis
- **OpenAI_Config**: Configuración para Azure OpenAI y OpenAI Assistants
- **UsersTemp**: Configuración de usuarios y pares de almacenamiento

## Instalación y Ejecución

### Requisitos previos

- Python 3.8+
- Cuenta de Azure con Azure OpenAI configurado
- Cuenta de OpenAI para Assistants API
- Instancia de Redis
- SharePoint configurado con los documentos necesarios

### Configuración de variables de entorno

Configure las siguientes variables de entorno:

```
# Bot Framework
MicrosoftAppId
MicrosoftAppPassword
MicrosoftAppType
MicrosoftAppTenantId

# SharePoint/Graph API
Tenant_ID
Client_ID
Client_Secret
SiteID

# Redis
REDIS_HOST
REDIS_PORT
REDIS_PASSWORD

# OpenAI
AZURE_API_VERSION
DEPLOYMENT_NAME
AZURE_ENDPOINT
AZURE_API_KEY
ASISTENTE_ID
```

### Instalación

1. Clone el repositorio
2. Cree un entorno virtual: `python -m venv .venv`
3. Active el entorno virtual
4. Instale las dependencias: `pip install -r requirements.txt`
5. Configure las variables de entorno según lo descrito anteriormente

### Ejecución

```bash
python app.py
```

El bot estará disponible en `http://localhost:3978/api/messages`

## Comandos Especiales

- `/actualizar`: Activa manualmente la sincronización entre SharePoint y el Vector Storage

## Arquitectura de Código

- **app.py**: Punto de entrada principal, configura el bot y los servicios
- **bots/Bot_Asistente.py**: Implementación principal del bot, maneja los mensajes y la integración con Teams
- **bots/OpenAI_Connection.py**: Integración con OpenAI Assistants API y gestión de hilos de conversación
- **bots/AzureGPT.py**: Integración con Azure OpenAI para mejora de preguntas
- **bots/Redis_Connection.py**: Manejo de persistencia con Redis
- **bots/Auth_ApiGraph.py**: Integración con Microsoft Graph API para SharePoint

## Flujo de Funcionamiento

1. Un usuario envía un mensaje al bot a través de Teams
2. El bot obtiene información del usuario (correo, departamento) desde Teams
3. Según el departamento, selecciona un asistente específico
4. Consulta Redis para ver si existe una conversación previa para ese usuario
5. Si existe, retoma la conversación; si no, crea una nueva
6. Procesa la respuesta del asistente, manejando casos de respuestas incompletas o errores
7. Devuelve la respuesta al usuario

## Mantenimiento

El sistema incluye tareas programadas para sincronizar documentos entre SharePoint y el Vector Storage cada 90 minutos.

Para realizar esta operación manualmente, envíe el comando `/actualizar` al bot.
