class MoneyFmt:
    def __init__(self, value):
        self.value = value

    def _repr(self):
        ostatok = "00"
        r = ""
        l = -1
        for i in str(self.value):
            l += 1
            if i == ".":
                ostatok = round(self.value, 3)
                ostatok = str(ostatok)[-2:]
                break
            
            elif l == 3:
                r += ","
                r += i
                l = 0
            else:
                r += i
        return f"${r}.{ostatok}"


    def __str__(self):
        return self._repr()


    def update(self, val):
        self.value = val
        return self._repr() 

god = MoneyFmt(1225456452254.2254)
print(god)
p = float(input("Update value:  "))
print(god.update(p))
