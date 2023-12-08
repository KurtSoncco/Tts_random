import pystrata
profile = pystrata.site.Profile(
    [	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 63.9881, 2247.4586),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 9.7260, 130.0839),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 7.3936, 167.1433),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 8.8792, 152.3576),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 18.4343, 238.9064),
	pystrata.site.Layer(pystrata.site.SoilType('Rock', 18.0, None, 0.05), 38.5055, 246.6721)
])
