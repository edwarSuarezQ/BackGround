# Background

Proyecto en Python para eliminar automáticamente el fondo de imágenes.

## Descripción

Procesa imágenes PNG, JPG y JPEG automáticament en `input/`, elimina el fondo con `rembg` y guarda las imágenes sin fondo en `output/` organizadas por fecha. Mueve las originales a `output/[fecha]/originals/`.

## Requisitos

- Python 3.7+
- rembg (`pip install rembg`)

## Instalación

1. Clona este repositorio:

```
git clone https://github.com/edwarSuarezQ/BackGround.git
```

2. Instala la librería `rembg` con el siguiente comando:

```bash
pip install rembg
```

## Uso

1. Pon las imágenes en `input/`

2. Ejecuta:

```bash
python background_remover.py
```
