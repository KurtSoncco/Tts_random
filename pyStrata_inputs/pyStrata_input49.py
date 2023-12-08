import pystrata
profile = pystrata.site.Profile(
    [	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 55.7343, 2606.5749),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 4.2088, 139.9713),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 10.5427, 145.7163),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 20.1619, 170.5659),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 13.0826, 405.7659),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 16.4594, 277.4010),
	pystrata.site.Layer(pystrata.site.SoilType('Rock', 18.0, None, 0.05), 26.7372, 437.4347)
])
