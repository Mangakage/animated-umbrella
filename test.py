# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random as rd
def random_3d6():
    d1 = rd.randint(1,6)
    d2 = rd.randint(1,6)
    d3 = rd.randint(1,6)
    d4 = rd.randint(1,6)
    d5 = rd.randint(1,6)
    rolls = [d1, d2, d3, d4, d5]
    rolls.sort(reverse=True)
    stat = sum(rolls[0:3])
    return stat

strength = random_3d6()
dexterity = random_3d6()
constitution = random_3d6()
intelligence = random_3d6()
wisdom = random_3d6()
charisma = random_3d6()

print(f"""
       Str = {strength}
       Dex = {dexterity}
       Con = {constitution}
       Int = {intelligence}
       Wis = {wisdom}
       Cha = {charisma}
       """)