import pystrata
profile = pystrata.site.Profile(
    [	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 52.7672, 2403.0939),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 5.5981, 148.8079),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 7.2382, 166.5725),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 21.9205, 205.7374),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 24.5726, 282.9152),
	pystrata.site.Layer(pystrata.site.SoilType('Rock', 18.0, None, 0.05), 34.8302, 337.3787)
])
