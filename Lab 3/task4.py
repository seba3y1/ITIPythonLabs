import json

def  products_task():
    while True:
        names = input("Enter product names with comma-separated: ").strip().split(",")
        names = [n.strip() for n in names if n.strip()]
        if names:
            break
        print("invalid input ,try again")

    while True:
        try:
            prices = [float(x) for x in input("Enter prices with comma-separated : ").split(",")]
            if len(prices) == len(names):
                break
            else:
                print(" must match number of names")
        except ValueError:
            print("invalid numbers, try again")

    paired = list(zip(names, prices))
    filtered = filter(lambda x: x[1] > 0, paired)
    transformed = list(map(lambda x: {"product": x[0], "price": x[1], "discounted": round(x[1]*0.9, 2)}, filtered))

    with open("products.json", "w") as file:
        json.dump(transformed, file, indent=4)

    print("products.json created")
    print(transformed[:5])