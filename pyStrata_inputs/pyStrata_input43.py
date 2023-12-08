import pystrata
profile = pystrata.site.Profile(
    [	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 53.8671, 2524.0792),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 8.5872, 142.5358),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 9.7294, 160.1929),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 22.9523, 208.0994),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 28.8661, 238.7317),
	pystrata.site.Layer(pystrata.site.SoilType('Rock', 18.0, None, 0.05), 22.9248, 820.9000)
])
