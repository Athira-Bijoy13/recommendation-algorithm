# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import linear_kernel

# # df=pd.read_csv('netflix_titles.csv')
# # df['description']=df['description'].fillna('')

# # tfidf=TfidfVectorizer(stop_words='english')

# # tfidf_matrix=tfidf.fit_transform(df['description'])
# # tfidf_matrix.shape



# # print(tfidf_matrix.top(3))

# # cosine_sim=linear_kernel(tfidf_matrix,tfidf_matrix)
# # indices=pd.Series(df.index,index=df['title']).drop_duplicates()



# # def get_recommendations(title,cosine_sim=cosine_sim, num_recommend=20):
# #     idx=indices[title]
    
# #     sim_scores=list(enumerate(cosine_sim[idx]))
# #     sim_scores=sorted(sim_scores,key=lambda x:x[1],reverse=True)
# #     top_similar=sim_scores[1:num_recommend+1]
# #     movie_indices=[i[0] for i in top_similar]
# #     return df['title'].iloc[movie_indices]



# # print(get_recommendations('Little Things'))


# owners=[{
#     "id": 101,
#     "preference":{
#         "products":[
#             {
#             "product_name":"Apple",
#             "preferred_cost": {
#                 "min": 500, 
#                 "max": 1000
#             }
#         },
#                 {
#             "product_name":"Orange",
#             "preferred_cost": {
#                 "min": 500, 
#                 "max": 1000
#             }
#         },
#             ],
#         "marketing":[
#             {
#     "marketing_type": "instagram",
#     "preferred_cost": {
#         "min": 1000,
#         "max": 3000
#         }
#         },
#             {
#         "marketing_type": "youtube",
#     "preferred_cost": {
#         "min": 1000,
#         "max": 3000
#         }
#         },
    
            
#         ]
#     }
# },
#         {
#     "id": 102,
#     "preference":{
#         "categories":[
#             {
#             "category_name":"Fruits",
#             "preferred_cost": {
#                 "min": 500, 
#                 "max": 1000
#             }
#         }],
#             "marketing":[
#             {
#     "marketing_type": "instagram",
#     "preferred_cost": {
#         "min": 1000,
#         "max": 3000
#         }
#         },
#             {
#         "marketing_type": "youtube",
#     "preferred_cost": {
#         "min": 1000,
#         "max": 3000
#         }
#         },
#                 {
#         "marketing_type": "ads",
#     "preferred_cost": {
#         "min": 1000,
#         "max": 3000
#         }
#         },
    
            
#         ]
#     }
# },
#         {
#     "id":103,
#     "preference":{
#         "products":[
#             {
#             "product_name":"Apple",
#             "preferred_cost": {
#                 "min": 500, 
#                 "max": 1000
#             }
#         },
#                 {
#             "product_name":"Apple",
#             "preferred_cost": {
#                 "min": 500, 
#                 "max": 1000
#             }
#         },
#             ]
#     }
# },
#         {
#     "id": 104,
#     "preference":{
#         "products":[
#             {
#             "product_name":"Apple",
#             "preferred_cost": {
#                 "min": 500, 
#                 "max": 1000
#             }
#         },
#                 {
#             "product_name":"Apple",
#             "preferred_cost": {
#                 "min": 500, 
#                 "max": 1000
#             }
#         },
#             ]
#     }
# },
        
        
#         ]


# influencers=[
#     {
#     "id": 201,
#     "preference":{
#         "products":[
#             {
#             "product_name":"Orange",
#             "preferred_cost": {
#                 "min": 500, 
#                 "max": 1000
#             }
#         },
            
#             ],
#             "marketing":[
#             {
#     "marketing_type": "instagram",
#     "preferred_cost": {
#         "min": 1000,
#         "max": 3000
#         }
#         },
#             {
#         "marketing_type": "youtube",
#     "preferred_cost": {
#         "min": 1000,
#         "max": 3000
#         }
#         },
    
            
#         ]
        
#     }
# },
#     {
#     "id": 202,
#     "preference":{
#         "categories":[
#             {
#             "category_name":"Fruits",
#             "preferred_cost": {
#                 "min": 500, 
#                 "max": 1000
#             }
#         },
            
#             ],
#             "marketing":[
#             {
#     "marketing_type": "instagram",
#     "preferred_cost": {
#         "min": 1000,
#         "max": 3000
#         }
#         },
            
    
            
#         ]
#     }
# },
#     {
#     "id": 203,
#     "preference":{
#         "products":[
#             {
#             "product_name":"Banana",
#             "preferred_cost": {
#                 "min": 500, 
#                 "max": 1000
#             }
#         },
#                 {
#             "product_name":"Orange",
#             "preferred_cost": {
#                 "min": 500, 
#                 "max": 1000
#             }
#         },
#             ]
#     }
# },
    
#     {
#     "id": 205,
#     "preference":{
#         "products":[
#             {
#             "product_name":"Mango",
#             "preferred_cost": {
#                 "min": 500, 
#                 "max": 1000
#             }
#         },
            
#             ]
#     }
# },
# ]
    


# # Create a mapping from product to category
# product_to_category = {
#     'Apple': 'Fruits',
#     'Orange': 'Fruits',
#     'Banana': 'Fruits',
#     'Mango': 'Fruits'
#     # Add more products as needed
# }

