import pystrata
profile = pystrata.site.Profile(
    [	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 64.1341, 2168.2183),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 3.6550, 146.1992),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 8.1782, 144.1074),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 12.9301, 165.2289),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 19.7487, 239.4086),
	pystrata.site.Layer(pystrata.site.SoilType('Rock', 18.0, None, 0.05), 38.2808, 253.5502)
])
