import pandas as pd

# data = [100, 300, 490]
# ----------------- Series -----------------
# series = pd.Series(data, index=['a', 'b', 'c'])
# print(series)

# series.loc['b'] = 1293
# print(series.loc['b'])
# print(series.iloc[0])
# print(series[series >= 500])

# ----------------- DataFrame -----------------
# s = pd.Series({'Alice': 25, 'Bob': 30, 'Charlie': 35})
# print(s)

# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
#     'Age': [25, 30, 35, 28],
#     'City': ['New York', 'London', 'Tokyo', 'Paris'],
#     'Salary': [50000, 60000, 70000, 55000]
# }

# df = pd.DataFrame(data)  # Create DataFrame
# print(df)                # Display DataFrame

# ---- Selection ----
# print(df['Name'])        # Select Name column
# print(df['Age'])         # Select Age column
# print(df[['Name', 'Salary']])  # Select multiple columns
# print(df.iloc[0])        # Select first row
# print(df.iloc[1:3])      # Select rows 2 to 3

# ---- Add new column ----
# df['Bonus'] = df['Salary'] * 0.10

# ---- Update Salary ----
# df['Salary'] = df['Salary'] + 5000
# print(df)

# ------------- Basic Attributes --------------
# print(df.shape)            # Display rows and columns
# print(df.columns)           # Display column names
# print(df.dtypes)            # Display data types
# print(df.describe())        # Display statistics

# new_row = pd.DataFrame([{'Name' : 'Fardin',
#                          'Age' : 21,
#                          'City' : 'Dhaka',
#                          'Salary' : 0,
#                          'Bonus' : 0}])
#
# df = pd.concat([df, new_row])
# print(df)

# ------------ Reading file -------------
df = pd.read_csv("data.csv", index_col="Name")
# print(df.to_string())

# ---- Selection by columns ----
# print(df["Name"])
# print(df["Height"])

# ---- Selection by rows ----
# print(df.loc["Pikachu"])
# print(df.loc["Charizard" : "Blastoise", ["No", "Height", "Weight"]])
# print(df.iloc[1:20:3, 1:4])

# ---- Exercise ----
# pokemon = input("Enter Pokemon Name: ")
# try:
#     print(df.loc[pokemon])
# except KeyError:
#     print(f"{pokemon} does not exist!")

# ---- Filtering ----
# tall_pokemon = df[df["Height"] >= 2][["Type1", "Height"]] # Filter height >= 2, then select columns
# print(tall_pokemon)

# legendary_pokemon = df[df["Legendary"] == 1].index.tolist()  # Get names as a list
# print(legendary_pokemon)

# water_niggas = df[(df["Type1"] == "Water") | (df["Type2"] == "Water")]
# print(water_niggas)

# ---------------- Aggregation -----------------
# print(df.mean(numeric_only=True)) # Whole Dataframe
# print(df["Height"].sum()) # Single Column
# print(df.min(numeric_only=True))
# print(df.max(numeric_only=True))
# print(df.count())
# print(df['Weight'].value_counts()) # Shows count of most common values

# ---- Grouping ----
# group = df.groupby("Type1")
# print(group["Weight"].mean())

# ---------------- Data Cleaning ----------------
# 1. Drop irrelevant columns
# df = df.drop(columns=["No"])

# 2. Handle missing data
# df = df.dropna(subset=["Type2"]) # drop datas if not available (na)
# df = df.fillna({"Type2" : "Sure"}) # fill datas if not available (na)

# 3. Fix inconsistent values
# df["Type1"] = df["Type1"].replace({"Grass" : "Shobuj",
#                                    "Water" : "Pani"})

# 4. Standardize text
# df["Type1"] = df["Type1"].str.upper()

# 5. Fix data types
# df["Legendary"] = df["Legendary"].astype(bool)

# 6. Remove duplicates
# df = df.drop_duplicates()

# print(df.to_string())
