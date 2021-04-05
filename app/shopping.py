import os
import datetime
from pandas import read_csv
from app.number_decorators import format_usd

def lookup_product(product_id, all_products):
    """
    Params :
        product_id (str) like "8"
        all_products (list of dict) each dict should have "id", "name", "department", "aisle", and "price" attributes
    """
    matching_products = [p for p in all_products if str(p["id"]) == str(product_id)]
    if any(matching_products):
        return matching_products[0]
    else:
        return None

# PREVENT ALL APP CODE FROM BEING IMPORTED

if __name__ == "__main__":

    # READ INVENTORY OF PRODUCTS

    products_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "products.csv")
    products_df = read_csv(products_filepath)
    products = products_df.to_dict("records")

    # CAPTURE PRODUCT SELECTIONS

    selected_products = []
    while True:
        selected_id = input("Please select a product identifier: ")
        if selected_id.upper() == "DONE":
            break
        else:
            matching_product = lookup_product(selected_id, products)
            if matching_product:
                selected_products.append(matching_product)
            else:
                print("OOPS, Couldn't find that product. Please try again.")

    date = datetime.date.today()
    time = datetime.datetime.now()

    subtotal = sum([float(p["price"]) for p in selected_products])

    # PRINT RECEIPT
    checkout_time_format = str(date) + " " + str(time.strftime("%I:%M:%S %p"))
    tax_rate = 0.0875
    total_tax = tax_rate * subtotal
    total_bill = subtotal + total_tax
    
    receipt = ""
    for p in selected_products:
        receipt += "SELECTED PRODUCT: " + p["name"] + "   " + format_usd(p["price"]) + "\n"
    receipt += "---------\n"
    receipt += f"SUBTOTAL: {format_usd(subtotal)}\n"
    receipt += f"TAX: {format_usd(total_tax)}\n"
    receipt += f"TOTAL: {format_usd((total_bill))}\n"
    receipt += "---------\n"
    receipt += "THANK YOU! PLEASE COME AGAIN SOON!\n"
    receipt += "---------\n"

    print("---------")
    print("CHECKOUT AT: " + checkout_time_format)
    print("---------")
    print(receipt)

    # WRITE RECEIPT TO FILE

    receipt_id = checkout_time_format
    receipt_filepath = os.path.join(os.path.dirname(__file__), "..", "receipts", f"{receipt_id}.txt")

    with open(receipt_filepath, "w") as receipt_file:
        receipt_file.write("------------------------------------------\n")
        receipt_file.write(receipt)