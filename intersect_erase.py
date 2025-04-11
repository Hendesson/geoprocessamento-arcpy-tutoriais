import arcpy

def intersect_e_erase(aaf, ucs):
    intersect = r'memory\intersect'
    erase = r'memory\erase'

    arcpy.analysis.Intersect([aaf, ucs], intersect, output_type="INPUT")
    arcpy.management.AddField(intersect, "local", "TEXT", field_length=10)
    with arcpy.da.UpdateCursor(intersect, ["local"]) as cursor:
        for row in cursor:
            row[0] = "interior"
            cursor.updateRow(row)

    arcpy.analysis.Erase(aaf, ucs, erase)
    arcpy.management.AddField(erase, "local", "TEXT", field_length=10)
    with arcpy.da.UpdateCursor(erase, ["local"]) as cursor:
        for row in cursor:
            row[0] = "entorno"
            cursor.updateRow(row)

    return intersect, erase
