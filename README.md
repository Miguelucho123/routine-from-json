# Rutina de 8 semanas

Aplicación web de una sola página para consultar una rutina de fuerza y cardio en
casa, pensada para usarse desde el celular durante el entrenamiento.

**👉 [Abrir la rutina](https://miguelucho123.github.io/routine-from-json/)**

Plan actual: 8 semanas, 5 días por semana de 30-45 min, en 3 fases, con
superseries de empuje + tirón y un protocolo de hombro en cada sesión.

## Qué incluye

- **Sesión del día**: selector de semana (1-8) y de día; abre en el día de hoy y
  muestra la prescripción de la fase que corresponde a esa semana (series, reps,
  RIR y descanso), la duración estimada, la carga para el hombro y los modos del
  kit que se usan.
- **Superseries agrupadas**: los bloques A1/A2, B1/B2 y los circuitos se muestran
  juntos, como se entrenan.
- **Animaciones de cada ejercicio**: cada movimiento se dibuja y se anima dentro
  de la propia página (SVG generado con JavaScript), sin imágenes ni GIFs
  externos. Son 35: los 27 ejercicios del catálogo, los formatos de cardio y los
  movimientos sueltos.
- **Ficha por ejercicio**: técnica paso a paso, alternativas, carga orientativa y
  un enlace para buscar video en YouTube.
- **Catálogo** completo agrupado por zona, con buscador.
- **Cardio**: saco con puños, rodillazos + footwork, EMOM con pesa rusa e
  intervalos de bajo impacto, con el detalle de cada fase.
- **Guía**: seguridad de hombro y regla del dolor, principios, fases, progresión,
  alimentación, seguimiento, proyección de peso y perfil del equipo.
- Tema claro y oscuro automático, y funcionamiento **sin conexión** después de la
  primera visita.

## En el celular

Ábrela en el navegador y añádela a la pantalla de inicio:

- **iPhone (Safari)**: botón de compartir → *Añadir a pantalla de inicio*.
- **Android (Chrome)**: menú ⋮ → *Añadir a pantalla principal*.

Queda con icono propio y se abre a pantalla completa, como una app.

## Estructura

```
index.html              página publicada (generada, no se edita a mano)
manifest.webmanifest    metadatos para instalarla en el celular
sw.js                   service worker (uso sin conexión)
assets/                 iconos
data/                   rutina en JSON + versión en Word
src/template.html       plantilla: estilos, motor de animación e interfaz
src/build.py            genera index.html a partir de la plantilla y el JSON
```

## Actualizar la rutina

Los datos van incrustados dentro de `index.html` para que la página funcione sin
conexión, así que hay que regenerarla tras cada cambio:

```bash
# 1. editar el JSON de data/
python src/build.py
# 2. commit y push: GitHub Pages publica el cambio en ~1 minuto
```

`build.py` toma el único `.json` que haya en `data/` y valida su sintaxis antes
de escribir, así que un error detiene la generación en lugar de publicar una
página rota.

Si cambia la **estructura** del JSON (nombres de secciones, campos nuevos) hay
que tocar también `src/template.html`, que es donde se decide cómo se pinta cada
parte. Y si aparecen ejercicios nuevos, se les añade su animación en el bloque
`ANIM` de esa misma plantilla; sin ella se dibuja una figura genérica.

## Despliegue

GitHub Pages sirve la rama `main` desde la raíz del repositorio. No hay proceso
de compilación en el servidor: lo que está en `index.html` es lo que se publica.

---

Rutina personal, adaptada a un equipamiento y unas limitaciones concretas
(antecedente de manguito rotador). No es consejo médico ni una rutina genérica.
