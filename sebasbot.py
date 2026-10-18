# -*- coding: utf-8 -*-
import os
from google import genai

# --- CONFIGURA TU CLAVE DE API AQUI ---
API_KEY = "AQ.Ab8RN6L5hmc6z1KCuh5DDDfHdwQoIp-bt8MTY19FfpLxOeVqvg"

client = genai.Client(api_key=API_KEY)

# --- PERFIL Y CEREBRO DE LA IA ---
instrucciones_sistema = """
Eres SebasBot, un asistente virtual de Inteligencia Artificial avanzado, profesional, eficiente y servicial.
Tu objetivo es responder de manera clara, precisa e inteligente a cualquier pregunta o tarea que te hagan sobre cualquier tema del mundo (tecnologia, programacion, negocios, ciencia, redaccion, ideas, etc.).
Manten siempre un tono respetuoso, directo, util y enfocado en resolver las dudas del usuario.
"""

print("[SebasBot v2.0 - IA Conectada y Lista]")
print("--------------------------------------------------")
print("SebasBot: Hola! Soy SebasBot. Estamos para ayudarte, en que te puedo colaborar hoy?")
print("--------------------------------------------------")
print("(Escribe 'salir' en cualquier momento para cerrar)")

while True:
    entrada = input("\nTu: ")
    if entrada.lower() == 'salir':
        print("\nSebasBot: Hasta luego! Fue un placer ayudarte.")
        break
    
    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=entrada,
            config={"system_instruction": instrucciones_sistema}
        )
        print(f"\nSebasBot: {response.text}")
    except Exception as e:
        print(f"\nSebasBot Error: Revisa tu API Key o tu conexion a internet. ({e})")
