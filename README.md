financial-modeling-prep-api
===========================

This is a Python package for financialmodelingprep.com API.

It is a simple package that allows you to get the data from the API.

I searched for a complete package for the API, but I could not find one.

I decided to create this package to help others who are looking for a complete package for the API.

Every endpoint is implemented in the package, including websockets.

They might not work or have errors however, this is a work in progress, see Known Issues / TODO.

## Installation

You can install the package using pip:

```bash
pip install financial-modeling-prep-api
```

## Usage

You can use the package to get the data from the API. You can use the following code to get the data:

```python
from financial_modeling_prep import FinancialModelingPrep

fmp = FinancialModelingPrep(api_key='your_api_key')

# Get the profile of the company
profile = fmp.company_info.get_company_profile('AAPL')
```

The various endpoints are broken down into different classes. You can use the following classes to get the data, this matches the documentation at financialmodelingprep.com.


Contributing
------------

If you would like to contribute to the package, please feel free to fork the repository and submit a pull request. You can also submit an issue if you would like to see a new feature or if you have found a bug.

This is still very much a work in progress, so any help is appreciated.

Known Issues / TODO
-------------------
- The package is still in development and is not yet ready for production use.
- The package is not tested, and therefore broken.
- Types are not yet fully implemented and may not be accurate.
- Params need validation and error handling.
- Error handling is non-existent.
- Requests-cache is not appropriate for all endpoints.
- Exponential backoff is not implemented when the API rate limit is reached. Although, requests-cache should help with this.


## License

This package is licensed under the MIT License. Please see the [LICENSE](LICENSE) file for more information.
