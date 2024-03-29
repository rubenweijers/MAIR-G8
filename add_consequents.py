import pandas as pd


def touristic(price, food):
    """Return True if the restaurant is touristic, False otherwise."""
    if price == "cheap":
        return True
    elif price == "moderate" and food == "good":
        return True
    else:
        return False


def assigned_seats(crowdedness):
    """Return True if the restaurant has assigned seats, False otherwise."""
    if crowdedness == 'busy':
        return True
    return False


def child_friendly(stay):
    """Return True if the restaurant is child friendly, False otherwise."""
    if stay == "short":
        return True
    else:
        return False


def romantic(stay, crowdedness):
    """Return True if the restaurant is romantic, False otherwise."""
    if stay == "long" and crowdedness == "not busy":
        return True
    elif stay == "long" and crowdedness == "not busy":
        return True
    else:
        return False


def add_rules(dataframe):
    """Add 3 columns based on handwritten rules for if the restaurant is romantic, touristic and child friendly."""
    t, c, r, a = [], [], [], []
    for _, row in dataframe.iterrows():
        t.append(touristic(row["pricerange"], row["foodquality"]))
        c.append(child_friendly(row["lengthofstay"]))
        r.append(romantic(row["lengthofstay"], row["crowdedness"]))
        a.append(assigned_seats(row['crowdedness']))
    dataframe = dataframe.assign(touristic=t, child_friendly=c, romantic=r, assigned_seats=a)
    return (dataframe)


if __name__ == "__main__":
    # Add consequents and add to restaurant_data csv file
    df = pd.read_csv("./data/restaurant_data.csv")
    df_add = add_rules(df)
    df_add.to_csv("./data/restaurant_data_consequents.csv")

    # Check if there are romantic restaurants
    print(df_add.loc[(df_add["romantic"])])
