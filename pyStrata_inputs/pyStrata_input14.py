import pystrata
profile = pystrata.site.Profile(
    [	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 51.4711, 2285.9988),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 5.5386, 141.8910),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 8.7586, 150.2800),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 10.3739, 173.8698),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 21.8355, 277.0033),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 27.0015, 228.7016),
	pystrata.site.Layer(pystrata.site.SoilType('Rock', 18.0, None, 0.05), 21.9479, 437.9163)
])
