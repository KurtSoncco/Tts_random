import pystrata
profile = pystrata.site.Profile(
    [	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 59.0734, 2425.0591),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 3.8850, 138.2635),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 8.0176, 153.5747),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 13.2032, 182.8636),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 20.8805, 256.2698),
	pystrata.site.Layer(pystrata.site.SoilType('Rock', 18.0, None, 0.05), 41.8673, 275.8304)
])
