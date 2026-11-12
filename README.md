# Ahorcado

Juego de ahorcado con la API de Claude.

## Requisitos

- Python 3.10 o superior (probado con 3.15)
- anthropic>=2.3.0
- python-dotenv>=1.2.4
- streamlit>=1.67.0

## Instalación

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install "anthropic>=2.3.0" "python-dotenv>=1.2.4" "streamlit>=1.67.0"
```

Crear un archivo `.env`:

```
ANTHROPIC_API_KEY=
```

## Ejecutar

```bash
source .venv/bin/activate
```

Web:

```bash
streamlit run app.py
```

Consola:

```bash
python main.py
```
