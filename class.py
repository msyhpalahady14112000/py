class user:
    def __init__(self, username, Password):
        self.username=username
        self.password=Password

    def setusername(self, username):
        self.username=username

    def setpassword(self, password):
        self.password=password

    def getusername (self):
        return username
    def getpassword (self): 
        return password

    def login():
        usr=input("input username =")
        pwd=input("input password =")
        a=user(usr , pwd)
        if(usr== 'admin' and pwd== 'admin'):
            print(f'selamat datang{usr}')
            pilih()
        else:
            print("belum nyampe....")
    def pilih():
        print("=================pilih menu==============")
        x =int(input("masukan pilihan"))
        if x == 1:
            print("hitung penjumlahan")
        elif x == 2:
            print("bangun datar")
        elif x == 3:
            print("algoritma")
        else:
            print("silahkan pilih  menu")
            login()

    if (__name__=="__main__"):
        login()