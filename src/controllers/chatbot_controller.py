from flask import Blueprint, render_template, jsonify, request
from src.services.chatbot_service import ChatbotService

chatbot_bp = Blueprint('chatbot', __name__)

@chatbot_bp.route('/', methods=['POST'])
def chatbot():
    
    body = request.get_json()

    option = body["option"]
 
    answer = ChatbotService.get_information(option)
    
    return jsonify(answer)