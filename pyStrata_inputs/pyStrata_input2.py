import pystrata
profile = pystrata.site.Profile(
    [	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 58.9207, 2353.0175),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 3.7682, 135.5526),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 8.8130, 149.8919),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 12.2918, 162.9212),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 28.3380, 286.3177),
	pystrata.site.Layer(pystrata.site.SoilType('Rock', 18.0, None, 0.05), 34.7953, 287.1770)
])
