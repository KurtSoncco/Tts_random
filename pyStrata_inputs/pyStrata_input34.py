import pystrata
profile = pystrata.site.Profile(
    [	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 59.3676, 2313.6463),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 4.9668, 139.0585),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 6.5295, 139.3802),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 21.4214, 219.0850),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 16.4375, 329.3743),
	pystrata.site.Layer(pystrata.site.SoilType('Rock', 18.0, None, 0.05), 38.2042, 312.4039)
])
