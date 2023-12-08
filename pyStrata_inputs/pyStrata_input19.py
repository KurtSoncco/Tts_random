import pystrata
profile = pystrata.site.Profile(
    [	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 52.2413, 2304.7580),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 8.0009, 153.1965),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 16.0816, 173.1178),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 20.7610, 242.0319),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 26.8872, 238.7170),
	pystrata.site.Layer(pystrata.site.SoilType('Rock', 18.0, None, 0.05), 22.9549, 521.5099)
])
