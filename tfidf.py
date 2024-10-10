from data import owners, influencers,product_to_category


import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity




def extract_details(user):
  
    products=user.get('products',[])
    categories=user.get('categories',[])
    product_names=[prod['product_name'] for prod in products]
    prod_categories=[product_to_category.get(prod,'') for prod in product_names if prod in product_to_category]
    categories=list(set(prod_categories+[category['category_name'] for category in categories]))
    marketing = [mark['marketing_type'] for mark in user.get('marketing', [])]
    return product_names+ categories+ marketing
    


def main():
    owners_df=pd.DataFrame(owners)
    influencers_df=pd.DataFrame(influencers)
    # print(owners_df['preference'],influencers_df)
    
    owners_df['weighted_preferences'] = owners_df['preference'].apply(extract_details)
    # print(owners_df['weighted_preferences'])
    influencers_df['weighted_preferences'] = influencers_df['preference'].apply(extract_details)

    tfidf = TfidfVectorizer(stop_words='english')
    all_weighted_preferences = pd.concat([owners_df['weighted_preferences'], influencers_df['weighted_preferences']])
    print(all_weighted_preferences)

    # Create a TF-IDF matrix for both business owners and influencers
    tfidf_matrix = tfidf.fit_transform(all_weighted_preferences)

    # Step 7: Calculate cosine similarity across all users (both owners and influencers)
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    # Get the similarity matrix for business owners against influencers
    cosine_sim_owners_to_influencers = cosine_sim[:len(owners_df), len(owners_df):]



    def get_similar_influencers(owner_id, cosine_sim_owners_to_influencers, num_recommendations=3):
        owner_idx = owners_df[owners_df['id'] == owner_id].index[0]
        sim_scores = list(enumerate(cosine_sim_owners_to_influencers[owner_idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[:num_recommendations]  # Top N recommendations
        influencer_indices = [i[0] for i in sim_scores]
        return influencers_df['id'].iloc[influencer_indices]
    
    similar_influencers = get_similar_influencers(101, cosine_sim_owners_to_influencers)
    print(f"Influencers similar to business owner 101: {similar_influencers.tolist()}")



if __name__=='__main__':
    main()
    