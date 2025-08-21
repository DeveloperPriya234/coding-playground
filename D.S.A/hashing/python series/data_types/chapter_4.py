is_boiling = True # note : true is 1 and false is consider as 0
stri_count = 5
total_actions = stri_count + is_boiling # upcasting
print(f"total actions:{total_actions}")


milk_presents = None# no milk
print(f"is there milk?{bool(milk_presents)}")

milk_presents = 0# no milk
print(f"is there milk : {bool(milk_presents)}")

water_hot = True
tea_added = False
can_server = water_hot and tea_added
print(f"can serve chai? {bool(can_server)}")


water_hot = True
tea_added = True
can_server = water_hot and tea_added
print(f"can serve chaii?{can_server}")


water_hot = True
tea_added = False
can_server = water_hot or tea_added
print(f"can serve chaii?{can_server}")