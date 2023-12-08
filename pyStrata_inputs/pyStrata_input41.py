import pystrata
profile = pystrata.site.Profile(
    [	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 50.7588, 2302.4007),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 5.3908, 139.6239),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 4.9980, 141.5878),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 18.5402, 171.4877),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 13.2213, 342.8845),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 16.3391, 245.7885),
	pystrata.site.Layer(pystrata.site.SoilType('Rock', 18.0, None, 0.05), 37.6787, 359.5838)
])
