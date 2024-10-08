import time

hino_corinthians = [
    "Salve o Corinthians",
    "O campeão dos campeões",
    "Eternamente dentro dos nossos corações",
    "Salve o Corinthians",
    "De tradições e glórias mil",
    "Tu és orgulho",
    "Dos desportistas do Brasil",
    "",
    "Teu passado é uma bandeira",
    "Teu presente é uma lição",
    "Figuras entre os primeiros",
    "Do nosso esporte bretão",
    "Corinthians grande",
    "Sempre altaneiro",
    "És do Brasil",
    "O clube mais brasileiro"
]

def cantar_hino():
    for linha in hino_corinthians:
        print(linha)
        time.sleep(2)  # Espera 2 segundos entre as linhas

cantar_hino()
