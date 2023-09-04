import mysql.connector
from datetime import datetime

def getEmpresaId(email, password):
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            database="sanderson"
        )

        connection = db.cursor(buffered=True)

        connection.execute("SELECT id FROM empresa WHERE email='{}' AND password='{}';".format(email, password))
        db.commit()

        id = connection.fetchone()[0]

        if id:
            return id
        else:
            return False

    except Exception as e:
        print(e)
        return False

def add_log(message):
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            database="sanderson"
        )

        connection = db.cursor(buffered=True)

        connection.execute("INSERT INTO `logs`(`id`, `time`, `description`) VALUES (NULL,'{}','{}')".format(str(datetime.now().strftime('%d/%m/%Y %H:%M')), str(message)))
        
        db.commit()

        return True
    except Exception as e:
        print(e)
        return None
    
def last_log():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            database="sanderson"
        )

        connection = db.cursor(buffered=True)

        connection.execute("SELECT * FROM logs ORDER BY id DESC LIMIT 1;")
        db.commit()

        log = connection.fetchone()

        if log:
            return log
        else:
            return False

    except Exception as e:
        print(e)
        return False
    
def verify_relatorio_0063(data):
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            database="sanderson"
        )

        connection = db.cursor(buffered=True)

        (cliente, pacote, servico, total, utilizados, validade, compra) = data

        connection.execute("SELECT id FROM relatorio_0063 WHERE cliente = '{}' AND pacote = '{}' AND servico = '{}' AND total = '{}' AND utilizados = '{}' AND validade = '{}' AND compra = '{}';".format(cliente, pacote, servico, total, utilizados, validade, compra))
        db.commit()

        id = connection.fetchone()[0]

        if id:
            return True
        else:
            return False

    except Exception as e:
        print(e)
        return False

def insert_relatorio_0063(data, idEmpresa):
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            database="sanderson"
        )

        connection = db.cursor(buffered=True)

        (cliente, pacote, servico, total, utilizados, validade, compra) = data

        connection.execute("INSERT INTO `relatorio_0063` (`id_empresa`, `id`, `cliente`, `pacote`, `servico`, `total`, `utilizados`, `validade`, `compra`) VALUES ('{}', NULL, '{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(idEmpresa, cliente, pacote, servico, total, utilizados, validade, compra))
        
        db.commit()

        return True
    except Exception as e:
        print(e)
        return None

def verify_relatorio_0123(data):
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            database="sanderson"
        )

        connection = db.cursor(buffered=True)

        (profissional, tipo_contratacao, cargo, banco, agencia, conta, faturado, rateio_servicos, rateio_produtos, rateio_outros, caixinha, descontos, a_pagar, valor_casa) = data

        connection.execute("SELECT id FROM relatorio_0123 WHERE profissional = '{}' AND tipo_contratacao = '{}' AND cargo = '{}' AND banco = '{}' AND agencia = '{}' AND conta = '{}' AND faturado = '{}' AND rateio_servicos = '{}' AND rateio_produtos = '{}' AND caixinha = '{}' AND descontos = '{}' AND a_pagar = '{}' AND valor_casa = '{}';".format(profissional, tipo_contratacao, cargo, banco, agencia, conta, faturado, rateio_servicos, rateio_produtos, rateio_outros, caixinha, descontos, a_pagar, caixinha, valor_casa))

        db.commit()

        id = connection.fetchone()[0]

        if id:
            return True
        else:
            return False

    except Exception as e:
        print(e)
        return False

def insert_relatorio_0123(data, idEmpresa):
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            database="sanderson"
        )

        connection = db.cursor(buffered=True)

        (profissional, tipo_contratacao, cargo, banco, agencia, conta, faturado, rateio_servicos, rateio_produtos, rateio_outros, caixinha, descontos, a_pagar, valor_casa) = data

        connection.execute("INSERT INTO `relatorio_0123` (`id_empresa`, `id`, `profissional`, `tipo_contratacao`, `cargo`, `banco`, `agencia`, `conta`, `faturado`, `rateio_servicos`, `rateio_produtos`, `rateio_outros`, `caixinha`, `descontos`, `a_pagar`, `valor_casa`) VALUES ('{}',NULL,'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(idEmpresa ,profissional, tipo_contratacao, cargo, banco, agencia, conta, faturado, rateio_servicos, rateio_produtos, rateio_outros, caixinha, descontos, a_pagar, caixinha, valor_casa))
        
        db.commit()

        return True
    except Exception as e:
        print(e)
        return None
    
def insert_relatorio_0053(data, idEmpresa):
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            database="sanderson"
        )

        connection = db.cursor(buffered=True)

        (data_reserva, hora, cliente, servico, valor) = data

        connection.execute("INSERT INTO `relatorio_0053` (`id_empresa`, `id`, `data_reserva`, `hora`, `cliente`, `servico`, `valor`) VALUES ('{}', NULL, '{}', '{}', '{}', '{}', '{}');".format(idEmpresa, data_reserva, hora, cliente, servico, valor))
        
        db.commit()

        return True
    except Exception as e:
        print(e)
        return None
    
