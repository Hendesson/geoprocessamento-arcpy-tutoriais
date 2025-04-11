# Geoprocessamento com ArcPy — Tutoriais Práticos

Este repositório reúne funções úteis e tutoriais práticos desenvolvidos durante um estágio com foco em análise espacial e monitoramento ambiental usando ArcPy, ArcGIS Online e PostgreSQL/PostGIS.

## 📚 Conteúdo

- Scripts modulares com funções reutilizáveis em ArcPy
- Conexão com bancos de dados PostgreSQL/PostGIS
- Publicação de dados no ArcGIS Online
- Manipulação de geometrias, interseções e áreas
- Classificação temática (ex: prevenção vs combate ao fogo)

## 📂 Estrutura

- `scripts/`: Funções separadas por tema
- `exemplos/`: Fluxos completos como notebooks
- `dados/`: Exemplos de dados (mockados)
- `utils/`: Conexões e configurações auxiliares

## 🚀 Requisitos

- ArcGIS Pro com licença ArcPy
- Python 3.7+
- pacotes: `geopandas`, `psycopg2`, `arcgis`

## 🧪 Executando

```bash
python scripts/intersect_e_erase.py

