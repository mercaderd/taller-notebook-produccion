# Taller: De notebook a modelo en producción

## Resumen

1. Crear una biblioteca Python con el código reutilizable correspondiente al proyecto
   y probar que funciona desde un intérprete de Python
2. Crear una aplicación web usando FastAPI que haga uso de ese código
   y probar que funciona desde Gitpod
3. Desplegar la aplicación web en Railway [Pendiente]

## Referencias

- https://github.com/astrojuanlu/ie-mbd-advanced-python/

## Enlaces

- https://fastapi.tiangolo.com/
- https://www.gitpod.io/
- https://voila.readthedocs.io/
- https://shiny.rstudio.com/py/
- https://railway.app/?referralCode=VO2J82 (afiliado)

Utilidades nuevas:
- pip-tools and pip-compile: compila y genera requirements.txt desde requirements.in Más completo que hacer simplemente pip freeze.
- flint: para crear fácilmente los metadatos de módulos de python que se puedan instalar con pip sin tener que hacer setup.py


## Instrucciones

```
python -m venv .venv
source .venv/bin/activate
pip install -U pip pip-tools
pip-compile
pip install -r requirements.txt
pip install flit
mkdir library && cd library
flit init
pip install black
uvicorn app:app --reload
```
