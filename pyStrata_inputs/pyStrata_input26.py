import pystrata
profile = pystrata.site.Profile(
    [	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 63.1759, 2076.9174),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 7.9274, 138.2690),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 16.0701, 166.6402),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 10.0285, 190.4840),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 25.4901, 252.8664),
	pystrata.site.Layer(pystrata.site.SoilType('Rock', 18.0, None, 0.05), 24.2347, 277.1242)
])
