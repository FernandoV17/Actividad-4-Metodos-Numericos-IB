def header():
    print("##########################################################################")
    print("# PIA: Resolución de Ecuación Diferencial por método de Euler           #")
    print("##########################################################################\n")
    print("\n")
    print("Métodos Numéricos: AD2024")
    print("\n")
    print("Integrantes:")
    print("Fernando Villarreal Castillo 2049219")   
    print("Julio Alejandro Galindo Estrada 1945686")    
    print("Oscar Eduardo Reyes Pereyra  2109292")  
    print("\n")

def metodo_euler(a, b, N, c0):
    h = (b - a) / N
    x = a
    w = c0

    for i in range(1, N + 1):
        w = w + h * (-0.02 * w)
        x = x + h
        print(f"x = {x:.2f} \tf(x) = {w:.6f}")

if __name__ == "__main__":
    header()
    print("Aproximación por método de Euler\n")
    metodo_euler(0, 30, 100, 1000)
