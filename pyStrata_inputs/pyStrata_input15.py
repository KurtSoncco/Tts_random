import pystrata
profile = pystrata.site.Profile(
    [	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 55.7793, 2386.5049),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 12.6151, 133.2967),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 12.1452, 158.4588),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 12.0811, 209.0362),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 21.1181, 268.0807),
	pystrata.site.Layer(pystrata.site.SoilType('Rock', 18.0, None, 0.05), 33.1882, 286.5014)
])
