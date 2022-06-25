counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")
    if "Arapahoe" in counties or "El Paso" in counties:
        print("Arapahoe or El Paso are in the list of counties.")
    else:
        print("Arapahoe or El Paso is not in the list of counties.")    


        for county in counties_dict.keys():
            print(county)

            for i in range(len(counties)):
                print(counties[i])
                counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")