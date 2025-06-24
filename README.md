# Prueba2025

Este repositorio contiene un script simple para obtener las ofertas de trabajo publicadas en [Computrabajo](https://ar.computrabajo.com/empleos-en-cordoba). El script descarga la página, analiza la información de cada oferta y genera un archivo CSV con los datos más relevantes.

## Requisitos

- Python 3.8 o superior
- Las dependencias listadas en `requirements.txt`

Instala las dependencias con:

```bash
pip install -r requirements.txt
```

## Uso

Ejecuta el script `scrape_computrabajo.py`:

```bash
python scrape_computrabajo.py
```

El resultado se guardará en `computrabajo_cordoba.csv` en el mismo directorio.
