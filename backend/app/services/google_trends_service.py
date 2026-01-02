from pytrends.request import TrendReq

# Initialize pytrends
pytrends = TrendReq(hl='en-US', tz=360)

def get_daily_trends():
    """
    Returns top trending searches for today
    """
    try:
        trending_df = pytrends.trending_searches(pn='united_states')  # Change country as needed
        trends = trending_df[0].tolist()
        return trends
    except Exception as e:
        print("Error fetching trends:", e)
        return []
