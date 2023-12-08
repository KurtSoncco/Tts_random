import pystrata
profile = pystrata.site.Profile(
    [	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 54.1577, 2303.5212),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 3.7929, 142.7049),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 16.0336, 162.3399),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 15.9049, 216.8109),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 16.6651, 280.8867),
	pystrata.site.Layer(pystrata.site.SoilType('Rock', 18.0, None, 0.05), 40.3728, 322.1774)
])
