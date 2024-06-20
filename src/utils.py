import os
import google.auth
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Si modificas estos alcances, elimina el archivo token.json.
SCOPES = ['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/spreadsheets']

path_principal = os.getcwd()
path_credentials = f"{path_principal}/credentials/credentials.json"
path_token = f"{path_principal}/credentials/token.json"


def authenticate():
    """Autentica y obtiene credenciales para acceder a la API de Google Drive."""
    creds = None
    # El archivo token.json almacena los tokens de acceso y actualización del usuario.
    # Se crea automáticamente cuando se completa el flujo de autorización.
    if os.path.exists(path_token):
        creds = Credentials.from_authorized_user_file(path_token, SCOPES)
    # Si no hay credenciales válidas disponibles, solicita al usuario que inicie sesión.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(path_credentials, SCOPES)
            creds = flow.run_local_server(port=0)
        # Guarda las credenciales para la próxima ejecución.
        with open(path_token, 'w') as token:
            token.write(creds.to_json())
    return creds