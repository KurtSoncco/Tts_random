import pystrata
profile = pystrata.site.Profile(
    [	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 64.4938, 2240.2682),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 4.8894, 144.5483),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 9.4313, 154.3209),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 11.0293, 158.5208),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 29.5120, 272.1313),
	pystrata.site.Layer(pystrata.site.SoilType('Rock', 18.0, None, 0.05), 27.5710, 255.1492)
])
