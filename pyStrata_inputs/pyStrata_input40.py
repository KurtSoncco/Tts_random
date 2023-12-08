import pystrata
profile = pystrata.site.Profile(
    [	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 65.0980, 2185.5011),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 8.0364, 143.8227),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 5.7440, 167.6483),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 9.3897, 200.0591),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 14.6120, 267.7382),
	pystrata.site.Layer(pystrata.site.SoilType('Rock', 18.0, None, 0.05), 44.0468, 284.4945)
])
