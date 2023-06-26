from database_handler.mongodb import get_womens_clothing_data
from shopify import upload_data_to_shopify
from analysis import analyze_shopify_results

def main():
    data = get_womens_clothing_data()
    upload_data_to_shopify(data)
    analyze_shopify_results()

if __name__ == '__main__':
    main()
