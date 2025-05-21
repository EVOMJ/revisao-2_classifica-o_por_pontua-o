def classificar_ia(pontuacao):
    if pontuacao < 0:
        return "Erro: Pontuação inválida! ❌"
    elif pontuacao <= 39.9:
        return "IA em Treinamento 🍼"
    elif pontuacao <= 69.9:
        return "IA Intermediária 🧠"
    elif pontuacao <= 89.9:
        return "IA Otimizada 🚀"
    elif pontuacao <= 100:
        return "IA Avançada (nível Skynet) 🤯"
    else:
        return "Erro: IA fora da escala! ⚠️"

# Exemplo de uso com tratamento de erro para entrada inválida
try:
    pontuacao = float(input("Digite a pontuação da IA (%): "))
    classificacao = classificar_ia(pontuacao)
    print(f"Classificação: {classificacao}")
except ValueError:
    print("Por favor, digite um número válido para a pontuação.")