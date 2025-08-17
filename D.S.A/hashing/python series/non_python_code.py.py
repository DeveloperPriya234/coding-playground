def make_chai():
    if not kettle_has_water():
        fill_kittle()
    plug_in_kettle()
    boil_water()
    if not is_cup_clean():
        wash_cup()
        