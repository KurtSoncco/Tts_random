import pystrata
profile = pystrata.site.Profile(
    [	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 56.4185, 2153.0078),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 3.2583, 145.7049),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 11.1386, 161.8401),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 6.6992, 205.5407),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 18.5641, 209.7271),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 18.5029, 237.2247),
	pystrata.site.Layer(pystrata.site.SoilType('Rock', 18.0, None, 0.05), 32.3454, 350.8413)
])
