import pystrata
profile = pystrata.site.Profile(
    [	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 53.4114, 2358.2688),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 8.0942, 147.3985),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 18.8236, 179.2282),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 16.2516, 281.1719),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 23.8711, 256.0531),
	pystrata.site.Layer(pystrata.site.SoilType('Rock', 18.0, None, 0.05), 26.4750, 254.5746)
])
