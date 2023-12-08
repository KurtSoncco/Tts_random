import pystrata
profile = pystrata.site.Profile(
    [	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 58.2252, 2304.4671),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 3.9371, 144.7427),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 14.8247, 149.6806),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 7.8408, 185.1040),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 33.5917, 304.4162),
	pystrata.site.Layer(pystrata.site.SoilType('Rock', 18.0, None, 0.05), 28.5075, 283.2267)
])
