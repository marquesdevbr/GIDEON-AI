import os

from dotenv import load_dotenv

load_dotenv()


class Config:

    OPENROUTER_API_KEY = os.getenv(
        "OPENROUTER_API_KEY"
    )

    OPENROUTER_MODEL = os.getenv(
        "OPENROUTER_MODEL",
        "google/gemini-3-flash-preview"
    )

    ELEVENLABS_API_KEY = os.getenv(
        "ELEVENLABS_API_KEY"
    )


print(
    "API KEY:",
    Config.OPENROUTER_API_KEY
)

print(
    "MODEL:",
    Config.OPENROUTER_MODEL
)

print(
    "ELEVENLABS:",
    "Configurado"
    if Config.ELEVENLABS_API_KEY
    else "Não configurado"
)