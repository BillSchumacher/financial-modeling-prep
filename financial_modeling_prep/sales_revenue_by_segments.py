REVENUE_PRODUCT_SEGMENTATION_ENDPOINT = "v4/revenue-product-segmentation"
# Provides a breakdown of a company's revenue by product category.

# Query Parameters
# symbol: str (required) - the stock ticker
# structure: string - flat
# period: string - annual, quarter


# Response:
"""
{
	"2022-09-24": {
		"Mac": 40177000000,
		"Service": 78129000000,
		"Wearables, Home and Accessories": 41241000000,
		"iPad": 29292000000,
		"iPhone": 205489000000
	}
}
"""

REVENUE_GEO_SEGMENTATION_ENDPOINT = "v4/revenue-geographic-segmentation"
# Provides a breakdown of a company's revenue by geographic region.

# Query Parameters
# symbol: str (required) - the stock ticker
# structure: string - flat
# period: string - annual, quarter

# Response:
"""
{
	"2022-09-24": {
		"Americas Segment": 169658000000,
		"Europe Segment": 95118000000,
		"Greater China Segment": 74200000000,
		"Japan Segment": 25977000000,
		"Rest of Asia Pacific Segment": 29375000000
	}
}
"""

