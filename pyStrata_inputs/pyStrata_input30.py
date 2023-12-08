import pystrata
profile = pystrata.site.Profile(
    [	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 55.6040, 2487.3354),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 9.8214, 141.5493),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 11.0069, 179.8621),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 14.4003, 204.1415),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 17.4601, 283.9355),
	pystrata.site.Layer(pystrata.site.SoilType('Rock', 18.0, None, 0.05), 38.6342, 313.5047)
])
