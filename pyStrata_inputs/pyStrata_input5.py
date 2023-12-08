import pystrata
profile = pystrata.site.Profile(
    [	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 63.7166, 2293.1806),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 3.7903, 139.4243),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 8.1364, 139.3734),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 10.5767, 170.4277),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 18.6639, 232.4416),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 22.8414, 208.5248),
	pystrata.site.Layer(pystrata.site.SoilType('Rock', 18.0, None, 0.05), 19.2015, 438.0132)
])
