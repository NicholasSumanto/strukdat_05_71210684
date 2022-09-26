class Mobil:
    _merk=""
    _tipe=""
    _jenisBahanBakar=""
    _kapasitasBBM=""
    

    def __init__(self,Merk,Tipe):
        self._merk = Merk
        self._tipe = Tipe
        self._jenisBahanBakar = None
        self._kapasitasBBM = None

    def setJenisBahanBakar(self,jenisBahanBakar):
        self._jenisBahanBakar = jenisBahanBakar
    
    def setKapasitasBBM(self,kapasitasBBM):
        self._kapasitasBBM = kapasitasBBM
    
    def getMerk(self):
        return self._merk
    
    def getTipe(self):
        return self._tipe 

    def getJenisBahanBakar(self):
        return self._jenisBahanBakar
    
    def getkapasitasBBM (self):
        return self._kapasitasBBM


    def printInfo(self):
        print("="*12,"INFO","="*12)
        print("Merk             :",self.getMerk())
        print("Tipe             :",self.getTipe())
        print("Bahan Bakar      :",self.getJenisBahanBakar())
        print("Kapasitas BBM    :",self.getkapasitasBBM())

    def isiBBM(self,harga):
        if self.getkapasitasBBM() == None or self.getJenisBahanBakar() == None :
            print("ERROR! kapasitas BBM atau Jenis Bajan Bakar belum di inputkan")
        else :
            print("mengisi",self.getkapasitasBBM(),"Liter")
            jumlah = self.getkapasitasBBM()*harga
            print("Total Harga",jumlah)




if __name__ == "__main__": 
    mobil1 = Mobil("Toyota", "Avanza") 
    mobil1.printInfo() 

    mobil2 = Mobil("Nissan", "Grand Livina") 
    mobil2.setJenisBahanBakar("Bensin") 
    mobil2.setKapasitasBBM(20) 
    mobil2.printInfo() 

    mobil1.isiBBM(14500) 
    mobil2.isiBBM(14500)
