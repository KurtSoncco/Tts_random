import pystrata
profile = pystrata.site.Profile(
    [	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 63.2919, 2395.1767),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 4.7861, 129.1773),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 15.5486, 148.4962),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 13.1997, 231.4484),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 17.7518, 259.5428),
	pystrata.site.Layer(pystrata.site.SoilType('Rock', 18.0, None, 0.05), 32.3489, 263.2764)
])
