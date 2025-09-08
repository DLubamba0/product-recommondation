# product_catalog.py

# -------------------------------
# Mock Product Data
# -------------------------------
products = [
    {"name": "Eco Water Bottle", "tags": ["eco-friendly", "durable", "recyclable"]},
    {"name": "Trail Backpack", "tags": ["durable", "water-resistant", "lightweight"]},
    {"name": "Vegan Leather Wallet", "tags": ["vegan", "stylish", "compact"]},
    {"name": "Bamboo Toothbrush", "tags": ["eco-friendly", "vegan", "biodegradable"]},
    {"name": "Smartwatch", "tags": ["tech", "durable", "stylish"]},
    {"name": "Running Shoes", "tags": ["lightweight", "durable", "stylish"]},
    {"name": "Solar Charger", "tags": ["eco-friendly", "tech", "portable"]},
]

# -------------------------------
# Helper Function
# -------------------------------
def count_matches(product_tags, customer_prefs):
    """Count how many tags match between a product and customer preferences."""
    return len(product_tags.intersection(customer_prefs))

# -------------------------------
# Recommendation Function
# -------------------------------
def recommend_products(products, customer_preferences):
    # Convert preferences to a set to remove duplicates
    customer_pref_set = set(customer_preferences)

    recommendations = []
    for product in products:
        product_tags = set(product["tags"])
        matches = count_matches(product_tags, customer_pref_set)
        if matches > 0:  # only recommend products with at least one match
            recommendations.append({"name": product["name"], "matches": matches})

    # Sort by number of matches (descending)
    recommendations.sort(key=lambda x: x["matches"], reverse=True)
    return recommendations

# -------------------------------
# Collect Customer Preferences
# -------------------------------
def main():
    customer_preferences = []
    while True:
        pref = input("Input a preference: ").strip().lower()
        customer_preferences.append(pref)
        cont = input("Do you want to add another preference? (Y/N): ").strip().lower()
        if cont == "n":
            break

    results = recommend_products(products, customer_preferences)

    print("\nRecommended Products:")
    for r in results:
        print(f"- {r['name']} ({r['matches']} match(es))")

if __name__ == "__main__":
    main()


# -------------------------------
# Design Memo (200–300 words)
# -------------------------------
"""
Design Memo
-----------
In this project, I created a simple product recommendation tool using lists, sets, and loops. The products are stored in a list of dictionaries, each containing a name and a list of tags. Customer preferences are collected in a list and later converted into a set. This conversion helps remove duplicates and makes comparisons more efficient.

The core operation used here is the set intersection. For each product, its tags are converted into a set, and the intersection with the customer preference set is computed. The size of this intersection tells us how many preferences match that product. Using sets makes this operation efficient because set lookups and intersections are optimized in Python compared to repeated list scans.

The recommendation function loops through all products, counts matches, and stores results in a list of dictionaries. Sorting is then applied so that products with the highest number of matches are displayed first. This ensures that the customer sees the most relevant recommendations at the top.

If this system were scaled to 1,000 or more products, the logic would largely stay the same, but efficiency would become more important. For example, the product catalog might be stored in a database rather than a static list. Preprocessing steps, such as indexing tags or caching common intersections, could speed up results. Additionally, more advanced techniques such as collaborative filtering or machine learning could be layered on top for richer recommendations.

Overall, this project demonstrates practical use of sets and loops, providing a foundation for real-world recommendation systems while balancing simplicity and efficiency.
"""
