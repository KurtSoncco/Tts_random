import pystrata
profile = pystrata.site.Profile(
    [	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 61.0014, 2217.0008),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 3.5857, 142.9778),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 8.1140, 148.0243),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 8.8188, 174.0023),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 16.3584, 222.8811),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 19.7065, 217.0679),
	pystrata.site.Layer(pystrata.site.SoilType('Rock', 18.0, None, 0.05), 29.3421, 252.1683)
])
