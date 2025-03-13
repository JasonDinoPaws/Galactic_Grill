# import pandas as pd
# menu = pd.read_csv('menu.csv')
# print(menu.to_string(index=False))

m = [[8, 'Lunar Garlic Rolls', 'Starters', '"Soft'], [8, 'Saturn’s Rings', 'Starters', '"Golden-fried onion rings stacked high'], [30, 'Nebula Ribeye', 'Main Courses', '"A 12oz flame-grilled ribeye steak'], [26, 'Solar Flare Salmon', 'Main Courses', '"Honey-glazed salmon with a side of comet rice and sautéed cosmic vegetables."'], [22, 'Black Hole Pasta', 'Main Courses', '"Squid ink pasta in a creamy garlic sauce with grilled shrimp and a sprinkle of stardust parmesan."'], [18, 'Planetary Power Bowl (Vegan)', 'Main Courses', '"Quinoa'], [10, 'Supernova Chocolate Cake', 'Desserts', '"Rich chocolate cake with a molten caramel core'], [9, 'Milky Way Cheesecake', 'Desserts', '"Classic New York cheesecake with a swirl of dark matter chocolate sauce."'], [8, 'Zero-Gravity Churros', 'Desserts', '"Cinnamon-dusted churros with a dark chocolate and caramel dipping duo."'], [6, 'Celestial Lemonade', 'Drinks', '"Freshly squeezed lemonade infused with cosmic berry syrup."'], [7, 'Rocket Fuel Espresso', 'Drinks', '"Bold espresso with steamed milk and a hint of caramel orbit."']]
x=1
tmp = ""
for i in m:
    if i[2] != tmp:
        tmp = i[2]
        print(f"\n{i[2]}")
    print(f"\n{x}: ${i[0]} {i[1]}")
    desc = i[3].replace("\"","")
    print(desc)
    x+=1