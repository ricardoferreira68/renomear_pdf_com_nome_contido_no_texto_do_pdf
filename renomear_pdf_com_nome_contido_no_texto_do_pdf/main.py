"""Aplicação que renomea arquivo PDF com o nome contido no próprio arquivo PDF.
    Ler um arquivo PDF, localizar o nome no texto contido no PDF e salvar o arquivo com esse nome.
    Entrada: texto_chave
             ler_arquivo_pdf(nome_pdf)
    Processamento:  Fazer para vários arquivos PDF:
                        abrir_arquivo_pdf(nome_pdf)
                        localizar_texto()
                        extrair_novo_nome_a_partir_do_texto_chave(texto_chave)
                        salvar_pdf(nov_nome_pdf)
    Saída: salvar_pdf(novo_nome_pdf)
"""

from io import BufferedReader
import os
import PyPDF2


def abrir_arquivo_pdf(nome_pdf: str) -> BufferedReader:
    """Abre o arquivo PDF para leitura.

    Args:
        nome_pdf (str): nome do arquivo gravado na memória auxiliar.

    Returns:
        BufferedReader: descritor para o arquivo aberto ou None
    """
    try:
        arquivo_pdf = open(nome_pdf, 'rb')
        return arquivo_pdf
    except:
        return None


def localizar_texto(arquivo_pdf: BufferedReader) -> str:
    """Retorna o nome contido na segunda linha do texto extraído do PDF.

    Args:
        arquivo_pdf (BufferedReader): Descritor do arquivo

    Returns:
        str: String da segunda linha do texto extraído do arquivo PDF.
    """
    linha_do_texto = 1
    try:
        texto_pdf = PyPDF2.PdfReader(arquivo_pdf)
    except:
        return None
    texto_localizado = texto_pdf.pages[0].extract_text().splitlines()[linha_do_texto]
    # print("Tipo do texto do PDF: ", texto_localizado)
    return texto_localizado


def renomear_pdf(arquivo_pdf: str, novo_nome_pdf: str) -> bool:
    """Troca o nome do arquivo PDF para o novo nome.

    Args:
        arquivo_pdf (str): nome atual do arquivo.
        novo_nome_pdf (str): novo nome a ser renomeado.

    Returns:
        bool: True
    """
    try:
        os.rename(arquivo_pdf, novo_nome_pdf)
        return True
    except:
        return None


if __name__ == "__main__":
    quantidade_arquivo_renomeado: int = 0
    pasta_com_arquivos_pdf: str = "./arquivos_pdf/"
    print("Salvando arquivos PDF como o novo nome ...")
    caminhos = [os.path.join(pasta_com_arquivos_pdf, nome) for nome in os.listdir(pasta_com_arquivos_pdf)]
    arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
    
    for nome_com_caminho in arquivos:
        try:
            arquivo_pdf = abrir_arquivo_pdf(nome_com_caminho)
            nome = localizar_texto(arquivo_pdf=arquivo_pdf)
            novo_nome_pdf = f"{pasta_com_arquivos_pdf}CONTROLE DE FREQUENCIA - {nome}.pdf"
            arquivo_pdf.close()
            renomear_pdf(nome_com_caminho, novo_nome_pdf) 
            quantidade_arquivo_renomeado+=1
        except:
            print("Erro")
        print(f"{quantidade_arquivo_renomeado} arquivo(s) salvo(s).")