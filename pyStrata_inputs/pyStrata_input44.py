import pystrata
profile = pystrata.site.Profile(
    [	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 58.4303, 2213.7574),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 4.7425, 138.7354),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 7.1060, 136.9947),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 13.2709, 146.2177),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 26.6849, 236.3778),
	pystrata.site.Layer(pystrata.site.SoilType('Rock', 18.0, None, 0.05), 36.6922, 263.6763)
])
