from GestorErrores import GestorErrores

class coche:
    def __init__(self,sBrand, sModel, iModelYear, iMilage, sFuelType, sEngine, sTransmission, sExtCol, sIntCol, sAccident, bCleanTitle, fPrice):
        self._lErrores = []

        self._sBrand = ""
        self._sModel = ""
        self._iModelYear = -1
        self._iMilage = -1
        self._sFuelTipe = ""
        self._sEngine = ""
        self._sTrasmission = ""
        self._sExtCol = ""
        self._sIntCol = ""
        self._sAccident = ""
        self._bCleanTitle = None
        self._fPrice = -1.00
        
        self.sBrand = sBrand
        self.sModel = sModel
        self.iModelYear = iModelYear
        self.iMilage = iMilage
        self.sFuelTipe = sFuelType
        self.sEngine = sEngine
        self.sTrasmission = sTransmission
        self.sExtCol = sExtCol
        self.sIntCol = sIntCol
        self.sAccident = sAccident
        self.bCleanTitle = bCleanTitle
        self.fPrice = fPrice

    def _registrarError(self, iCodigo):
        if iCodigo != GestorErrores.EXITO:
            self._lErrores.append(iCodigo)

    @property
    def sBrand(self):
        return self._sBrand
    
    @sBrand.setter
    def sBrand(self, valor):
        iErr = GestorErrores.EXITO
        if not isinstance(valor, str):
            iErr = GestorErrores.ERR_BRAND_TIPO
        elif len(valor)<1 or len(valor)>100:
            iErr = GestorErrores.ERR_BRAND_LONGITUD
        else:
            self._sBrand = valor
        self._registrarError(iErr)

    @property
    def sModel(self):
        return self._sModel
    
    @sModel.setter
    def sModel(self, valor):
        iErr = GestorErrores.EXITO
        if not isinstance(valor, str):
            iErr = GestorErrores.ERR_MODEL_TIPO
        elif len(valor)<1 or len(valor)>100:
            iErr = GestorErrores.ERR_MODEL_LONGITUD
        else:
            self._sModel = valor
        self._registrarError(iErr)

    @property
    def iModelYear(self):
        return self._iModelYear
    
    @iModelYear.setter
    def iModelYear(self, valor):
        iErr = GestorErrores.EXITO
        if not isinstance(valor, int):
            iErr = GestorErrores.ERR_MODELYEAR_TIPO
        elif valor>2026 and valor<1900:
            iErr = GestorErrores.ERR_MODELYEAR_VALOR
        else:
            self._iModelYear = valor
        self._registrarError(iErr)

    @property
    def iMilage(self):
        return self._iMilage
    
    @iMilage.setter
    def iMilage(self, valor):
        iErr = GestorErrores.EXITO
        if not isinstance(valor, int):
            iErr = GestorErrores.ERR_MILAGE_TIPO
        elif valor<0:
            iErr = GestorErrores.ERR_MILAGE_VALOR
        else:
            self._iMilage = valor
        self._registrarError(iErr)

    @property
    def sFuelTipe(self):
        return self._sFuelTipe
    
    @sFuelTipe.setter
    def sFuelTipe(self, valor):
        iErr = GestorErrores.EXITO
        if not isinstance(valor, str):
            iErr = GestorErrores.ERR_FUELTYPE_TIPO
        elif len(valor)<1 or len(valor)>100:
            iErr = GestorErrores.ERR_FUELTYPE_LONGITUD
        else:
            self._sFuelTipe = valor
        self._registrarError(iErr)

    @property
    def sEngine(self):
        return self._sEngine
    
    @sEngine.setter
    def sEngine(self, valor):
        iErr = GestorErrores.EXITO
        if not isinstance(valor, str):
            iErr = GestorErrores.ERR_ENGINE_TIPO
        elif len(valor)<1 or len(valor)>100:
            iErr = GestorErrores.ERR_ENGINE_LONGITUD
        else:
            self._sEngine = valor
        self._registrarError(iErr)

    @property
    def sTrasmission(self):
        return self._sTrasmission
    
    @sTrasmission.setter
    def sTrasmission(self, valor):
        iErr = GestorErrores.EXITO
        if not isinstance(valor, str):
            iErr = GestorErrores.ERR_TRANSMISSION_TIPO
        elif len(valor)<1 or len(valor)>100:
            iErr = GestorErrores.ERR_TRANSMISSION_LONGITUD
        else:
            self._sTrasmission = valor
        self._registrarError(iErr)

    @property
    def sExtCol(self):
        return self._sExtCol
    
    @sExtCol.setter
    def sExtCol(self, valor):
        iErr = GestorErrores.EXITO
        if not isinstance(valor, str):
            iErr = GestorErrores.ERR_EXTCOL_TIPO
        elif len(valor)<1 or len(valor)>100:
            iErr = GestorErrores.ERR_EXTCOL_LONGITUD
        else:
            self._sExtCol = valor
        self._registrarError(iErr)

    @property
    def sIntCol(self):
        return self._sIntCol
    
    @sIntCol.setter
    def sIntCol(self, valor):
        iErr = GestorErrores.EXITO
        if not isinstance(valor, str):
            iErr = GestorErrores.ERR_INTCOL_TIPO
        elif len(valor)<1 or len(valor)>100:
            iErr = GestorErrores.ERR_INTCOL_LONGITUD
        else:
            self._sIntCol = valor
        self._registrarError(iErr)

    @property
    def sAccident(self):
        return self._sAccident
    
    @sAccident.setter
    def sAccident(self, valor):
        iErr = GestorErrores.EXITO
        if not isinstance(valor, str):
            iErr = GestorErrores.ERR_ACCIDENT_TIPO
        elif len(valor)<1 or len(valor)>100:
            iErr = GestorErrores.ERR_ACCIDENT_LONGITUD
        else:
            self._sAccident = valor
        self._registrarError(iErr)

    @property
    def bCleanTitle(self):
        return self._bCleanTitle
    
    @bCleanTitle.setter
    def bCleanTitle(self, valor):
        iErr = GestorErrores.EXITO
        if not isinstance(valor, bool):
            iErr = GestorErrores.ERR_CLEANTITLE_TIPO
        else:
            self._bCleanTitle = valor
        self._registrarError(iErr)

    @property
    def fPrice(self):
        return self._fPrice
    
    @fPrice.setter
    def fPrice(self, valor):
        iErr = GestorErrores.EXITO
        if not isinstance(valor, float):
            iErr = GestorErrores.ERR_PRICE_TIPO
        elif valor<0:
            iErr = GestorErrores.ERR_PRICE_VALOR
        else:
            self._fPrice = valor
        self._registrarError(iErr)

        
    
    def __str__(self):
        return f''