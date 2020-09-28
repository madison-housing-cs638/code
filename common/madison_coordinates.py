from geopy import distance

class _GeoPair:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def __sub__(self, other):
        return _GeoPair(self.lat - other.lat, self.lon - other.lon)

    def __add__(self, other):
        return _GeoPair(self.lat + other.lat, self.lon + other.lon)

    def __str__(self):
        return f'({self.lat},{self.lon})'

    def tuple(self):
        return (self.lat, self.lon)

    def dist_km(self, other):
        return distance.distance(self.tuple(), other.tuple()).km

class _MadisonCoordPair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return _MadisonCoordPair(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f'({self.x},{self.y})'

    def __add__(self, other):
        return _MadisonCoordPair(self.x + other.x, self.y + other.y)


FALLES_GEO = _GeoPair(43.061509, -89.449546)
FALLES_MAD = _MadisonCoordPair(803736.92570725, 478026.37722023)

MAD_Y_PET_LAT = abs(-28902.847774619993 / -0.07933299999999832)
MAD_X_PER_LON = abs(-17068.62115716003 / -0.06408499999999151)

def madisonCoordinateToLatLon(madX, madY):
  madPair = _MadisonCoordPair(madX, madY)
  falles_reletive = madPair - FALLES_MAD
  delta_geo = _GeoPair(falles_reletive.y / MAD_Y_PET_LAT, falles_reletive.x / MAD_X_PER_LON)
  result = FALLES_GEO + delta_geo
  return (result.lat, result.lon)
