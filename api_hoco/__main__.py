# aqui eu faço a inicialização do servidor, rodando em http://0.0.0.0/5000

from . rest import app


app.run(host="0.0.0.0", port=8000, debug=True)
