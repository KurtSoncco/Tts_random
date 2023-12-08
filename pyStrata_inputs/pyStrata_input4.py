import pystrata
profile = pystrata.site.Profile(
    [	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 55.4900, 2436.9911),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 5.9560, 145.9287),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 5.8014, 162.1840),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 7.3683, 166.1958),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 15.6441, 195.6182),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 28.7584, 265.9452),
	pystrata.site.Layer(pystrata.site.SoilType('Rock', 18.0, None, 0.05), 27.9087, 402.3598)
])
