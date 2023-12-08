import pystrata
profile = pystrata.site.Profile(
    [	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 65.0994, 2298.0643),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 3.7650, 139.3726),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 10.9081, 142.3201),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 19.3182, 188.2991),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 11.4526, 273.6179),
	pystrata.site.Layer(pystrata.site.SoilType('Rock', 18.0, None, 0.05), 36.3836, 259.6257)
])
