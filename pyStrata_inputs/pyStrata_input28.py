import pystrata
profile = pystrata.site.Profile(
    [	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 60.7839, 2213.4312),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 3.5271, 133.0475),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 10.2000, 146.0058),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 9.5409, 144.7928),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 11.5521, 240.6131),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 16.2183, 294.1376),
	pystrata.site.Layer(pystrata.site.SoilType('Rock', 18.0, None, 0.05), 35.1047, 332.9107)
])
