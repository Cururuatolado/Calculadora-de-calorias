def grau_atv(atv_fisica):
    if atv_fisica <= 0:
        return "sedentário"
    elif 1 <= atv_fisica <= 2.9:
        return "levemente ativo"
    elif 3 <= atv_fisica <= 5:
        return "moderadamente ativo"
    elif 6 <= atv_fisica <= 7:
        return "muito ativo"

def GEDT():
    peso = int(input('Peso (kg): '))
    altura = float(input('Altura (cm): '))
    idade = int(input('Idade: '))
    atv_fisica = float(input('Quantos dias você pratica exercício por semana? '))
    dieta = int(input('Dieta (digite 1 para emagrecer, 2 para aumentar, 3 para manter o peso): '))
    grau = grau_atv(atv_fisica)
    
    tmb = 66 + (13.8 * peso) + (5 * altura) - (6.8 * idade)
    total_gasto = 0
    if grau == 'sedentário':
        total_gasto = tmb * 1.2
    elif grau == 'levemente ativo':
        total_gasto = tmb * 1.375
    elif grau == 'moderadamente ativo':
        total_gasto = tmb* 1.55
    elif grau == 'muito ativo':
        total_gasto = tmb* 1.725
        
    if dieta == 1:
         return f'você gasta {total_gasto:.2f} Kcal por dia. para seguir a dieta você deve consumir entre {total_gasto - 500:.2f} e {total_gasto - 1000:.2f} Kcal por dia para emagrecer'
    if dieta == 2:
         return f'você gasta {total_gasto:.2f} Kcal por dia. para seguir na dieta você deve consumir entre {total_gasto+250:.2f} e {total_gasto+500:.2f} Kcal por dia para aumentar'
    if dieta == 3:   
        return f'você gasta {total_gasto:.2f} Kcal por dia. para seguir na dieta você deve consumir {total_gasto:.2f} Kcal para manter o peso.'

resultado = GEDT()
print(resultado)