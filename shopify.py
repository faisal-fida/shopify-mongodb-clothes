import shopify

def upload_data_to_shopify(data):
    """
    Upload data to Shopify
    """
    data = get_womens_clothing_data()
    shop_url = 'shopify_url'
    admin_api_key = 'admin_api_key'
    api_version = 'api_version'

    session = shopify.Session(shop_url, api_version, admin_api_key)
    shopify.ShopifyResource.activate_session(session)

    for item in data:
        product = shopify.Product()
        product.title = item['title']
        product.body_html = item['description']
        product.product_type = "Women's Clothing"
        product.vendor = "Your Vendor Name"
        product.price = item['price']

        variant = shopify.Variant({'option1': item['size']})
        product.variants = [variant]

        product.save()

def main():
    data = get_womens_clothing_data()
    upload_data_to_shopify(data)

if __name__ == '__main__':
    main()
