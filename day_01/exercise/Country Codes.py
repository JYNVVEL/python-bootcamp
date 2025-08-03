country_codes = {
                "PH" : "Philippines",
                "US" : "United States",
                "UK" : "United Kingdom",
                "EU" : "Europe"
                }

print("Countries")
for key, value in country_codes.items():
    print("\t", key, value)

country_code = input("Enter country code: ").upper()

print(f"{country_codes} \n{country_codes.get(country_code, "Unkown")}")

