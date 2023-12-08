import pystrata
profile = pystrata.site.Profile(
    [	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 60.6928, 2316.9242),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 7.0005, 129.5512),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 15.9606, 178.7384),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 28.3229, 249.3119),
	pystrata.site.Layer(pystrata.site.SoilType('Rock', 18.0, None, 0.05), 34.9501, 272.8541)
])
