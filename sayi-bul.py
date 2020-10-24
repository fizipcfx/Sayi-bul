import tkinter as tk
from random import randrange
from tkinter import messagebox as msgbox
from functools import partial

#LEFT = "<Button-3>"

SIZE = 9 or int(input("Büyüklüğünü giriniz: "))
tahmin_number = 7 or int(input("Kaç tahmin olsun: "))


class Saybul(tk.Tk):
    def __init__(self):
        super().__init__()

        self.resizable(False, False)
        self.title("Sayıyı bul")
        # --------------------------------------
        self.game_frame = tk.Frame(self)
        self.game_frame.pack()
        self.TNumber = self.TheNumber()
        self.tahmin = tahmin_number
        self.txt = tk.Label(self, text=f"Sayıyı bulun     |     Kalan tahmin hakkınız: {self.tahmin}")
        self.txt.pack()

        for i in range(pow(SIZE, 2)):
            sayi = str(i + 1)
            row = i // SIZE
            column = i % SIZE
            num = "  "+sayi if len(sayi) == 1 else sayi
            exec(f"self.button{sayi} = tk.Button(self.game_frame,bg='white', command=partial(self.check,{sayi}), text='{num}')")
            eval(f"self.button{sayi}.grid(row={row},column={column})")

    def check(self, numb):
        if self.TNumber == numb:
            # win
            exec(f"self.button{numb}['bg'] = 'green'")
            res = self.ask(True)
            if res:
                self.clear()
            else:
                self.quit()

        elif self.TNumber > numb:
            # pick bigger number
            self.tahmin -= 1
            exec(f"self.button{numb}['bg'] = 'red'")
            self.txt["text"] = f"Sayıyı büyültün  |     Kalan tahmin hakkınız: {self.tahmin}"
            if self.tahmin == 0:
                res = self.ask(False)
                if res:
                    self.clear()

                else:
                    self.quit()

        elif self.TNumber < numb:
            # pick smaller number
            self.tahmin -= 1
            exec(f"self.button{numb}['bg'] = 'red'")
            self.txt["text"] = f"Sayıyı küçültün  |     Kalan tahmin hakkınız: {self.tahmin}"
            if self.tahmin == 0:
                res = self.ask(False)
                if res:
                    self.clear()

                else:
                    self.quit()

    def ask(self, tf):
        msg = "Kazandınız, Yeniden oyna?" if tf else f"Kaybettiniz, sayı {self.TNumber} idi, Yeniden oyna?"
        return msgbox.askyesno("Oyun Bitti", msg)

    def TheNumber (self):
        return randrange(1, 82)

    def clear(self):
        self.tahmin = tahmin_number
        self.txt["text"] = f"Sayıyı bulun     |     Kalan tahmin hakkınız: {self.tahmin}"
        self.TNumber = self.TheNumber()
        for i in range(81):
            sa = i +1
            exec(f"self.button{sa}['bg'] = 'white'")


oyun = Saybul()

oyun.mainloop()
