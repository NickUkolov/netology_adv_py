from google_maps_reviews import ReviewsClient

def map():
    client = ReviewsClient(api_key='SECRET_API_KEY')
    results = print(type(client))
    return results
