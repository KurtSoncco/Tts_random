import pystrata
profile = pystrata.site.Profile(
    [	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 57.1296, 2238.3679),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 5.2957, 130.7634),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 6.6260, 141.1489),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 13.1081, 169.7759),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 32.7227, 244.8675),
	pystrata.site.Layer(pystrata.site.SoilType('Rock', 18.0, None, 0.05), 32.0447, 297.7429)
])
