import arcpy

def calcular_area_geodesica(camada, campo_area):
    arcpy.management.CalculateGeometryAttributes(camada, [[campo_area, "AREA_GEODESIC"]], area_unit="HECTARES")
