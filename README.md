<h1>Teste documentação API com flask_restplus</h1>
<br>

<p>
    Estrutura básica para testar a biblioteca <a href="https://github.com/noirbizarre/flask-restplus">flask_restplusflask_restplus</a> / <a href="https://github.com/python-restx/flask-restx">flask-restx</a>
    Versões: Python 3.9.5, PIP 21.1.3, flask_restplusflask_restplus 0.13.0, MariaDB 8.0.12
</p>


<h4>Dependencias</h4>
<ul>
    <li>dotenv</li>
    <li>flask-restplus</li>
    <li>mysql-connector-python</li>
</ul>
<br>


<h4>Estrutura banco de dados</h4>
Link: <a href="doc/banco.sql">.SQL</a>
<br>


<h4>Executar - Windows</h4>
<ul>
    <li>set FLASK_APP=flaskr</li>
    <li>set FLASK_ENV=development</li>
    <li>set FLASK_RUN_HOST=0.0.0.0</li>
    <li>set FLASK_RUN_PORT=5000</li>
    <li>flask run</li>
</ul>

<h4>Executar - Linux</h4>
<ul>
    <li>export FLASK_APP=flaskr</li>
    <li>export FLASK_ENV=development</li>
    <li>export FLASK_RUN_HOST=0.0.0.0</li>
    <li>export FLASK_RUN_PORT=5000</li>
    <li>flask run</li>
</ul>
<br>


<h4>Documentação Swagger</h4>
<ul>
    <li>Link:
        <a href="http://localhost:5000/api/doc">http://localhost:5000/api/doc</a>
    </li>
    <li>
        <img src="doc/doc_api.png">
    </li>
</ul>
<br>

<h4>Postman Collection</h4>
Link: <a href="doc/flask-restplus-teste.postman_collection.json">Collection</a>
<br>

<h4>Pendências</h4>
<ul>
    <li>Endpoint DELETE Pessoa</li>
    <li>Endpoint GET por ID de Pesssoa</li>
    <li>Testes unitários</li>
    <li>SQL Alchemy</li>
    <li>Virtual Environments</li>
    <li>Docker</li>
</ul>