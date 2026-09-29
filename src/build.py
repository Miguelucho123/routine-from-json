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
def _find_data():
    """Usa el unico JSON de rutina que haya en data/."""
    d = os.path.join(ROOT, "data")
    jsons = sorted(f for f in os.listdir(d) if f.endswith(".json"))
    if len(jsons) != 1:
        raise SystemExit("Se esperaba exactamente un .json en data/, hay %d: %s" % (len(jsons), jsons))
    return os.path.join(d, jsons[0])


DATA = _find_data()
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
    print("index.html generado desde %s" % os.path.basename(DATA))
    print("  %d KB | %d ejercicios | %d semanas" % (len(html) // 1024, ejercicios, semanas))


if __name__ == "__main__":
    main()
