#Ask the user to input the current weather from a predefined set of conditions: sunny, rainy, or cold.
Wether_conditions = input("What's the weather like today? (sunny/rainy/cold): ")

if Wether_conditions == "sunny":
    print("Wear a t-shirt and sunglasses")
elif Wether_conditions == "rainy":
    print("Don't forget your umbrella and a raincoat")
elif Wether_conditions == "cold":
    print("Make sure to wear a warm coat and a scarf")
else:
    print("Sorry, I don't have recommendations for this weather")


