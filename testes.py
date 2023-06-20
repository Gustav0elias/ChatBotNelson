import unittest
from nelson import *

class perguntasTestadas(unittest.TestCase):
    def setUp(self):
        self.bot = iniciar()
        
    def testeSaudacoesIniciais(self):

        colecao = ["olá","oi", "e aí"]
        for i in colecao:
           
            resposta= self.bot.get_response(i)
            self.assertIn("Olá, sou o robô educacional Nelson, estou aqui para tirar suas dúvias sobre o movimento Cinema Novo. Qual a sua dúvida?",resposta.text)
            print("teste das saudações iniciais: ola, oi e e ", i)


    def testaBomdia(self):
        resposta= self.bot.get_response("bom dia")
        self.assertIn("Bom dia, sou o robô educacional Nelson, estou aqui para tirar suas dúvias sobre o movimento Cinema Novo. Qual a sua dúvida?",resposta.text)
        print("teste das saudações iniciais: Bom dia ")

    def testeBoatarde(self):
        resposta= self.bot.get_response("boa tarde")
        self.assertIn("Boa tarde, sou o robô educacional Nelson, estou aqui para tirar suas dúvias sobre o movimento Cinema Novo. Qual a sua dúvida?",resposta.text)
        print("teste das saudações iniciais: Boa tarde  ")

    def testaBoanoite(self):
        resposta= self.bot.get_response("boa noite")
        self.assertIn("Boa noite, sou o robô educacional Nelson, estou aqui para tirar suas dúvias sobre o movimento Cinema Novo. Qual a sua dúvida?",resposta.text)
        print("teste das saudações iniciais: Boa noite  ")
   
    def testeOutrosTratamentos(self):
        colecao = ["tudo bem","tudo certo"]
        for i in colecao:
           
            resposta= self.bot.get_response(i)
            self.assertIn("sou o robô educacional Nelson, estou aqui para tirar suas dúvias sobre o movimento Cinema Novo. Qual a sua dúvida?",resposta.text)
            print("teste de outras formas de tratamento: ", i)    

    def testeOrigem(self):
        respotaTeste = "Na década de 1950, o cinema brasileiro era dominado por chanchadas (musicais, muitas vezes cômicos e baratos), épicos de grande orçamento que imitavam o estilo de Hollywood, e cinema sério que o cineasta de Cinema Novo Carlos Diegues caracteriza como às vezes cerebral e muitas vezes ridiculamente pretensioso. Este cinema tradicional foi apoiado por produtores, distribuidores e expositores estrangeiros. À medida que a década terminava, jovens cineastas brasileiros protestaram contra os filmes que eles percebiam como de mau gosto e comercialismo sórdido, uma forma de prostituição cultural que dependia do patrocínio de um Brasil analfabeto e empobrecido. Tudo começa em 1952 com o primeiro Congresso Paulista de Cinema Brasileiro e o primeiro Congresso Nacional do Cinema Brasileiro. Por meio desses congressos, foram discutidas novas ideias para a produção de filmes nacionais. Essa nova fase está bem representada no filme Rio, 40 Graus (1955), de Nelson Pereira dos Santos. As propostas do neorrealismo italiano, que Alex Viany vinha divulgando, foram a inspiração do autor do filme."
        resposta= self.bot.get_response("Qual a origem do cinema novo")
        self.assertIn(respotaTeste,resposta.text)
        
    def testeCaracteristicas(self):
        respotaTeste = "A maioria dos historiadores do cinema divide o Cinema Novo em três fases sequenciais que diferem em tema, estilo e assunto. Stam e Johnson identificam uma primeira fase que vai de 1960 a 1964, uma segunda fase em execução de 1964 a 1968, e uma terceira fase em execução de 1968 a 1972 (embora também reivindiquem que a fase final se conclui grosso modo no final de 1971). Há pouco desacordo entre os críticos de cinema sobre essa linha do tempo. O cineasta Carlos Diegues afirma que, embora a falta de fundos reduza a precisão técnica dos filmes do Cinema Novo, também permitiu que diretores, escritores e produtores tivessem uma quantidade incomum de liberdade criativa. Porque o Cinema Novo não é uma escola, não tem um estilo estabelecido, afirma Diegues. No Cinema Novo, as formas expressivas são necessariamente pessoais e originais sem dogmas formais. Esta liberdade de direção, juntamente com a mudança do clima social e político no Brasil, fez com que o Cinema Novo experimentasse turnos de forma e conteúdo em um curto período de tempo."
        resposta= self.bot.get_response("Quais as características do cinema novo")
        self.assertIn(respotaTeste,resposta.text)
        
    def testeInfluencia(self):
        respotaTeste = "Os cineastas brasileiros modelaram o Cinema Novo segundo gêneros conhecidos por subversão: neorrealismo italiano e Nouvelle Vague francesa. Johnson e Stam afirmaram ainda que o Cinema Novo tem algo em comum com o filme soviético dos anos vinte, que, como o neorrealismo italiano e a francesa Nouvelle Vague, tinha uma propensão para teorizar sua própria prática cinematográfica. O cinema neorrealista italiano filmava frequentemente em localização com atores não-profissionais e cidadãos da classe trabalhadora representados durante os tempos econômicos difíceis após a Segunda Guerra Mundial. A Nouvelle Vague absorveu fortemente o neorrealismo italiano, pois os diretores franceses rejeitaram o cinema clássico e abraçaram a iconoclasia. Alguns proponentes do Cinema Novo foram desprezíveis com a política da Nouvelle Vague, considerando sua tendência de copiar estilisticamente Hollywood como elitista. Mas os cineastas de Cinema Novo foram bastante atraídos pelo uso da teoria do autor por parte da onda francesa, o que permitiu aos diretores fazer filmes de baixo orçamento e desenvolver bases de fãs pessoais."
        resposta= self.bot.get_response("Quais as influências do cinema novo")
        self.assertIn(respotaTeste,resposta.text)
        
    def testeRepresentantes(self):
        respotaTeste= "Cacá Diegues, Glauber Rocha, Joaquim Pedro de Andrade, Leon Hirszman,Nelson Pereira dos Santos, Roberto Santos, Roberto Pires, Arnaldo Jabor, Helena Solberg, Ruy Guerra, Olney São Paulo, Paulo César Saraceni"
        resposta= self.bot.get_response("Quais os principais representantes do cinema novo")
        self.assertIn(respotaTeste,resposta.text)
        
    def testeLegado(self):
        respotaTeste = "Em 1969, o governo brasileiro instituiu a Embrafilme, empresa destinada a produzir e distribuir o cinema brasileiro. A Embrafilme produziu filmes de vários gêneros, incluindo fantasias e épicos de grande orçamento. Na época, o cineasta Carlos Diegues disse que apoiava a Embrafilme porque era - a única empresa com poder econômico e político suficiente para enfrentar a devastadora voracidade das corporações multinacionais no Brasil. Além disso, Diegues afirmou que enquanto o Cinema Novo não está identificado com a Embrafilme, ​a existência é, na realidade, um projeto do Cinema Novo.Quando a Embrafilme foi desmantelada em 1990 pelo presidente Fernando Collor de Mello, as conseqüências para o setor cinematográfico brasileiro foram imediatas e sombrias. À falta de investidores, muitos diretores brasileiros co-produziram filmes em inglês. Isso causou que o cinema inglês ultrapassasse o mercado brasileiro, que passou de 74 filmes produzidos em 1989 para nove filmes produzidos em 1993. O presidente brasileiro Itamar Franco encerrou a crise implementando o Prêmio Resgate do Cinema Brasileiro, que financiou 90 projetos entre 1993 e 1994. A premiação abriu novas portas para uma nova geração de novos cineastas (e alguns dos veteranos) confiantes de que, como o título de um filme do cineasta veterano Carlos Diegues, anunciado profeticamente, chegariam melhores dias (Dias Melhores Virão, 1989)."
        resposta= self.bot.get_response("Qual o legado do cinema novo")
        self.assertIn(respotaTeste,resposta.text)

    def testeFilmes(self):
        respotaTeste = "Aruanda (1960), Arraial do Cabo (1960), Cinco Vezes Favela (1962), Barravento (1962), Os Cafajestes (1962), Ganga Zumba (1963), Vidas Secas (1963), Sol Sobre a Lama (1963), Deus e o Diabo na Terra do Sol (1964), Os Fuzis (1964)"
        resposta= self.bot.get_response("Quais os principais filmes do cinema novo")
        self.assertIn(respotaTeste,resposta.text)
if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(perguntasTestadas))

    executor = unittest.TextTestRunner()
    executor.run(testes)   