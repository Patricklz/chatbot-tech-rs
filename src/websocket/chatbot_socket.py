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

    socketio.emit('fetch_response', {'userId': user_id, 'response': response})

def get_menu_response(user_id, message):
    state_path = user_states[user_id]
    current_menu = get_current_menu(menus, state_path)

    if message == "0":
        # Reseta o estado do usuário para o menu inicial
        user_states[user_id] = ["main"]
        return "Que tipo de suporte você precisa?\n" + get_menu_options(menus)
    
    # Verifica se a opção está no menu atual
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
        return ("Opção inválida. Por favor, escolha uma opção válida.\n" +
                get_menu_options(current_menu))

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