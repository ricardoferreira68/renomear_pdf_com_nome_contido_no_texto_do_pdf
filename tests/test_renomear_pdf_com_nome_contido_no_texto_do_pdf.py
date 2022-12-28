"""Teste automatizados da aplicação que renomea arquivo PDF com o nome contido no próprio arquivo PDF.
    Ler um arquivo PDF, localizar o nome no texto contido no PDF e salvar o arquivo com esse nome.
    Entrada: texto_chave
             ler_arquivo_pdf(nome_pdf)
    Processamento:  Fazer para vários arquivos PDF:
                        abrir_arquivo_pdf(nome_pdf)
                        localizar_texto_chave(texto_chave)
                        extrair_novo_nome_a_partir_do_texto_chave(text_chave)
                        renomear_pdf(nov_nome_pdf)
    Saída: renomear_pdf(novo_nome_pdf)
"""

from test_renomear_pdf_com_nome_contido_no_texto_do_pdf import __version__
from test_renomear_pdf_com_nome_contido_no_texto_do_pdf import main


def test_version():
    assert __version__ == '0.1.0'

def test_abrir_arquivo_pdf():
    assert main.abrir_arquivo_pdf("./arquivos_pdf/RELATÓRIO FREQUENCIA PRODEPA-1.pdf") != None

def test_abrir_arquivo_pdf_invalido():
    assert main.abrir_arquivo_pdf("") == None
    
def test_localizar_texto():
    assert main.localizar_texto(main.abrir_arquivo_pdf("./arquivos_pdf/RELATÓRIO FREQUENCIA PRODEPA-1.pdf")) != None

def test_localizar_texto_invalido():
    assert main.localizar_texto(main.abrir_arquivo_pdf("")) == None

def test_renomear_pdf_nome_invalido():
    assert main.renomear_pdf("./arquivos_pdf/REL FREQUENCIA PRODEPA-1.pdf", "./arquivos_pdf/CONTROLE DE FREQUENCIA - FULANO DE TAL.pdf") == None

def test_renomear_pdf():
    assert main.renomear_pdf("./arquivos_pdf/RELATÓRIO FREQUENCIA PRODEPA-1.pdf", "./arquivos_pdf/CONTROLE DE FREQUENCIA - FULANO DE TAL.pdf") != None