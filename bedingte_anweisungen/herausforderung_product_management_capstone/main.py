# Input variables
days_until_expiration = 5  # Example value
product_type = "Perishable"  # Can be "Perishable" or "Non-Perishable"

if product_type == "Perishable":
    if days_until_expiration <= 3:
        print("Big discount applied")
    else:
        print("Small discount applied")
else:
    print("No discount for non-perishable items.")