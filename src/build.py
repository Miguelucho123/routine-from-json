"""Genera index.html a partir de la plantilla y del JSON de la rutina.

Uso:  python src/build.py

La pagina publicada lleva los datos incrustados para poder funcionar sin
conexion y sin servidor: por eso hay que regenerarla despues de editar el JSON.
"""

import io
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "src", "template.html")
DATA = os.path.join(ROOT, "data", "rutina_12_semanas_70kg.json")
OUTPUT = os.path.join(ROOT, "index.html")
PLACEHOLDER = "__ROUTINE_JSON__"


def main():
    with io.open(DATA, encoding="utf-8") as f:
        raw = f.read()

    rutina = json.loads(raw)  # falla aqui si el JSON quedo mal editado
    if "</script" in raw.lower():
        raise SystemExit("El JSON no puede contener la cadena '</script'.")

    with io.open(TEMPLATE, encoding="utf-8") as f:
        template = f.read()
    if PLACEHOLDER not in template:
        raise SystemExit("La plantilla no contiene " + PLACEHOLDER)

    html = template.replace(PLACEHOLDER, raw.strip())
    with io.open(OUTPUT, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)

    ejercicios = len(rutina["catalogo_ejercicios_fuerza"])
    semanas = rutina["perfil"]["duracion_semanas"]
    print("index.html generado: %d KB | %d ejercicios | %d semanas"
          % (len(html) // 1024, ejercicios, semanas))


if __name__ == "__main__":
    main()
