import unittest
from Newton import *

CHAMANDO_NEWTON = "audios\\chamando newton.wav"
CHAMANDO_OUTRO_NOME = "audios\\chamando outro nome.wav"

class TesteChamandoNome(unittest.TestCase):

    def setUp(self):
        iniciar()

    def testar_reconhecer_nome(self):
        _, reconhecedor, palavras_de_parada, _, _ = iniciar()
        tem_fala, fala = processar_audio_da_fala(CHAMANDO_NEWTON, reconhecedor)
        self.assertTrue(tem_fala)
        tem_transcricao, transcricao = transcrever_fala(fala, reconhecedor)
        print(f"comando reconhecido: {transcricao}")
        self.assertTrue(tem_transcricao)
        tokens = tokenizar_transcricao(transcricao)
        tokens = eliminar_palavras_de_parada(tokens, palavras_de_parada)
        nome_assistente = tokens[0].lower()
        print(f"nome do assistente: {nome_assistente}")
        self.assertIn("newton", nome_assistente)

    def testar_nao_reconhecer_outro_nome(self):
        _, reconhecedor, palavras_de_parada, _, _ = iniciar()
        tem_fala, fala = processar_audio_da_fala(CHAMANDO_OUTRO_NOME, reconhecedor)
        self.assertTrue(tem_fala)
        tem_transcricao, transcricao = transcrever_fala(fala, reconhecedor)
        print(f"comando reconhecido: {transcricao}")
        self.assertTrue(tem_transcricao)
        tokens = tokenizar_transcricao(transcricao)
        tokens = eliminar_palavras_de_parada(tokens, palavras_de_parada)
        nome_assistente = tokens[0].lower()
        print(f"nome do assistente: {nome_assistente}")
        self.assertNotIn("newton", nome_assistente)

if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteChamandoNome))
    executor = unittest.TextTestRunner()
    executor.run(testes)