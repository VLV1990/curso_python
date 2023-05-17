pizza_vegetariana = ['pimiento', 'tofu']
pizza_nor = ['peperoni', 'jamon', 'salmon']
base_pizza = ['tomate', 'mozarella']

tipo_pizza = str(input("Qué tipo de pizza quieres? (vegetariana/normal): "))

if tipo_pizza == "vegetariana":
    print(pizza_vegetariana)
    ingrediente = str(input("Qué ingrediente vegetariano desea?: "))
else:
    print(pizza_nor)
    ingrediente = str(input("Qué ingrediente normal desea?: "))

print(f"tu pizza tiene como base {base_pizza} y un agregado de {ingrediente}")