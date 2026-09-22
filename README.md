# Rutina de 12 semanas

Aplicación web de una sola página para consultar una rutina de fuerza y cardio en
casa, pensada para usarse desde el celular durante el entrenamiento.

**👉 [Abrir la rutina](https://miguelucho123.github.io/routine-from-json/)**

## Qué incluye

- **Rutina día a día**: selector de semana (1-12) y de día; abre por defecto en el
  día de hoy. Muestra series y repeticiones de la sesión, el formato de circuito
  cuando corresponde, y el cardio del final.
- **Animaciones de cada ejercicio**: cada movimiento se dibuja y se anima dentro de
  la propia página (SVG generado con JavaScript), sin imágenes ni GIFs externos.
  Son 18: los 13 ejercicios de fuerza, tres movimientos de cardio y el saco.
- **Ficha por ejercicio**: técnica paso a paso, las dos alternativas previstas y un
  enlace para buscar video en YouTube.
- **Catálogo** completo con buscador, sección de **cardio** (bloque base, intervalos
  y saco) y **guía** con seguridad, principios, progresión y seguimiento de peso.
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
# 1. editar data/rutina_12_semanas_70kg.json
python src/build.py
# 2. commit y push: GitHub Pages publica el cambio en ~1 minuto
```

`build.py` valida el JSON antes de escribir, así que un error de sintaxis detiene
la generación en lugar de publicar una página rota.

## Despliegue

GitHub Pages sirve la rama `main` desde la raíz del repositorio. No hay proceso de
compilación en el servidor: lo que está en `index.html` es lo que se publica.

---

Rutina personal, adaptada a un equipamiento y unas limitaciones concretas
(antecedente de manguito rotador). No es consejo médico ni una rutina genérica.
