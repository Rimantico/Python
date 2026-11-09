# Python · Tema 1

## Organización

- `retos/`: ejercicios numerados; se conserva su numeración original.
- `ejemplos/`: ejemplo de clase y ejercicio de palíndromos.
- `pruebas/`: programas de prueba.
- `herramientas/ping/`: programa de ping y su archivo `host.txt`.
- `herramientas/automatizacion/`: automatización con PyAutoGUI.
- `.venv/`: entorno virtual existente.

## Ejecución

Desde esta carpeta, activa el entorno virtual:

```bash
source .venv/bin/activate
python retos/reto_01.py
```

El programa de ping busca `host.txt` en el directorio de trabajo. Ejecútalo desde su carpeta:

```bash
cd herramientas/ping
python "Ping con host.py"
```

Los archivos se han reubicado sin modificar su contenido. `organizacion.json` registra las rutas anteriores y actuales, y sus huellas SHA-256.
