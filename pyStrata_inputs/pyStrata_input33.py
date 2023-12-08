import pystrata
profile = pystrata.site.Profile(
    [	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 59.3668, 2366.1337),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 6.2066, 136.8249),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 7.4131, 155.4659),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 24.6027, 212.6492),
	pystrata.site.Layer(pystrata.site.SoilType('Rock', 18.0, None, 0.05), 49.3376, 270.6455)
])
