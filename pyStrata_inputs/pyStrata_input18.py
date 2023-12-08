import pystrata
profile = pystrata.site.Profile(
    [	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 58.2861, 2232.1846),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 3.3541, 145.1464),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 9.7384, 139.4295),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 10.4955, 179.1578),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 24.6347, 240.7433),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 18.3115, 255.0560),
	pystrata.site.Layer(pystrata.site.SoilType('Rock', 18.0, None, 0.05), 22.1067, 342.6357)
])
