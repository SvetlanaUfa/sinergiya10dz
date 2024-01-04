pets = {} #объявляем пустой словарь
pet_name = input("Введите имя питомца: ")
pet_species = input("Введите вид питомца: ")
pet_age = int(input("Введите возраст питомца: "))
owner_name = input("Введите имя владельца: ")
pets[pet_name] = {
    "Вид питомца": pet_species,
    "Возраст питомца": pet_age,
    "Имя владельца": owner_name
}
print("Словарь успешно создан!")
print(pets.values())
print("Это (pet_species) по кличке "{pet_name})""