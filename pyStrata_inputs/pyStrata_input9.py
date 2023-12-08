import pystrata
profile = pystrata.site.Profile(
    [	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 56.9332, 2364.1163),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 12.6363, 159.3309),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 15.7272, 178.9263),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 13.5481, 318.1905),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 29.6315, 248.9173),
	pystrata.site.Layer(pystrata.site.SoilType('Rock', 18.0, None, 0.05), 18.4506, 420.4886)
])
