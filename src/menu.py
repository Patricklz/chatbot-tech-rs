# src/menu.py

menus = {
    "1": {
        "title": "Solicitar suporte",
        "message": "Entendi! Vou encontrar a melhor opção para você, mas primeiro me diga que tipo de orientação deseja receber?",
        "submenus": {
            "1": {
                "title": "Orientações de saúde",
                "message": "Vou te ajudar com isso! Qual o tipo de consulta ou orientação que você precisa?",
                "submenus": {
                    "1": {"title": "Consulta médica", "message": "Consulta médica pode ser marcada aqui."},
                    "2": {"title": "Consulta pediátrica", "message": "Consulta pediátrica pode ser marcada aqui."},
                    "3": {"title": "Atendimento psicológico", "message": "Atendimento psicológico pode ser marcado aqui."},
                },
            },
            "2": {
                "title": "Suporte jurídico",
                "message": "Vou te ajudar com isso! Qual o tipo de suporte jurídico que você precisa?",
                "submenus": {
                    "1": {"title": "Direito criminal", "message": "O escritório entrará em contato o mais breve possível."},
                    "2": {"title": "Direito civil", "message": "O escritório Civil entrará em contato o mais breve possível."},
                },
            },
            "3": {
                "title": "Reparos na casa",
                "message": "Legal! Qual tipo de reparo você precisa?",
                "submenus": {
                    "1": {"title": "Encanamento", "message": "Encanamento solicitado."},
                    "2": {"title": "Elétrica", "message": "Serviço elétrico solicitado."},
                    "3": {"title": "Limpeza", "message": "Serviço de limpeza solicitado."},
                    "4": {"title": "Pintura", "message": "Serviço de pintura solicitado."},
                    "5": {"title": "Móveis e Marcenaria", "message": "Entendi! Aguarde um pouquinho que eu vou pesquisar como posso te ajudar. \n\n Tenho uma boa notícia! Encontrei alguém que pode te ajudar. Já passei o seu telefone e a empresa XXXX vai entrar em contato com você. Se você preferir, pode entrar em contato pelo telefone XXXXXX"},
                    "6": {"title": "Retirada de entulho", "message": "Serviço de retirada de entulho solicitado."},
                    "7": {"title": "Recuperação de eletrodomésticos", "message": "Serviço de recuperação de eletrodomésticos solicitado."},
                    "8": {
                        "title": "Avaliação de estrutura",
                        "message": "Qual tipo de avaliação de estrutura você precisa?",
                        "submenus": {
                            "1": {"title": "Defesa civil", "message": "Avaliação pela defesa civil solicitada."},
                            "2": {"title": "Engenheiro", "message": "Avaliação por engenheiro solicitada."},
                        },
                    },
                    "9": {"title": "Voltar para o menu principal"},
                },
            },
            "4": {"title": "Voltar para o menu principal"},
        },
    },
    "2": {"title": "Oferecer suporte", "message": "Se você faz parte de alguma empresa ou iniciativa que pode oferecer ajuda para as pessoas, envie um e-mail para XXXXX@gmail.com"},
    "3": {"title": "Orientações de segurança", "message": "Aqui estão algumas orientações de segurança. \n\n https://agenciabrasil.ebc.com.br/saude/noticia/2024-05/saude-alerta-para-cuidados-pos-enchente-no-rio-grande-do-sul"},
    "4": {"title": "Receber alertas oficiais da Defesa Civil", "message": "Para receber alertas sobre condições climáticas adversas, entre em contato com a Defesa Civil pelo whatsapp no link: \n\n https://api.whatsapp.com/send/?phone=556120344611&text&type=phone_number&app_absent=0"},
}
