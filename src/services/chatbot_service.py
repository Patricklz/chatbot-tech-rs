


class ChatbotService:
  
  @staticmethod
  def get_information(option):

    
    if(option == None):
      message = "Olá! Boas vindas ao serviço de assistência aos afetados pelas enchentes no Rio Grande do Sul. Que tipo de suporte você precisa?"
    else:
      message = "Opção inválida"

    return message