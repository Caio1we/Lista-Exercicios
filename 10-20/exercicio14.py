# 14. Leia duas notas e informe se o aluno foi aprovado (média ≥ 7).

nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print(f"Sua média foi {media}, você foi aprovado")
else:
    print(f"Sua média foi {media}, você foi reprovado")
