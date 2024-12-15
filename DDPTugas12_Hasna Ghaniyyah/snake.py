from animal import Animal

class Snake(Animal):
    #Konstruktor Properti
    def __init__(self, nama, makanan, hidup, berkembangBiak, berbisa, habitat):
        super().__init__(nama, makanan, hidup, berkembangBiak)
        self.bisa = berbisa
        self.habitat = habitat

    #Method
    def infoSnake(self):
        super().infoAnimal()
        print('Jenis Bisa Ular\t\t: ', self.bisa, '\nHabitat\t\t\t: ', self.habitat)

#Objek
print('---Info Snake---')
snake = Snake('Ular Kobra', "Daging", "Darat", "Bertelur", "Beracun", "Hutan\n")
snake.infoSnake()
snake = Snake('Ular Sanca', "Daging", "Darat", "Bertelur", "Tidak memiliki bisa", "Hutan tropis yang lembab\n")
snake.infoSnake()
snake = Snake('Ular Sawah', "Daging", "Darat", "Bertelur", "Tidak memiliki bisa", "Sawah")
snake.infoSnake()