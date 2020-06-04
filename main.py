#!/usr/bin/env python
import os
import time
import random
while True:
    try: 
        from plyer import notification
        break
    except:
        import dependencies
s = str(os.getpid())
print(s)
if __name__ == "__main__":
    quotes = [
        """Drinking water is like washing out your insides. The water will cleanse the system, fill you up, decrease your caloric load and improve the function of all your tissues.\n\t - Kevin R. Stone
        """
        ,
        """If there is magic on this planet, it is contained in water.\n\t - Loren Eiseley
        """
        ,
        """Water is life's matter and matrix, mother and medium. There is no life without water.\n\t - Albert Szent-Gyorgyi
        """
        ,
        """I believe that water is the only drink for a wise man.\n\t - Henry David Thoreau
        """
        ,
        """In time and with water, everything changes.\n\t - Leonardo da Vinci
        """
        ,
        """Thousands have lived without love, not one without water.\n\t - W. H. Auden
        """
        ,
        """
        We forget that the water cycle and the life cycle are one.\n\t - Jacques Yves Cousteau
        """
        ,
        """Wanna lose 1200 Calories a month? Drink a liter of ice water a day. You burn the energy just raising the water to body temp.\n\t - Neil deGrasse Tyson
        """
        ,
        """Drinking water is like washing out your insides. The water will cleanse the system, fill you up, decrease your caloric load and improve the function of all your tissues.\n\t - Kevin R. Stone
        """
        ,
        """Drinking water is essential to a healthy lifestyle.\n\t - Stephen Curry
        """
        ,
        """If you have forest, if you have green forest, the water table goes up. What happens with deforestation is the water level goes down and we all know how much importance drinking water has.\n\t - MS Dhoni
        """
        ,
        """I try to start drinking water as soon as my feet hit the floor in the morning.\n\t - Mary Kay Andrews
        """
        ,
        """Thousands have lived without love, not one without water.\n\t - Rohit Vishwakarma
        """
    ]
    watercall = [
        """Please Drink Water now !\n""",
        """Time for some H₂O \n""" ,
        """🚰 time !!"""
    ]
    import platform
    mypath = os.getcwd()+'/'+"water.svg"
    if(platform.system() == 'Windows'):
        mypath = os.getcwd()+"\\"+"water.svg"
    while True:
        notification.notify(
            title = random.choice(watercall),
            message = random.choice(quotes),
            app_icon = mypath,
            timeout = 15
        )
        time.sleep(60)
