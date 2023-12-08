import pystrata
profile = pystrata.site.Profile(
    [	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 55.9483, 2442.2000),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 3.2735, 142.1481),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 14.7161, 148.2138),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 26.2245, 236.4415),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 30.2380, 280.4373),
	pystrata.site.Layer(pystrata.site.SoilType('Rock', 18.0, None, 0.05), 16.5265, 364.0845)
])