# # Function to extract both products and categories separately
# def extract_product_and_category(user):
#     # Extract products and map to categories
#     products = user['preference'].get('products', [])
#     product_names = [prod['product_name'] for prod in products]
#     categories = [product_to_category.get(prod, '') for prod in product_names]

#     # Extract marketing preferences (kept unchanged)
#     marketing = [mark['marketing_type'] for mark in user['preference'].get('marketing', [])]

#     return product_names, categories, marketing

# # Function to build weighted similarity vectors for products and categories
# def build_weighted_vector(user, weight_product=1.0, weight_category=0.5):
#     product_names, categories, marketing = extract_product_and_category(user)
    
#     # Vector consists of product names with full weight and categories with lower weight
#     weighted_vector = product_names * weight_product + categories * weight_category + marketing
#     return " ".join(weighted_vector)

# # Example business owners and influencers data are already defined

# # Convert business owners and influencers into dataframes
# owners_df = pd.DataFrame(owners)
# influencers_df = pd.DataFrame(influencers)

# # Build weighted preference vectors
# owners_df['weighted_preferences'] = owners_df['preference'].apply(build_weighted_vector)
# influencers_df['weighted_preferences'] = influencers_df['preference'].apply(build_weighted_vector)

# # Vectorize preferences using TF-IDF
# tfidf = TfidfVectorizer(stop_words='english')
# all_weighted_preferences = pd.concat([owners_df['weighted_preferences'], influencers_df['weighted_preferences']])

# # Create a TF-IDF matrix for both business owners and influencers
# tfidf_matrix = tfidf.fit_transform(all_weighted_preferences)

# # Calculate cosine similarity across all users (both owners and influencers)
# cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# # Get the similarity matrix for business owners against influencers
# cosine_sim_owners_to_influencers = cosine_sim[:len(owners_df), len(owners_df):]

# # Function to get similar influencers for a given business owner
# def get_similar_influencers(owner_id, cosine_sim_owners_to_influencers, num_recommendations=3):
#     owner_idx = owners_df[owners_df['id'] == owner_id].index[0]
#     sim_scores = list(enumerate(cosine_sim_owners_to_influencers[owner_idx]))
#     sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
#     sim_scores = sim_scores[:num_recommendations]  # Top N recommendations
#     influencer_indices = [i[0] for i in sim_scores]
#     return influencers_df['id'].iloc[influencer_indices]

# # Example: Find influencers similar to business owner with id 101
# similar_influencers = get_similar_influencers(101, cosine_sim_owners_to_influencers)
# print(f"Influencers similar to business owner 101: {similar_influencers.tolist()}")


import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample JSON data
owners = [
    {
        "id": 101,
        "preference": {
            "products": [
                {"product_name": "Apple", "preferred_cost": {"min": 500, "max": 1000}},
                {"product_name": "Orange", "preferred_cost": {"min": 500, "max": 1000}},
            ],
            "marketing": [
                {"marketing_type": "instagram", "preferred_cost": {"min": 1000, "max": 3000}},
                {"marketing_type": "youtube", "preferred_cost": {"min": 1000, "max": 3000}},
            ]
        }
    },
    {
        "id": 102,
        "preference": {
            "categories": [
                {"category_name": "Fruits", "preferred_cost": {"min": 500, "max": 1000}}
            ],
            "marketing": [
                {"marketing_type": "instagram", "preferred_cost": {"min": 1000, "max": 3000}},
                {"marketing_type": "youtube", "preferred_cost": {"min": 1000, "max": 3000}},
                {"marketing_type": "ads", "preferred_cost": {"min": 1000, "max": 3000}},
            ]
        }
    },
    {
        "id": 103,
        "preference": {
            "products": [
                {"product_name": "Apple", "preferred_cost": {"min": 500, "max": 1000}},
                {"product_name": "Apple", "preferred_cost": {"min": 500, "max": 1000}},
            ]
        }
    },
    {
        "id": 104,
        "preference": {
            "products": [
                {"product_name": "Apple", "preferred_cost": {"min": 500, "max": 1000}},
                {"product_name": "Apple", "preferred_cost": {"min": 500, "max": 1000}},
            ]
        }
    }
]

# Function to extract exact product preferences
def extract_exact_products(owner):
    # Extract product names from each owner
    products = owner['preference'].get('products', [])
    product_names = [prod['product_name'] for prod in products]
    
    # Extract marketing preferences
    marketing = [mark['marketing_type'] for mark in owner['preference'].get('marketing', [])]
    
    # Return a combined string of product names and marketing preferences
    return " ".join(product_names + marketing)

# Extract preferences for each owner
owners_df = pd.DataFrame(owners)
owners_df['preferences'] = owners_df['preference'].apply(extract_exact_products)

# Vectorize the exact products using TF-IDF
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(owners_df['preferences'])

# Calculate cosine similarity between all users
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Function to get similar users based on exact products and marketing
def get_similar_users(user_id, cosine_sim=cosine_sim, num_recommendations=2):
    idx = owners_df[owners_df['id'] == user_id].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num_recommendations+1]  # Skip the first one (itself)
    similar_indices = [i[0] for i in sim_scores]
    return owners_df['id'].iloc[similar_indices]

# Example: Get similar users for user with id 101
similar_users = get_similar_users(101)
print(f"Users similar to 101: {similar_users.tolist()}")

