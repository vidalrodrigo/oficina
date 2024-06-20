import os
from googleapiclient.discovery import build
from utils import authenticate
from gdrive_functions import *


def run_execute():
    try:
        creds = authenticate()
        service = build('drive', 'v3', credentials=creds)
        # Listar archivos
        print("PERMITIDO")
        list_files(service)
    except Exception as err:
        print(f"ERROR: {err}")
if __name__ == '__main__':
    run_execute()
