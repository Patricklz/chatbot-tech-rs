from src import create_app, socketio
import eventlet

if __name__ == '__main__':
    app = create_app()
    # app.run(debug=True)
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)