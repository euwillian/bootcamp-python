from random import randint
dice_images = [1,2,3,4,5,6]
dice_num = randint(1, 6) 
# o erro neste caso ocorre pois, quando randint for 6, nao existe este numero na lista dice_images
# outro erro também ocorre pois a lista inicia do zero, e neste caso o randint() inicia do 1, logo o dado com numero 1 nunca irá cair pois, precisaria ser dice_images[0]
# melhor forma = randint(0, 5)
print(dice_num)
print(dice_images[dice_num])


# correcao:

from random import randint
dice_images = [1,2,3,4,5,6]
dice_num = randint(0, 5) 
print(dice_num)
print(dice_images[dice_num])