"""Sales Revenue by Segments API endpoints and class."""
REVENUE_PRODUCT_SEGMENTATION_ENDPOINT = "v4/revenue-product-segmentation"
REVENUE_GEO_SEGMENTATION_ENDPOINT = "v4/revenue-geographic-segmentation"


class SalesRevenueBySegments:
    """
    A class to access sales revenue segmentation information for companies.

    Explanation:
    This class provides methods to retrieve revenue breakdowns by
      product category and geographic region for a company.

    Methods:
    - revenue_product_segmentation:
     Provides a breakdown of a company's revenue by product category.
    - revenue_geo_segmentation:
     Provides a breakdown of a company's revenue by geographic region.
    """

    def __init__(self, api):
        """
        Initializes the SalesRevenueBySegments class with the provided API object.

        Args:
            api: The API object for interacting with the API.

        Returns:
            None
        """
        self.api = api

    def revenue_product_segmentation(self, symbol, period, structure="flat"):
        """Provides a breakdown of a company's revenue by product category.

        Args:
            symbol (str): the stock ticker
            period (str): annual, quarter
            structure (str): flat

        Returns: {
            "2022-09-24": {
                "Mac": 40177000000,
                "Service": 78129000000,
                "Wearables, Home and Accessories": 41241000000,
                "iPad": 29292000000,
                "iPhone": 205489000000
            }
        }
        """
        return self.api.get(
            REVENUE_PRODUCT_SEGMENTATION_ENDPOINT,
            params={"symbol": symbol, "period": period, "structure": structure},
        )

    def revenue_geo_segmentation(self, symbol, period, structure="flat"):
        """Provides a breakdown of a company's revenue by geographic region.

        Args:
            symbol (str): the stock ticker
            period (str): annual, quarter
            structure (str): flat

        Returns: {
            "2022-09-24": {
                "Americas Segment": 169658000000,
                "Europe Segment": 95118000000,
                "Greater China Segment": 74200000000,
                "Japan Segment": 25977000000,
                "Rest of Asia Pacific Segment": 29375000000
            }
        }
        """
        return self.api.get(
            REVENUE_GEO_SEGMENTATION_ENDPOINT,
            params={"symbol": symbol, "period": period, "structure": structure},
        )
