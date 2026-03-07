class GestorErrores: 
    EXITO = 0
    ERR_BRAND_TIPO = 1
    ERR_BRAND_LONGITUD = 2
    ERR_MODEL_TIPO = 3
    ERR_MODEL_LONGITUD = 4
    ERR_MODELYEAR_TIPO = 5
    ERR_MODELYEAR_VALOR = 6
    ERR_MILAGE_TIPO = 7
    ERR_MILAGE_VALOR = 8
    ERR_FUELTYPE_TIPO = 9
    ERR_FUELTYPE_LONGITUD = 10
    ERR_ENGINE_TIPO = 11
    ERR_ENGINE_LONGITUD = 12
    ERR_TRANSMISSION_TIPO = 13
    ERR_TRANSMISSION_LONGITUD = 14
    ERR_EXTCOL_TIPO = 15
    ERR_EXTCOL_LONGITUD = 16
    ERR_INTCOL_TIPO = 17
    ERR_INTCOL_LONGITUD = 18
    ERR_ACCIDENT_TIPO = 19
    ERR_ACCIDENT_LONGITUD = 20
    ERR_CLEANTITLE_TIPO = 21
    ERR_PRICE_TIPO = 22
    ERR_PRICE_VALOR = 23

    _dErrores = {
        ERR_BRAND_TIPO: "Error: La marca debe ser tipo string.",
        ERR_BRAND_LONGITUD: "Error: La marca debe ser de entre 1 y 100 caracteres.",
        ERR_MODEL_TIPO: "Error: El modelo debe ser tipo string.",
        ERR_MODEL_LONGITUD: "Error: El modelo debe ser de entre 1 y 100 caracteres.",
        ERR_MODELYEAR_TIPO: "Error: El año del modelo debe ser tipo int.",
        ERR_MODELYEAR_VALOR: "Error: El año del modelo debe ser de entre 1900 y 2026.",
        ERR_MILAGE_TIPO: "Error: El kilometraje debe ser tipo int.",
        ERR_MILAGE_VALOR: "Error: El kilometraje debe ser mayor de 0.",
        ERR_FUELTYPE_TIPO: "Error: El tipo de combustible debe ser tipo string.",
        ERR_FUELTYPE_LONGITUD: "Error: El tipo de combustible debe ser de entre 1 y 100 caracteres.",
        ERR_ENGINE_TIPO: "Error: El motor debe ser tipo string.",
        ERR_ENGINE_LONGITUD: "Error: El motor debe ser de entre 1 y 100 caracteres.",
        ERR_TRANSMISSION_TIPO: "Error: La transmisión debe ser tipo string.",
        ERR_TRANSMISSION_LONGITUD: "Error: La transmisión debe ser de entre 1 y 100 caracteres.",
        ERR_EXTCOL_TIPO: "Error: El color del exterior debe ser tipo string.",
        ERR_EXTCOL_LONGITUD: "Error: El color del exterior debe ser de entre 1 y 100 caracteres.",
        ERR_INTCOL_TIPO: "Error: El color del interior debe ser tipo string.",
        ERR_INTCOL_LONGITUD: "Error: El color del interior debe ser de entre 1 y 100 caracteres.",
        ERR_ACCIDENT_TIPO: "Error: EL accidente debe ser tipo string.",
        ERR_ACCIDENT_LONGITUD: "Error: El accidente debe ser de entre 1 y 100 caracteres.",
        ERR_CLEANTITLE_TIPO: "Error: El titulo limpio debe ser tipo booleano.",
        ERR_PRICE_TIPO: "Error: El precio debe ser tipo float.",
        ERR_PRICE_VALOR: "Error: El precio debe ser de entre 1 y 100 caracteres."
    }

    @staticmethod
    def getMessage(iCodigo):
        return GestorErrores._mensajes.get(iCodigo, "Error desconocido.")