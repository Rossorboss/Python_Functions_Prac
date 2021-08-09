#User picks nation
ship_list_rn = ('HMS Lion', 'HMS Tiger', 'HMS Inflexible', 'HMS Indefatigable', 'HMS Indomitable', 'HMS Invincible', 'HMS Queen Mary', 'HMS New Zealand', 'HMS Princess Royal')
ship_list_hsf =('SMS Lutzow', 'SMS Derffliner', 'SMS Moltke', 'SMS Von der Tann', 'SMS Seydlitz')

ship_dict_rn = {'Name':'HMS Lion', 'Class': 'Lion Class', 'Squadron': '1st Battlecruiser Squadron',  'Guns': '8 x 13.5"/45', 'Jutland outcome': 'Damaged'}, {'Name':'HMS Tiger', 'Class': 'Tiger (Lion Subclass)', 'Squadron': '1st Battlecruiser Squadron',  'Guns': '8 x 13.5"/45', 'Jutland outcome': 'Damaged'}, {'Name':'HMS Inflexible', 'Class': 'Invincible Class', 'Squadron': '3rd Battlecruiser Squadron',  'Guns': '8 x 12"/45', 'Jutland outcome': 'Not damaged'}, {'Name':'HMS Indefatigable', 'Class': 'Indefatigable Class','Squadron': '1st Battlecruiser Squadron',  'Guns': '8 x 12"/45', 'Jutland outcome': 'Sunk during run to the South'}, {'Name':'HMS Indomitable', 'Class': 'Invincible Class', 'Squadron': '3rd Battlecruiser Squadron',  'Guns': '8 x 12"/45', 'Jutland outcome': 'Not damaged'}, {'Name':'HMS Invincible', 'Class': 'Invincible Class','Squadron': '3rd Battlecruiser Squadron',  'Guns': '8 x 12"/45', 'Jutland outcome': 'Sunk during the main engagment'}, {'Name':'HMS Queen Mary', 'Class': 'Queen Mary (Lion Subclass)', 'Squadron': '1st Battlecruiser Squadron',  'Guns': '8 x 13.5"/45', 'Jutland outcom': 'Sunk during the run to the South'}, {'Name':'HMS New Zealand', 'Class': 'Indefatigable Class', 'Squadron': '1st Battlecruiser Squadron',  'Guns': '8 x 12"/45', 'Jutland outcome': 'Lightly Damaged'}, {'Name':'HMS Princess Royal', 'Class': 'Lion Class', 'Squadron': '1st Battlecruiser Squadron',  'Guns': '8 x 13.5"/45', 'Jutland outcom2': 'Damaged'}
ship_dict_hsf ={'Name':'SMS Lutzow', 'Class': 'Derfflinger Class', 'Squadron': '1st Scouting Group',  'Guns': '8 x 12"/50', 'Jutland outcome': 'Sunk'},{'Name':'SMS Derfflinger', 'Class': 'Derfflinger Class', 'Squadron': '1st Scouting Group',  'Guns': '8 x 12"/50', 'Jutland outcome': 'Heavily Damaged'}, {'Name':'SMS Moltke', 'Class': 'Moltke Class', 'Squadron': '1st Scouting Group',  'Guns': '10 x 11"/50', 'Jutland outcome': 'Damaged'}, {'Name':'SMS Von der Tann', 'Class': 'Von der Tann', 'Squadron': '1st Scouting Group',  'Guns': '8 x 11"/45', 'Jutland outcome': 'Heavily Damaged'}, {'Name':'SMS Seydlitz', 'Class': 'Seydlitz', 'Squadron': '1st Scouting Group',  'Guns': '10 x 11"/50', 'Jutland outcome': ' Very Heavily Damaged'}



def battlecruisers():
    side = ''
    while side != 'British' and side != 'German':
        side = input('please choose British or German: ')
    if side == 'British':
        print(ship_list_rn[0])
        print(ship_list_rn[1])
        print(ship_list_rn[2])
        print(ship_list_rn[3])
        print(ship_list_rn[4])
        print(ship_list_rn[5])
        print(ship_list_rn[6])
        print(ship_list_rn[7])
        print(ship_list_rn[8])
    else:
        print(ship_list_hsf[0])
        print(ship_list_hsf[1])
        print(ship_list_hsf[2])
        print(ship_list_hsf[3])
        print(ship_list_hsf[4])


        
    choose_ship = input('Select the ship you would like more detials on: ')
    if choose_ship == (ship_list_rn[0]):
        print(ship_dict_rn[0])
        choose_ship = input('Select the ship you would like more detials on: ')
    if choose_ship == (ship_list_rn[1]):
        print(ship_dict_rn[1])
    if choose_ship == (ship_list_rn[2]):
        print(ship_dict_rn[2])
    if choose_ship == (ship_list_rn[3]):
        print(ship_dict_rn[3])
    if choose_ship == (ship_list_rn[4]):
        print(ship_dict_rn[4])
    if choose_ship == (ship_list_rn[5]):
        print(ship_dict_rn[5])
    if choose_ship == (ship_list_rn[6]):
        print(ship_dict_rn[6])
    if choose_ship == (ship_list_rn[7]):
        print(ship_dict_rn[7])
    if choose_ship == (ship_list_rn[8]):
        print(ship_dict_rn[8])
    if choose_ship ==(ship_list_hsf[0]):
        print(ship_dict_hsf[0])
    if choose_ship ==(ship_list_hsf[1]):
        print(ship_dict_hsf[1])
    if choose_ship ==(ship_list_hsf[2]):
        print(ship_dict_hsf[2])
    if choose_ship ==(ship_list_hsf[3]):
        print(ship_dict_hsf[3])
    if choose_ship ==(ship_list_hsf[4]):
        print(ship_dict_hsf[4])
            
    

battlecruisers()





        