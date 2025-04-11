# Tutorial: Intersect e Erase com Áreas de Fogo e Unidades de Conservação

Este tutorial mostra como usar a função `intersect_e_erase` para separar as áreas atingidas por fogo que estão **dentro** e **fora** de Unidades de Conservação.

## Requisitos

- ArcPy
- Duas camadas vetoriais:
  - `aaf_2024.shp` (áreas de fogo)
  - `limites_uc.shp` (limites das UCs)

## Código

```python
from scripts.intersect_erase import intersect_e_erase

interior, entorno = intersect_e_erase("aaf_2024.shp", "limites_uc.shp")
```

Resultado:
- `interior`: feições de fogo **dentro das UCs**
- `entorno`: feições de fogo **fora das UCs**
