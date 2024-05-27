from src import socketio
from src.menu import menus

user_states = {}

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')


@socketio.on('start_typing')
def handle_start_typing(data):
    socketio.emit('start_typing', data, broadcast=True)

@socketio.on('stop_typing')
def handle_stop_typing(data):
    socketio.emit('stop_typing', data, broadcast=True)

@socketio.on('fetch_response')
def handle_fetch_response(data):
    user_id = data['userId']
    message = data['message']

    # Inicializa o estado do usuário se não existir
    if user_id not in user_states:
        user_states[user_id] = []

    try:
        # Primeira interação do usuário
        if not user_states[user_id]:
            response = ("Olá! Boas vindas ao serviço de assistência aos afetados pelas enchentes no Rio Grande do Sul. "
                        "Que tipo de suporte você precisa?\n" + get_menu_options(menus))
            user_states[user_id].append("main")
        else:
            response = get_menu_response(user_id, message)
    except KeyError:
        user_states[user_id] = ["main"]
        response = ("Olá! Boas vindas ao serviço de assistência aos afetados pelas enchentes no Rio Grande do Sul. "
                        "Que tipo de suporte você precisa?\n" + get_menu_options(menus))
        
    if response == "Entendi! Aguarde um pouquinho que eu vou pesquisar como posso te ajudar. \n\n Tenho uma boa notícia! Encontrei alguém que pode te ajudar. Já passei o seu telefone e a empresa XXXX vai entrar em contato com você. Se você preferir, pode entrar em contato pelo telefone XXXXXX \n\n\n Essa jornada é um teste. Qualquer informação digitada irá retornar para o começo. \n\n Para conferir a jornada completa, siga os passos: \n1- Solicitar suporte \n> 3- Reparos na casa \n> 5- Móveis e marcenaria":
        response = "Entendi! Aguarde um pouquinho que eu vou pesquisar como posso te ajudar."
        socketio.emit('fetch_response', {'userId': user_id, 'response': response})
        reponse1 = "Tenho uma boa notícia! Encontrei alguém que pode te ajudar. Já passei o seu telefone e a empresa XXXX vai entrar em contato com você. Se você preferir, pode entrar em contato pelo telefone XXXXXX"
        socketio.emit('fetch_response', {'userId': user_id, 'response': reponse1})
        reponse2 = "Essa jornada é um teste. Qualquer informação digitada irá retornar para o começo. \n\n Para conferir a jornada completa, siga os passos: \n>1- Solicitar suporte \n> 3- Reparos na casa \n> 5- Móveis e marcenaria"
        socketio.emit('fetch_response', {'userId': user_id, 'response': reponse2})
        print(response)
    else:
        socketio.emit('fetch_response', {'userId': user_id, 'response': response})

def get_menu_response(user_id, message):
    state_path = user_states[user_id]
    current_menu = get_current_menu(menus, state_path)

    if message == "0":
        # Reseta o estado do usuário para o menu inicial
        user_states[user_id] = ["main"]
        return "Que tipo de suporte você precisa?\n" + get_menu_options(menus)

    # Verifica se a opção está no menu atual
    if state_path == ["main"] and message == "1":
        # Solicitar CEP e número após selecionar "Solicitar suporte"
        user_states[user_id].append("1")
        return "Entendi! Vou encontrar a melhor opção para você. Qual o CEP e número do local onde o serviço será feito?"
    
    # Se o usuário está no passo de fornecer o CEP e número
    if state_path == ["main", "1"] and not message.isdigit():
        user_states[user_id].append("cep")
        return "Legal! Agora me conta qual o tipo de suporte você precisa?\n" + get_menu_options(current_menu["1"]["submenus"])

    if message in current_menu:
        next_menu = current_menu[message].get('submenus', None)
        user_states[user_id].append(message)
        
        if next_menu:
            return current_menu[message]['message'] + "\n" + get_menu_options(next_menu)
        else:
            # Mensagem final personalizada
            return current_menu[message]['message']
    else:
        # Opção inválida
        return (get_menu_options(current_menu))

def get_current_menu(menu, path):
    current = menu
    for p in path[1:]:
        current = current[p]['submenus']
    return current

def get_menu_options(menu):
    response = ""
    for key, value in menu.items():
        if isinstance(value, dict):
            response += f"{key}- {value['title']}\n"
    return response