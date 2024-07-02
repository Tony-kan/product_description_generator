def individual_product(product):
    return {
        "id": str(product["_id"]),
        "title": product["name"],
        "description": product["description"],
    }


def all_products(products):
    return [individual_product(product) for product in products]
