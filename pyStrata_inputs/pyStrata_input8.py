import pystrata
profile = pystrata.site.Profile(
    [	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 61.0588, 2138.4123),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 3.3220, 134.1844),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 13.9530, 160.8261),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 13.7538, 201.4373),
	pystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), 32.7368, 290.5731),
	pystrata.site.Layer(pystrata.site.SoilType('Rock', 18.0, None, 0.05), 22.1025, 284.7831)
])
