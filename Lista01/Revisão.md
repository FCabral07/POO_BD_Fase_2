
Q01 - Persistência de Dados
	É o ato de salvar os dados em algo como o BD, para poder utilizá-los e manipulá-los no futuro

Q02 - Obj transientes e persistentes
	Objetos transientes são os objetos temporários, ou seja, aqueles que não serão persistidos, já o persistentes são os objetos salvos em BD, etc

Q03 - BD Relacional e BD OO
	O BD relacional guarda os dados de maneira tabular, enquanto o OO guarda em formato de objetos orientados ao mundo real

Q04 - ORM
	Serve para auxiliar na integração entre os BDs relacionais e OO, manipulando os dados em formato de objetos

Q05 - Dados
	Estruturados: São aqueles que seguem o formato de tabela e tem a estrutura muito bem definida;
	Semiestruturados: Seguem uma estrutura de chave-valor, não é necessariamente estruturado, mas tem uma certa estrutura;
	Não-estruturado: Dados sem estruturas alguma, pode ser em formato de texto, email, video, imagem

Q06 - Biblioteca extração
	JSOUP

Q07 - XML
	a) Sintaxe inicial:
		< ? version... ? >
	b) Organização:
		São estruturados de forma hierárquica, seguindo um padrão de árvore
	c) Representação:
		Tem duas formas, em árvore com elementos aninhados, ou em forma textual, seguindo as marcações XML

Q08 - Documento XML
< ? version= "1.0" ?>
< produtos >
	< produto >
	...
	</ produto > 
</ produtos >

Q09 - JSON
	Formato de dados simples e flexível, muito usado para troca de informações na internet. Tem como principais características ser leve e pouco verboso, além de fácil entendimento e suporte à dados primitivos

Q10 - Serialização e Desserialização
	Serialização: Conversão de dados para o formato JSON
	Desserialização: Processo inverso, transforma o JSON em sua forma original

Q11 - Exemplo JSON
{
	"nome": "Felipe",
	"idade": 23,
	"parentes": [ "pai", "mae" ],
	"curso": {
		"universidade": "Unifacisa",
		"curso": "SI"
	}
}

Q12 - Diferença JSON e XML
	JSON é mais eficiente para transferência de dados e APIs, enquanto o XML é mais utilizado para estruturas de dados complexas. Além do XML ter a estrutura parecida com a do HTML, e o JSON ser mais legível que um XML

Q13 - Para que serve o JDBC com SGBD
	Permite que apps Java se conectem ao BD, de forma a enviar dados para o mesmo

Q14 - Principais componentes JDBC
	1- Connexion: É a conexão com o BD;
	2- Statement: Envia comandos SQL para o BD;
	3- resultSet: É o resultado de uma consulta SQL, permitindo recuperar e manipular dados;

Q15 - Restrições JDBC atualmente
	Limitações de desempenho e complexidade