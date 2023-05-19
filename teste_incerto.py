import unittest
from incerto import *
from Newton import *

PERGUNTA_INCERTO= "audios\\uso incerto.wav"

class TestePerguntaIncerto(unittest.TestCase):

    def setUp(self):
        iniciar()

    def testar_uso_crase(self):
        iniciado, reconhecedor, palavras_de_parada, nome_do_assistente, acoes = iniciar()
        self.assertTrue(iniciado)
        tem_fala, fala = processar_audio_da_fala(PERGUNTA_INCERTO, reconhecedor)
        self.assertTrue(tem_fala)
        tem_transcricao, transcricao = transcrever_fala(fala, reconhecedor)
        print(f"comando reconhecido: {transcricao}")
        self.assertTrue(tem_transcricao)
        tokens = tokenizar_transcricao(transcricao)
        tokens = eliminar_palavras_de_parada(tokens, palavras_de_parada)
        valido, _, _ = validar_comando(tokens, nome_do_assistente, acoes)
        self.assertTrue(valido)

if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TestePerguntaIncerto))
    executor = unittest.TextTestRunner()
    executor.run(testes)