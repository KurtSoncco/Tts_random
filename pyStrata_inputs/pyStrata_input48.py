import pystrata
profile = pystrata.site.Profile(
    [	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 55.2587, 2546.7535),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 8.3403, 137.3953),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 10.5187, 174.7937),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 13.2329, 218.1434),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 14.6281, 288.1999),
	pystrata.site.Layer(pystrata.site.SoilType('Rock', 18.0, None, 0.05), 44.9482, 316.4294)
])
