# Shopify MongoDB Clothes

## Overview

This project integrates Shopify with MongoDB to manage and analyze women's clothing data. It scrapes product data from Shopify, stores it in MongoDB, and provides analytical insights.

## Complexities

### Shopify API Integration
- **Challenge:** Seamless communication with Shopify's API.
- **Solution:** Utilized the `shopify` Python package to manage sessions and handle API requests effectively.

### Data Management
- **Challenge:** Efficiently storing and retrieving large datasets.
- **Solution:** Leveraged MongoDB for its scalability and ease of use with the `pymongo` library.

## Challenges and Solutions

### Challenge 1: API Rate Limits
- **Problem:** Handling Shopify API rate limits.
- **Solution:** Implemented session management to handle retries and respect rate limits.

### Challenge 2: Dynamic Data Handling
- **Problem:** Parsing and analyzing dynamically changing data.
- **Solution:** Used MongoDB's flexible schema design to accommodate varying data structures.

## Getting Started

### Prerequisites
- Python 3.8+
- MongoDB
- Shopify Admin API Key

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/faisal-fida/shopify-mongodb-clothes.git
   cd shopify-mongodb-clothes
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   ```plaintext
   SHOPIFY_URL=your_shopify_url
   ADMIN_API_KEY=your_admin_api_key
   API_VERSION=your_api_version
   ```

4. Run the application:
   ```bash
   python main.py
   ```

## Usage

- The script fetches women's clothing data from MongoDB and uploads it to Shopify.
- It also provides a function to analyze the products uploaded to Shopify.

## Contributing

We welcome contributions. Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
