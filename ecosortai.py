# ============================================
#             ECO SORT AI 
#      AI-Based Waste Classification System
# ============================================

import random

print("=" * 50)
print("          🌱 ECO SORT AI ")
print("     Smart Waste Classification System")
print("=" * 50)

# Waste database
waste_data = {
    "plastic bottle": ("Recyclable", "♻️", "Put it in the recycling bin."),
    "plastic bag": ("Recyclable", "♻️", "Reuse it if possible or place it in the recycling bin."),
    "paper": ("Recyclable", "📄", "Put it in the paper recycling bin."),
    "cardboard": ("Recyclable", "📦", "Flatten it and place it in recycling."),
    "glass bottle": ("Recyclable", "🍾", "Place it carefully in the glass recycling bin."),
    
    "banana peel": ("Organic", "🍌", "Put it in the compost/organic waste bin."),
    "vegetable waste": ("Organic", "🥦", "Use it for composting."),
    "food waste": ("Organic", "🍎", "Put it in the organic waste bin."),
    "leaves": ("Organic", "🍂", "Compost it if possible."),
    
    "battery": ("Hazardous", "🔋", "Take it to an authorized battery collection point."),
    "paint": ("Hazardous", "🎨", "Do not pour it into drains. Use a hazardous-waste facility."),
    "medicine": ("Hazardous", "💊", "Return unused medicine to an appropriate collection point."),
    
    "diaper": ("General Waste", "🗑️", "Place it in the general waste bin."),
    "tissue": ("General Waste", "🧻", "Place it in general waste."),
    "broken sponge": ("General Waste", "🧽", "Place it in general waste.")
}

# Statistics
statistics = {
    "Recyclable": 0,
    "Organic": 0,
    "Hazardous": 0,
    "General Waste": 0
}

def classify_waste(item):

    item = item.lower().strip()

    if item in waste_data:
        category, emoji, advice = waste_data[item]

        print("\n AI ANALYSIS...")
        print("Item      :", item.title())
        print("Category  :", emoji, category)
        print("Advice    :", advice)

        statistics[category] += 1

    else:
        print("\n AI is not sure about this item.")
        print("Try entering a common waste item such as:")
        print("plastic bottle, banana peel, battery, paper...")

def show_statistics():

    print("\n" + "=" * 50)
    print("            ECO IMPACT REPORT")
    print("=" * 50)

    total = sum(statistics.values())

    if total == 0:
        print("No waste has been analyzed yet.")
        return

    for category, count in statistics.items():
        percentage = (count / total) * 100
        print(f"{category:15} : {count} ({percentage:.1f}%)")

    recyclable = statistics["Recyclable"]

    print("\n Environmental Insight:")

    if recyclable > 0:
        print(" Great! You identified recyclable waste.")
    
    if statistics["Organic"] > 0:
        print(" Organic waste can be converted into compost.")

    if statistics["Hazardous"] > 0:
        print(" Hazardous waste needs special handling.")

    print("\nTotal items analyzed:", total)


# Main program
while True:

    print("\n--------------------------------------------")
    print("1️  Analyze Waste")
    print("2️  View Eco Impact Report")
    print("3️  Exit")
    print("--------------------------------------------")

    choice = input("Choose an option: ")

    if choice == "1":

        item = input("\n Enter the waste item: ")
        classify_waste(item)

    elif choice == "2":

        show_statistics()

    elif choice == "3":

        print("\n Thank you for using ECO SORT AI!")
        print("Small actions → Big environmental impact 🌱")
        break

    else:

        print("❌ Invalid choice. Please try again.")