def verify_relatorio_0053(data):
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            database="sanderson"
        )

        connection = db.cursor(buffered=True)

        (data_reserva, hora, cliente, servico, valor) = data

        connection.execute("SELECT id FROM relatorio_0053 WHERE data_reserva = '{}' AND hora = '{}' AND cliente = '{}' AND servico = '{}' AND valor = '{}';".format(data_reserva, hora, cliente, servico, valor))
        db.commit()

        id = connection.fetchone()[0]

        if id:
            return True
        else:
            return False

    except Exception as e:
        print(e)
        return False

def insert_relatorio_0004(data, idEmpresa):
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            database="sanderson"
        )

        connection = db.cursor(buffered=True)

        (cliente, codigo, aniversario, telefone, celular, email, sexo, como_conheceu, cpf, cep, endereco, numero, estado, cidade, complemento, bairro, profissao, cadastrado, obs, rg) = data

        query = "INSERT INTO `relatorio_0004` (`id_empresa`, `id`, `cliente`, `codigo`, `aniversario`, `telefone`, `celular`, `email`, `sexo`, `como_conheceu`, `cpf`, `cep`, `endereco`, `numero`, `estado`, `cidade`, `complemento`, `bairro`, `profissao`, `cadastrado`, `obs`, `rg`) VALUES ('{}', NULL, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(
            idEmpresa, cliente, codigo, aniversario, telefone, celular, email, sexo, como_conheceu, cpf, cep, endereco, numero, estado, cidade, complemento, bairro, profissao, cadastrado, obs, rg)

        connection.execute(query)

        db.commit()

        return True
    except Exception as e:
        print(e)
        return False

def verify_relatorio_0004(data):
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            database="sanderson"
        )

        connection = db.cursor(buffered=True)

        (cliente, codigo, aniversario, telefone, celular, email, sexo, como_conheceu, cpf, cep, endereco, numero, estado, cidade, complemento, bairro, profissao, cadastrado, obs, rg) = data

        query = "SELECT id FROM relatorio_0004 WHERE cliente = '{}' AND codigo = '{}' AND aniversario = '{}' AND telefone = '{}' AND celular = '{}' AND email = '{}' AND sexo = '{}' AND como_conheceu = '{}' AND cpf = '{}' AND cep = '{}' AND endereco = '{}' AND numero = '{}' AND estado = '{}' AND cidade = '{}' AND complemento = '{}' AND bairro = '{}' AND profissao = '{}' AND cadastrado = '{}' AND obs = '{}' AND rg = '{}';".format(
            cliente, codigo, aniversario, telefone, celular, email, sexo, como_conheceu, cpf, cep, endereco, numero, estado, cidade, complemento, bairro, profissao, cadastrado, obs, rg)

        connection.execute(query)
        db.commit()

        id = connection.fetchone()[0]

        if id:
            return True
        else:
            return False

    except Exception as e:
        print(e)
        return False
    
def insert_relatorio_0186(data, idEmpresa):
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            database="sanderson"
        )

        connection = db.cursor(buffered=True)

        (data, comanda, item, tipo, categoria, profissional, assistente_1, assistente_2, comissao_percentual, cliente, email, telefone, celular, valor, desconto, quantidade, custo, comissao, liquido, ua) = data

        query = "INSERT INTO `relatorio_0186` (`id_empresa`, `id`, `data`, `comanda`, `item`, `tipo`, `categoria`, `profissional`, `assistente_1`, `assistente_2`, `comissao_percentual`, `cliente`, `email`, `telefone`, `celular`, `valor`, `desconto`, `quantidade`, `custo`, `comissao`, `liquido`, `ua`) VALUES ('{}', NULL, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(
            idEmpresa, data, comanda, item, tipo, categoria, profissional, assistente_1, assistente_2, comissao_percentual, cliente, email, telefone, celular, valor, desconto, quantidade, custo, comissao, liquido, ua)

        connection.execute(query)

        db.commit()

        return True
    except Exception as e:
        print(e)
        return False

def verify_relatorio_0186(data):
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            database="sanderson"
        )

        connection = db.cursor(buffered=True)

        (data, comanda, item, tipo, categoria, profissional, assistente_1, assistente_2, comissao_percentual, cliente, email, telefone, celular, valor, desconto, quantidade, custo, comissao, liquido, ua) = data

        query = "SELECT id FROM relatorio_0186 WHERE data = '{}' AND comanda = '{}' AND item = '{}' AND tipo = '{}' AND categoria = '{}' AND profissional = '{}' AND assistente_1 = '{}' AND assistente_2 = '{}' AND comissao_percentual = '{}' AND cliente = '{}' AND email = '{}' AND telefone = '{}' AND celular = '{}' AND valor = '{}' AND desconto = '{}' AND quantidade = '{}' AND custo = '{}' AND comissao = '{}' AND liquido = '{}' AND ua = '{}';".format(
            data, comanda, item, tipo, categoria, profissional, assistente_1, assistente_2, comissao_percentual, cliente, email, telefone, celular, valor, desconto, quantidade, custo, comissao, liquido, ua)

        connection.execute(query)

        result = connection.fetchone()

        if result:
            return True
        else:
            return False

    except Exception as e:
        print(e)
        return False