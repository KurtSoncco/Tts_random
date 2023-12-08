import pystrata
profile = pystrata.site.Profile(
    [	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 57.0118, 2250.7309),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 5.9477, 144.1430),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 7.7364, 147.7058),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 8.5241, 180.5780),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 15.5991, 221.2915),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 35.3700, 243.1965),
	pystrata.site.Layer(pystrata.site.SoilType('Rock', 18.0, None, 0.05), 16.7378, 432.3694)
])
