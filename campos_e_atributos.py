import arcpy

def add_field_nome_ano_mes(camada):
    arcpy.management.AddField(camada, "data", "DATE")
    arcpy.management.AddField(camada, "ano", "INTEGER")
    arcpy.management.AddField(camada, "mes_nome", "TEXT", field_length=20)
    arcpy.management.AddField(camada, "mes_num", "TEXT", field_length=2)
