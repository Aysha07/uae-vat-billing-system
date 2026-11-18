import datetime

# Sample Dubai Cafe / Retail Store Menu (Item: Price in AED)
menu = {
    "1": {"name": "Karak Chai", "price": 5.00},
    "2": {"name": "Chicken Shawarma", "price": 12.00},
    "3": {"name": "Fresh Orange Juice", "price": 15.00},
    "4": {"name": "Club Sandwich", "price": 25.00},
    "5": {"name": "Arabic Coffee Pot", "price": 35.00}
}

VAT_RATE = 0.05  # 5% UAE VAT


def display_menu():
    print("\n--- DUBAI CAFE & RETAIL MENU ---")
    for key, item in menu.items():
        print(f"{key}. {item['name']} - {item['price']:.2f} AED")
    print("--------------------------------")


def calculate_bill(cart):
    subtotal = sum(item["total"] for item in cart)
    
    # Apply 10% discount if subtotal is 100 AED or more
    discount = 0.0
    if subtotal >= 100:
        discount = subtotal * 0.10
        
    taxable_amount = subtotal - discount
    vat_amount = taxable_amount * VAT_RATE
    grand_total = taxable_amount + vat_amount
    
    return subtotal, discount, vat_amount, grand_total


def print_and_save_receipt(customer_name, cart, subtotal, discount, vat, total):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    receipt_lines = [
        "\n========================================",
        "         DUBAI RETAIL & CAFE            ",
        "       TRN: 100234567800003 (UAE)       ",
        f"Date: {now}",
        f"Customer: {customer_name}",
        "----------------------------------------"
    ]
    
    for item in cart:
        receipt_lines.append(
            f"{item['name']} (x{item['qty']}) : {item['total']:.2f} AED"
        )
        
    receipt_lines.extend([
        "----------------------------------------",
        f"Subtotal       : {subtotal:.2f} AED",
        f"Discount (10%) : -{discount:.2f} AED",
        f"UAE VAT (5%)   : +{vat:.2f} AED",
        f"GRAND TOTAL    : {total:.2f} AED",
        "========================================\n"
    ])
    
    receipt_text = "\n".join(receipt_lines)
    print(receipt_text)
    
    # Save daily sales log to a text file
    with open("daily_sales_log.txt", "a") as file:
        file.write(receipt_text)
    print("Receipt saved to 'daily_sales_log.txt'.")


def main():
    print("Welcome to UAE Automated Billing System")
    customer_name = input("Enter Customer Name: ").strip() or "Walk-in Customer"
    cart = []
    
    while True:
        display_menu()
        choice = input("Enter item number to add (or 'done' to checkout): ").strip().lower()
        
        if choice == "done":
            break
        elif choice in menu:
            try:
                qty = int(input(f"Enter quantity for {menu[choice]['name']}: "))
                if qty <= 0:
                    print("Quantity must be at least 1.")
                    continue
                item_total = menu[choice]["price"] * qty
                cart.append({
                    "name": menu[choice]["name"],
                    "qty": qty,
                    "total": item_total
                })
                print(f"Added {qty} x {menu[choice]['name']} to cart.")
            except ValueError:
                print("Invalid input. Please enter a valid number for quantity.")
        else:
            print("Invalid selection. Please choose a valid item number.")
            
    if not cart:
        print("Cart is empty. Exiting billing system.")
        return
        
    subtotal, discount, vat, total = calculate_bill(cart)
    print_and_save_receipt(customer_name, cart, subtotal, discount, vat, total)


if __name__ == "__main__":
    main()