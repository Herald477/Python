def CalculateDamage(ATK, DEF, ATKtype, DEFtype):
    effective = 0

    ATKtype = input("ATTACK TYPE -:- Fire-Water-Grass-Electric: ").lower()
    DEFtype = input("DEFENSE TYPE -:- Fire-Water-Grass-Electric: ").lower()

    
    if ATKtype == "fire":
        if DEFtype == "grass":
            effective = 2
        if DEFtype == "electric":
            effective = 1
        if DEFtype == "water":
            effective = 0.5
        if DEFtype == ATKtype:
            effective = 1

    if ATKtype == "water":
        if DEFtype == "grass":
            effective = 0.5
        if DEFtype == "electric":
            effective = 0.5
        if DEFtype == "fire":
            effective = 2
        if DEFtype == ATKtype:
            effective = 1

    if ATKtype == "grass":
        if DEFtype == "water":
            effective = 2
        if DEFtype == "fire":
            effective = 0.5
        if DEFtype == "electric":
            effective = 1
        if DEFtype == ATKtype:
            effective = 1

    if ATKtype == "electric":
        if DEFtype == "water":
            effective = 2
        if DEFtype == "grass":
            effective = 1
        if DEFtype == "fire":
            effective = 1
        if DEFtype == ATKtype:
            effective = 1