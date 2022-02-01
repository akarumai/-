def h(n,pin1,pin2):
    if n==1:
        print(f"Переложить диск 1 со стержня {pin1} на {pin2}")
    else:
        h(n - 1, pin1,6 - pin1 - pin2)
        print(f"Переложить диск {n} со стержня {pin1} на {pin2}")
        h(n - 1,6 - pin1 - pin2, pin2)

n = int(input("Кол-во дисков\n"))
h(n,1,2)
