import pystrata
profile = pystrata.site.Profile(
    [	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 59.5727, 2355.5877),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 6.1968, 142.5760),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 5.0782, 133.3573),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 17.4494, 180.1699),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 31.0980, 262.0284),
	pystrata.site.Layer(pystrata.site.SoilType('Rock', 18.0, None, 0.05), 27.5318, 252.1557)
])
