import pystrata
profile = pystrata.site.Profile(
    [	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 59.3512, 2054.3527),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 5.3621, 126.6772),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 9.9958, 145.3095),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 8.3969, 159.5593),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 13.4124, 336.8240),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 20.4018, 225.0061),
	pystrata.site.Layer(pystrata.site.SoilType('Rock', 18.0, None, 0.05), 30.0066, 288.8466)
])
