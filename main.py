from src import app

if __name__ == "__main__":
    app.logger.info('[SERVER] Servidor iniciado na porta {port}'.format(port=7575))
    app.run(host='0.0.0.0', port=7575)
