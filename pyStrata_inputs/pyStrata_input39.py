import pystrata
profile = pystrata.site.Profile(
    [	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 63.5490, 2249.8692),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 4.2129, 149.5598),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 5.0153, 159.3456),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 10.5980, 179.5632),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 13.4474, 229.9033),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 12.7827, 257.7828),
	pystrata.site.Layer(pystrata.site.SoilType('Rock', 18.0, None, 0.05), 37.3217, 285.1468)
])
