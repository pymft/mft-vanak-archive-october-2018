def division(a, b):
    try:
        return a / b
    except:
        print("ERROR")
    finally:
        print("Finally")


print(division(1,2))