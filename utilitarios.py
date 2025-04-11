def stryear(field):
    return field.year if field else None

def obter_mes(field):
    return field.strftime("%b") if field else None

def obter_num(field):
    return field.strftime("%m") if field else None
