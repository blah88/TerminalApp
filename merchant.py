def store(items):
    print("""
To sell item(s) type sell 'item_name'.
To buy type buy 'item_name'.
To exit the store type 'exit'.
""")

    print(f"""
    buy                 price

    fruit               2
    mushroom            10
    hatchet             20
    armour              50
    machete             100
    mysterious object   1000

    sell

    {items}
    
    """)

