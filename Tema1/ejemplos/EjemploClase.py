grades = {}
for i in range(3):
    nombre = input("Nombre del alumno: ")
    ma = float(input("Nota de Matemáticas: "))
    en = float(input("Nota de Inglés: "))
    fr = float(input("Nota de Francés: "))
    grades[nombre] = {
        "Ma": ma,
        "En": en,
        "Fr": fr
        }
print(grades)