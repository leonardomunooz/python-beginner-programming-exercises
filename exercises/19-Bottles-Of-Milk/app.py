# ✅↓ Write your code here ↓✅
def number_of_bottles():
    decremento = range(10 -1,-1,-1)
    for  repeticiones in decremento:
        if repeticiones == 0:
           print(f"""
            No more bottles of milk on the wall, no more bottles of milk.
            Go to the store and buy some more, 99 bottles of milk on the wall.
                 """)
        else:
             print(f"""
              {repeticiones} bottles of milk on the wall, {repeticiones} bottles of milk.
             Take one down and pass it around, {repeticiones - 1} bottles of milk on the wall.
              """ )

        


number_of_bottles()