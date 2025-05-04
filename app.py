from flask import Flask, render_template, request, jsonify
import unicodedata
import re

def normalizar(texto):
    texto = texto.lower()  # Converte para minúsculas
    texto = unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('utf-8')  # Remove acentos
    texto = re.sub(r'[^\w\s]', '', texto)  # Remove pontuação
    return texto

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = normalizar(request.json.get('message'))

    respostas = {
        ("oi", "beleza", "olá", "e aí", "opa", "fala", "fala ai", "falaa", "bom dia", "boa tarde", "boa noite"): 
            "Falaa, fã da FURIA! Preparado pra mais um dia?",

        ("sempre pronto", "bora la", "vamos nessa", "nasci pronto", "com certeza", "sim"):
            "Que bom saber, como posso ajudar hoje?",

        ("quem é a furia", "o que é furia", "o que significa a furia", "me conta sobre a furia",  "me fala sobre a furia", "quem vocês são", "quem são vocês"): 
            "A FURIA é um dos maiores times de E-Sports do Brasil, com grandes times e uma torcida apaixonada!",

        ("quem joga", "quem que joga", "quem são os jogadores", "qual o time", "quem está no time da furia"):
            "O elenco atual da FURIA no time de CS têm grandes jogadores como: KSCERATO, yuurih, molodoy, YEKINDAR e FalleN (dependendo do roster atual).",

        ("quem treina essas feras", "quem treina esses caras", "quem é o treinador desse time", "quem é o tecnico", "quem é o coach"):
            "O time consta com dois super treinadores. São eles: Sidde e Hepa!",

        ("qual a data do próximo campeonato", "próximo campeonato", "qual a data do próximo jogo", "quando é o próximo jogo", "próximo jogo", "quais são os próximos campeonatos", "quando jogam", "quando vão jogar", "tem jogo hoje"):
            "Ainda não tenho a data exata do próximo confronto, mas tem campeonato novo chegando, da uma olhada no PGL Astana 2025",

        ("ganharam o ultimo jogo", "venceram o ultimo jogo", "furia ganhou o ultimo jogo", "como foi o último jogo"):
            "No último jogo a FURIA mandou bem demais! Mas vale sempre conferir o resultado e os highlights no canal oficial.",
        
        ("consigo entrar em contato com vocês", "como faço para entrar em contato com vocês", "como faço para falar com vocês", "como posso falar com vocês", "como entrar em contato com vocês"):
            "Você pode falar com nossa equipe de suporte através do seguinte número: (11)99942-1659",

        ("adeus", "tchau", "valeu", "até mais"):
            "Valeu por bater esse papo! Furia neles!"
    }

    resposta = "Hmm... não entendi. Tenta perguntar de outro jeito, furioso!"

    for chaves, mensagem in respostas.items():
        normalizadas_chaves = [normalizar(chave) for chave in chaves]
        if user_input in normalizadas_chaves:
            resposta = mensagem
            break

    return jsonify({'response': resposta})

if __name__ == '__main__':
    app.run(debug=True)