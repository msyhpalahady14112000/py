class Pecahan:
 
    def __init__(abc,atas,bawah):
        abc.pembilang = atas
        abc.penyebut = bawah
    
    def __str__(abc):
        return str(abc.pembilang)+"/"+str(abc.penyebut)
p = Pecahan(3,5)
 
del p.pembilang
print(p1.pembilang)