import pystrata
profile = pystrata.site.Profile(
    [	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 57.0996, 2445.5170),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 8.0618, 129.9485),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 11.4771, 157.0405),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 25.2968, 219.2781),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 32.2613, 279.5879),
	pystrata.site.Layer(pystrata.site.SoilType('Rock', 18.0, None, 0.05), 12.7302, 523.8694)
])
