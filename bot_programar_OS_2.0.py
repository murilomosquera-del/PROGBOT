import datetime as dt
import pandas as pd
import numpy as np
from pathlib import Path
import pyperclip
import pyautogui
from pyautogui import ImageNotFoundException
import logging
import os
import time
from datetime import datetime, date
import calendar
import sys
import atexit
import signal
from dataclasses import dataclass, field



log_path = f"C:/Users/U469784/venvs/py311/bot_programacao/LOGS/log_execucao_{dt.date.today():%Y%m%d}.log"

logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

# Caminho para salvar os prints de erros
caminho_destino_prints = os.path.join(
    r"C:\Users\U469784\venvs\py311\bot_programacao\LOGS\PRINTS_ERRO",
    f"painel_print_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
)

imagem_janela_selecao = r"C:\Users\U469784\venvs\py311\bot_cancelamento\janela_selecao.png"
imagem_janela_desbloq = r"C:\Users\U469784\venvs\py311\bot_programacao\PRINTS\janela_desbloq_sucesso.png"
imagem_botao_ok = r"C:\Users\U469784\venvs\py311\bot_programacao\PRINTS\botao_ok_janela_desbloq_sucesso.png"
imagem_janela_desprog = r"C:\Users\U469784\venvs\py311\bot_programacao\PRINTS\janela_confirm_desprogramar.png"
imagem_botao_yes_desprog = r"C:\Users\U469784\venvs\py311\bot_programacao\PRINTS\botao_yes_desprogramar.png"
imagem_janela_info_bloqueio = r"C:\Users\U469784\venvs\py311\bot_programacao\PRINTS\janela_info_bloqueio_desprogramadas.png"
janela_atencao = r"C:\Users\U469784\venvs\py311\bot_cancelamento\titulo_janela_atencao.png"
janela_processando_dados = r"C:\Users\U469784\venvs\py311\bot_cancelamento\processando_dados_janela.png"
botao_ok_sucesso = r"C:\Users\U469784\venvs\py311\bot_cancelamento\botao_ok_sucesso.png"
janela_bloqueio_click = r"C:\Users\U469784\venvs\py311\bot_cancelamento\janela_atencao_bloqueio_click.png"
botao_ok_bloqueio_click = r"C:\Users\U469784\venvs\py311\bot_cancelamento\botao_ok_atencao_bloqueio_click.png"
janela_editar_os = r"C:\Users\U469784\venvs\py311\bot_programacao\PRINTS\janela_editar_os_principal.png"
janela_edicao_habilidade = r"C:\Users\U469784\venvs\py311\bot_programacao\PRINTS\janela_campo_edicao_habilidade_turma.png"
imagem_caracteristica_propria_eps = r"C:\Users\U469784\venvs\py311\bot_programacao\PRINTS\imagem_caracteristica_propria_eps.png"
janela_confirm_editar = r"C:\Users\U469784\venvs\py311\bot_programacao\PRINTS\janela_confirm_programadas_editar.png"
janela_atencao_editar_os = r"C:\Users\U469784\venvs\py311\bot_programacao\PRINTS\janela_atencao_editar_os.png"
botao_ok_janela_atencao_editar = r"C:\Users\U469784\venvs\py311\bot_programacao\PRINTS\botao_ok_janela_atencao_editar.png"
janela_confirm_programar = r"C:\Users\U469784\venvs\py311\bot_programacao\PRINTS\janela_confirm_programar.png"
janela_programar_lote = r"C:\Users\U469784\venvs\py311\bot_programacao\PRINTS\janela_programar_lote.png"
campo_plan_data_inicio = r"C:\Users\U469784\venvs\py311\bot_programacao\PRINTS\plan_data_inicio_programar_lote.png"
campo_plan_data_final = r"C:\Users\U469784\venvs\py311\bot_programacao\PRINTS\plan_data_final_programar_lote.png"
campo_prioridades = r"C:\Users\U469784\venvs\py311\bot_programacao\PRINTS\prioridades_programar_lote.png"
campo_empresas_programar = r"C:\Users\U469784\venvs\py311\bot_programacao\PRINTS\campo_empresas_programar_os.png"
botao_confirmar_programar_lote = r"C:\Users\U469784\venvs\py311\bot_programacao\PRINTS\botao_confirmar_programar.png"
janela_aviso_programar_lote = r"C:\Users\U469784\venvs\py311\bot_programacao\PRINTS\janela_aviso_programar_lote.png"
botao_sim_aviso_programar_lote = r"C:\Users\U469784\venvs\py311\bot_programacao\PRINTS\botao_sim_aviso_programar_lote.png"
janela_confirm_programar_final = r"C:\Users\U469784\venvs\py311\bot_programacao\PRINTS\janela_confirm_programar_final.png"
janela_aviso_editar_programadas = r"C:\Users\U469784\venvs\py311\bot_programacao\PRINTS\janela_aviso_editar_programadas.png"
botao_ok_operacao_sucesso = r"C:\Users\U469784\venvs\py311\bot_programacao\PRINTS\botao_ok_operacao_sucesso.png"
janela_operacao_efetuada_sucesso = r"py311/bot_programacao/PRINTS/janela_operacao_efetuada_com_sucesso.png"
janela_falha_eqm = r"C:\Users\U469784\venvs\py311\bot_programacao\PRINTS\janela_falha.png"
botao_fechar_janela_falha = r"C:\Users\U469784\venvs\py311\bot_programacao\PRINTS\botao_fechar_janela_falha.png"
janela_sem_resposta_eqm = r"C:\Users\U469784\venvs\py311\bot_programacao\PRINTS\janela_not_responding.png"
janela_sem_resposta_eqm_2 = r"C:\Users\U469784\venvs\py311\bot_programacao\PRINTS\janela_eqm_not_responding.png"
janela_alt_tab = r"C:\Users\U469784\venvs\py311\bot_programacao\PRINTS\janela_alt_tab.png"
botao_restore = r"C:\Users\U469784\venvs\py311\bot_programacao\PRINTS\botao_restore.png"

#pyautogui.displayMousePosition()
posicao_28 = (783,439) #botao ok confirmação de desbloquear
posicao_1 = (162,74) 
rgb_posicao_1 = (231,231,239)
posicao_2 = (96,99)
posicao_3 = (1305,174)
posicao_4 = (671,201)
rgb_posicao_4 = (82,190,231)
posicao_5 = (902,201)
posicao_6 = (787,546)
posicao_7 = (610,321) #clicar dentro do campo de pesquisa de ordens de serviço
posicao_8 = (788,541) #confirmar 1
posicao_9 = (1002,602) #confirmar 2
rgb_posicao_9 = (115,134,132)
posicao_10 = (91,370) #clicar em uma das linhas no agrupamento de colunas
posicao_11 = (778,687) #botão bloquear 
posicao_12 = (770,662) # selecionar desbloquear
posicao_13 = (171,654) # botao programar
posicao_14 = (178,709) # seleção desprogramar OS na lista suspensa
posicao_15 = (85,650) # selecionar editar OS
posicao_16 = (447,78) # campo características
posicao_17 = (562, 104) # ordenar campo características
posicao_18 = (1053,123) # abrir preenchimento do primeiro campo de características rgb (247,247,247)
posicao_19 = (334,700) # desmarcar editar próxima 
rgb_posicao_19 = (0,162,214)
posicao_20 = (952,695) #botao confirmar janela de edição de caracteristicas
rgb_posicao_20 = (49,174,16)
posicao_21 = (1016,661) #botao confirmar janela de edição de OS
rgb_posicao_21 = (49, 178, 16)
posicao_22 = (166, 683) # seleção programar OS na lista suspensa
posicao_23 = (956, 674) # botao confirmar janela de programação de lote de OS
rgb_posicao_23 = (49,182,24)
posicao_24 = (366, 237) # campo empresas programção de lote
posicao_25 = (360, 268) # campo plan data inicio programação de lote
posicao_26 = (535, 268) # campo plan data final programação de lote
posicao_27 = (759, 233) # campo prioridades programação de lote

# Flags de controle de erros

global flag_travamento
global flag_erro
global flag_janela_oculta

#pyautogui.displayMousePosition()


hoje = dt.date.today()

cinco_dias_atras = hoje - dt.timedelta(days=5)

ultimo_dia = calendar.monthrange(hoje.year, hoje.month)[1]

data_final_mes = dt.date(hoje.year, hoje.month, ultimo_dia)

amanha = hoje + dt.timedelta(days=2)

print(f"Data hoje: {hoje:%d/%m/%Y}")

print(f"Data de referência: {data_final_mes:%d/%m/%Y}")

logging.info(f"Data hoje: {hoje:%d/%m/%Y}")
logging.info(f"Data de referência: {data_final_mes:%d/%m/%Y}")



ARQUIVO_BASE_EQM = r"\\brnet002\Publico\Central_De_Relatorios\manutencao\base_eqm\base_eqm.csv"
ARQUIVO_BI_PCP_BASE_OS = r"\\brnet002\Publico\Central_De_Relatorios\manutencao\bi_pcp_base_os\bi_pcp_base_os.csv"
PASTA_CARGA_WFM = Path(r"\\brnet002\Publico\Central_De_Relatorios\tempo_real\carga_click_tarefas_abertas_tempo_real")
ARQUIVO_CARGA_WFM = PASTA_CARGA_WFM/f"{hoje:%Y%m}"/f"{hoje:%Y%m%d}_carga_click_tarefas_abertas_tempo_real.csv"
print(ARQUIVO_CARGA_WFM)
# === Exporta Excel com 2 abas ====================================================================================================================

pasta_saida = Path(r"C:\Users\U469784\venvs\py311\bot_programacao\EXCEL")
pasta_saida.mkdir(parents=True, exist_ok=True)
arquivo_saida = pasta_saida / f"pendentes_{hoje:%Y%m%d}.xlsx" 
arquivo_saida_teste = pasta_saida / f"teste_{hoje:%Y%m%d}.xlsx" 

# === Inicio do Novo tratamento com base eqm e extração do wfm =====================================================================================

dtype_map_wfm = {
    'Call_id': 'string',
    'Skill': 'string',
    'Status': 'string',
    'Descricao_Tarefa': 'string',
    'Area_Op': 'string',
    'Regional':'string'
}


df_wfm = pd.read_csv(
  ARQUIVO_CARGA_WFM,
    sep=';',
    usecols=['Call_id','Skill','Status','Descricao_Tarefa','Area_Op','Regional'],
    encoding='latin1',   
    engine='python',
    dtype=dtype_map_wfm
)

dtype_map_eqm = {
    'UTD': 'string',
    'OS_CORRECAO': 'string',
    'DEFEITO': 'string',
    'POT_DESLIGAMENTO':'string',
    'TIPO_DEFEITO': 'string',
    'RECURSO': 'string',
    'CARTEIRA_ATUAL':'string',
    'CONTABILIZA_PM':'string',
    'BOOLEAN_STATUS':'int',
    'NOME_PLANO':'string',
    'PEDIDOS_PRIORIZACAO':'string',
    'DISP_CLICK':'string'
}


df_eqm = pd.read_csv(
  ARQUIVO_BASE_EQM,
    sep=';',
    usecols=['UTD','OS_CORRECAO','DEFEITO','POT_DESLIGAMENTO','TIPO_DEFEITO','RECURSO','CARTEIRA_ATUAL','CONTABILIZA_PM','BOOLEAN_STATUS', 'NOME_PLANO','PEDIDOS_PRIORIZACAO','DISP_CLICK'],
    encoding='utf-8',   
    engine='python',
    dtype=dtype_map_eqm
)


#FILTRO_WFM = (df_wfm['Area_Op'].eq('Preventiva'))

FILTRO_EQM= (
  ~df_eqm['TIPO_DEFEITO'].eq('EXTRAS') &
   df_eqm['BOOLEAN_STATUS'].eq(0) & 
  ~df_eqm['DEFEITO'].eq('MANUTENÇÃO COM TURMA PODA') &
  ~df_eqm['DEFEITO'].str.contains('cadastro', case=False, na=False) &
  ~df_eqm['DEFEITO'].str.contains('inspeção', case=False, na=False) 
   #df_eqm['UTD'].eq('ITAPETINGA')
   #df['UTD'].isin(['JACOBINA', 'JUAZEIRO', 'REMANSO', 'SENHOR DO BONFIM','IRECE','ITABERABA','JEQUIE','LIVRAMENTO DE NOSSA SENHORA','SEABRA','BRUMADO','GUANAMBI','ITAPETINGA','VITORIA DA CONQUISTA'])
)

df_wfm_filtrado = df_wfm
df_eqm_filtrado = df_eqm.loc[FILTRO_EQM].copy()

df_eqm_wfm_merged = pd.merge(df_eqm_filtrado, df_wfm_filtrado, left_on="OS_CORRECAO", right_on="Call_id", how="left")

df_eqm_wfm_merged.replace("\\N", np.nan, inplace=True)

df_eqm_wfm_merged['POT_DESLIGAMENTO'] = df_eqm_wfm_merged['POT_DESLIGAMENTO'].str.replace(r'\s+', ' ', regex=True).str.normalize('NFKD').str.encode('ascii','ignore').str.decode('utf-8').str.strip().str.upper()
# === Separação por recurso ===================================================================================================================================

FILTRO_PREV_LV = (
    df_eqm_wfm_merged['CARTEIRA_ATUAL'].eq('ATUAL PROPRIO') &
    df_eqm_wfm_merged['RECURSO'].eq('LINHA VIVA') &
   (~df_eqm_wfm_merged['Skill'].eq('Preventiva_LinhaViva') | df_eqm_wfm_merged['Skill'].isna())

)

FILTRO_PREV_PBT = (
    df_eqm_wfm_merged['CARTEIRA_ATUAL'].eq('ATUAL PROPRIO') &
    df_eqm_wfm_merged['RECURSO'].eq('LINHA MORTA') &
    df_eqm_wfm_merged['TIPO_DEFEITO'].eq('PODA') &
  (~df_eqm_wfm_merged['Skill'].eq('Preventiva_PodaBT') | df_eqm_wfm_merged['Skill'].isna())
)

FILTRO_PREV_REDES = (
    df_eqm_wfm_merged['CARTEIRA_ATUAL'].eq('ATUAL PROPRIO') &
    df_eqm_wfm_merged['RECURSO'].eq('LINHA MORTA') &
    df_eqm_wfm_merged['TIPO_DEFEITO'].eq('ESTRUTURAL') 
    #NECESSARIO VERIFICAR CODIGO PARA ESSA SKILL NA EXTRAÇÃP DO WFM
   
)

FILTRO_PREV_LEVE = (
    df_eqm_wfm_merged['CARTEIRA_ATUAL'].eq('NAO') &
    df_eqm_wfm_merged['RECURSO'].eq('LINHA MORTA') &
    df_eqm_wfm_merged['POT_DESLIGAMENTO'].eq('NAO') &
    df_eqm_wfm_merged['TIPO_DEFEITO'].eq('PODA') &
    (~df_eqm_wfm_merged['NOME_PLANO'].isna()| 
    df_eqm_wfm_merged['CONTABILIZA_PM'].eq('SIM')|
    ~df_eqm_wfm_merged['PEDIDOS_PRIORIZACAO'].isna())

)

df_eqm_wfm_merged_lv = df_eqm_wfm_merged.loc[FILTRO_PREV_LV].copy()
df_eqm_wfm_merged_pbt = df_eqm_wfm_merged.loc[FILTRO_PREV_PBT].copy()
df_eqm_wfm_merged_redes = df_eqm_wfm_merged.loc[FILTRO_PREV_REDES].copy()
df_eqm_wfm_merged_leve = df_eqm_wfm_merged.loc[FILTRO_PREV_LEVE].copy()

# === arquivo tratado ============================================================================================

with pd.ExcelWriter(arquivo_saida, engine='openpyxl') as writer:
    df_eqm_wfm_merged.to_excel(writer, index=False, sheet_name='raw')
    df_eqm_wfm_merged_lv.to_excel(writer, index=False, sheet_name='PREV_LV')
    df_eqm_wfm_merged_pbt.to_excel(writer, index=False, sheet_name='PREV_PBT')
    df_eqm_wfm_merged_redes.to_excel(writer, index=False, sheet_name='PREV_REDES')
    df_eqm_wfm_merged_leve.to_excel(writer, index=False, sheet_name='PREV_LEVE')


    

lote_size = 25 #Definir quantas OS serão processadas por em um lote


df_LM = pd.read_excel(
        arquivo_saida,
        sheet_name='PREV_PBT',
        header= 0,
        dtype=str,
        usecols=['OS_CORRECAO']
)
num_lotes_LM = (len(df_LM) // lote_size) + int(len(df_LM) % lote_size > 0)

df_LV = pd.read_excel(
        arquivo_saida,
        sheet_name='PREV_LV',
        header= 0,
        dtype=str,
        usecols=['OS_CORRECAO']  
)
num_lotes_LV = (len(df_LV) // lote_size) + int(len(df_LV) % lote_size > 0)

df_REDES = pd.read_excel(
        arquivo_saida,
        sheet_name='PREV_REDES',
        header= 0,
        dtype=str,
        usecols=['OS_CORRECAO']  
)
num_lotes_REDES = (len(df_REDES) // lote_size) + int(len(df_REDES) % lote_size > 0)

df_LEVE = pd.read_excel(
        arquivo_saida,
        sheet_name='PREV_LEVE',
        header= 0,
        dtype=str,
        usecols=['OS_CORRECAO']  
)
num_lotes_LEVE = (len(df_LEVE) // lote_size) + int(len(df_LEVE) % lote_size > 0)


print(f"\nQtde OS de LINHA VIVA: {len(df_LV)}")
print(f"Qtde OS poda de LINHA MORTA: {len(df_LM)}")
print(f"\nQtde OS estrutural de LINHA MORTA : {len(df_REDES)}")
print(f"Qtde OS poda de LINHA MORTA fora carteira: {len(df_LEVE)}")
logging.info(f"\nQtde OS de LINHA VIVA: {len(df_LV)}")
logging.info(f"Qtde OS poda de LINHA MORTA: {len(df_LM)}")
logging.info(f"\nQtde OS estrutural de LINHA MORTA : {len(df_REDES)}")
logging.info(f"Qtde OS poda de LINHA MORTA fora carteira: {len(df_LEVE)}")

print(f"\n Qtd de lotes de LM: {num_lotes_LM}")
print(f"\n Qtd de lotes de LV: {num_lotes_LV}")
print(f"\n Qtd de lotes de ESTRUTURAL LM: {num_lotes_REDES}")
print(f"\n Qtd de lotes de LEVE: {num_lotes_LEVE}")
logging.info(f"\n Qtd de lotes de LM: {num_lotes_LM}")
logging.info(f"\n Qtd de lotes de LV: {num_lotes_LV}")
logging.info(f"\n Qtd de lotes de ESTRUTURAL LM: {num_lotes_REDES}")
logging.info(f"\n Qtd de lotes de LEVE: {num_lotes_LEVE}")

def tirar_print():
# Captura a tela
  print("Capturando print...")
  screenshot = pyautogui.screenshot()
  screenshot.save(caminho_destino_prints)


# === Funções para tratar erro/travamento/bug do EQM ====================================================================================

def verificar_erro_eqm()-> int:

 try:

  erro_1 = pyautogui.locateOnScreen(janela_falha_eqm, confidence=0.8)

 except ImageNotFoundException:
            
  erro_1 = None


 if erro_1:
  print("🟨 Identificado falha no EQM")
  logging.info("🟨 Identificado falha no EQM")
  tirar_print()
  pyautogui.click(botao_fechar_janela_falha)
  time.sleep(15)
  return 1
 return 0 




def verificar_travamento_eqm() -> int:
 
 try:

  erro_1 = pyautogui.locateOnScreen(janela_sem_resposta_eqm, confidence=0.8)

 except ImageNotFoundException:
            
  erro_1 = None   

 try:

  erro_2 = pyautogui.locateOnScreen(janela_sem_resposta_eqm_2, confidence=0.8)

 except ImageNotFoundException:
            
  erro_2 = None

 if erro_1 or erro_2:
  print("🟨 Identificado travamento no EQM, reiniciando contador de espera")
  logging.info("🟨 Identificado travamento no EQM, reiniciando contador de espera")
  inicio = time.time()
  return 1
 return 0
  

 
  

def verificar_janela_oculta(janela: str) -> int:

  print("🟨 verificando janela oculta")
  logging.info("verificando janela oculta")
  pyautogui.click(posicao_10)
  time.sleep(5)
  pyautogui.keyDown('alt')
  pyautogui.press('tab')
  pyautogui.keyUp('alt')
  time.sleep(5)

  try:

    confirmacao = pyautogui.locateOnScreen(janela, confidence=0.8)

  except ImageNotFoundException:
            
    confirmacao = None   

  if confirmacao:
    time.sleep(2)
    print("Janela restaurada")
    logging.info("Janela restaurada")
    inicio = time.time()
    return 1
  return 0
      

# === TRACKER DE EXECUÇÃO (tempo + OS programadas + relatório) ============================


   

# === Copiar lote de OS =================================================================================================================

def copiar_os_do_arquivo(df_os, idx):
    
    
    inicio = idx * lote_size
    fim = inicio + lote_size
    df_lote = df_os.iloc[inicio:fim]

    dados = df_lote['OS_CORRECAO'].dropna().astype(str).str.strip().tolist()
    texto_para_copiar = "\n".join(dados)
    pyperclip.copy(texto_para_copiar)

    
    print(f"DEBUG: idx={idx}, inicio={inicio}, fim={fim}")
    print(f"✅ {len(dados)} OS copiadas para a área de transferência.")
    print(f"📋 Lote {idx+1} copiado.")
    logging.info(f"DEBUG: idx={idx}, inicio={inicio}, fim={fim}")
    logging.info(f"✅ {len(dados)} OS copiadas para a área de transferência.")
    logging.info(f"📋 Lote {idx+1} copiado.")


# === abrir janela de pesquisa avançada de OS =======================================================================================

def abrir_janela_selecao():

# abre a janela de pesquisa avançada de OS
  
  pyautogui.click(posicao_1)
  time.sleep(2)
  pyautogui.click(posicao_2)
  time.sleep(2)
  pyautogui.click(posicao_3)
  time.sleep(2)


# === copiar e colar o lote de OS na pesquisa avançada ======================================================================================

def abrir_selecao_colar_os(df_os,idx):

  flag_travamento = 0
  flag_erro = 0
  flag_janela_oculta = 0
  
  timeout_seg = 600   # tempo máximo para tentar (em segundos)
  intervalo_seg = 10  # tempo entre tentativas
    
  inicio = time.time()   
  
# abre a janela de selação de OS, cola as OS do lote, aguarda, seleciona novamente as OS e clica no botão de desbloquear

  while True:
   
        try:

              selecao = pyautogui.locateOnScreen(imagem_janela_selecao, confidence=0.8)

        except ImageNotFoundException:
            
               selecao = None

        if selecao:
            print("Janela de seleção aberta")
            logging.info("Janela de seleção aberta")
            x, y = posicao_4
            if pyautogui.pixel(x,y) != rgb_posicao_4:     
                  pyautogui.click(posicao_4)
                  time.sleep(2)
          
            pyautogui.click(posicao_5)
            time.sleep(2) 
            pyautogui.click(posicao_7)
            time.sleep(2)
            copiar_os_do_arquivo(df_os,idx)
            time.sleep(2)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(2)
            pyautogui.click(posicao_8)
            time.sleep(2)
            pyautogui.click(posicao_9)
            time.sleep(2)

            x, y = posicao_9
            while pyautogui.pixel(x,y) == rgb_posicao_9:
              print("⌛ Esperando mudança visual...")
              logging.info("⌛ Esperando mudança visual...")
              time.sleep(1)
           
            print("✅ Tela carregada!")
            logging.info("✅ Tela carregada!")

            time.sleep(2)
           

            break

        if time.time() - inicio > timeout_seg:
         
         flag_janela_oculta = verificar_janela_oculta(imagem_janela_selecao)

         if flag_janela_oculta == 0:
          print("⏱️ Tempo limite atingido. Abortando seleção")
          logging.info("⏱️ Tempo limite atingido. Abortando seleção")
          tirar_print()
          time.sleep(5)
          sys.exit()
         
        print("⌛ Aguardando janela de seleção...")
        logging.info("⌛ Aguardando janela de seleção...")
        flag_travamento = verificar_travamento_eqm()
        flag_erro = verificar_erro_eqm()

        time.sleep(intervalo_seg)
        pyautogui.click(posicao_10)



# === Desbloquear o lote de OS ===


def desbloquear_os ():
    
    flag_travamento = 0
    flag_erro = 0
    flag_janela_oculta = 0

    timeout_seg = 600   # tempo máximo para tentar (em segundos)
    intervalo_seg = 10  # tempo entre tentativas

    inicio = time.time()


    pyautogui.click(posicao_10)
    time.sleep(2)
    pyautogui.hotkey('ctrl','a')
    time.sleep(2)
    pyautogui.click(posicao_11)
    time.sleep(2)
    pyautogui.click(posicao_12)



    while True:
        
        if flag_erro == 1:
         
         pyautogui.click(posicao_10)
         time.sleep(2)
         pyautogui.hotkey('ctrl','a')
         time.sleep(2)
         pyautogui.click(posicao_11)
         time.sleep(2)
         pyautogui.click(posicao_12) 
         flag_erro = 0         

        try:
            confirmacao = pyautogui.locateOnScreen(imagem_janela_desbloq, confidence=0.8)

        except ImageNotFoundException:
            
            confirmacao = None
    
        if confirmacao:
            print("🟨 Registros desbloqueados com sucesso")
            logging.info("🟨 Registros desbloqueados com sucesso")
            time.sleep(1)
            pyautogui.click(posicao_28)
            time.sleep(1)
            break
        
        if time.time() - inicio > timeout_seg:
         
         flag_janela_oculta = verificar_janela_oculta(imagem_janela_desbloq)

         if flag_janela_oculta == 0:
          print("⏱️ Tempo limite atingido. Abortando seleção")
          logging.info("⏱️ Tempo limite atingido. Abortando seleção")
          tirar_print()
          time.sleep(5)
          sys.exit()
            
                           
        print("⌛ Aguardando janela de confirmação de desbloqueio...")
        logging.info("⌛ Aguardando janela de confirmação de desbloqueio...")
        flag_travamento = verificar_travamento_eqm()
        flag_erro = verificar_erro_eqm()
        
        time.sleep(intervalo_seg)
        pyautogui.click(posicao_10)
              
                                


def desprogramar_os():
  
  timeout_seg = 600   # tempo máximo para tentar (em segundos)
  intervalo_seg = 10  # tempo entre tentativas
  inicio = time.time()


#=== desprogramar o lote de OS ===

  while True:
        
    
        try:
            confirmacao = pyautogui.locateOnScreen(imagem_janela_desprog, confidence=0.9)

        except ImageNotFoundException:
            confirmacao = None
    
        if confirmacao:
            print("🟨 Janela de confirmação de desprogramação detectada")
            logging.info("🟨 Janela de confirmação de desprogramação detectada")
            time.sleep(1)
            pyautogui.click(imagem_botao_yes_desprog)
            time.sleep(2)

            try:

                confirmacao_2 = pyautogui.locateOnScreen(imagem_janela_info_bloqueio, confidence=0.9)

            except ImageNotFoundException:

                confirmacao_2 = None    

            if confirmacao_2:
                print("🟨 Nenhuma OS já programada")
                logging.info("🟨 Nenhuma OS já programada")
                time.sleep(2)
                pyautogui.click(imagem_botao_ok)
                time.sleep(2)
                pyautogui.click(posicao_10)
                time.sleep(2)
                pyautogui.hotkey('ctrl','a')
                time.sleep(2)
                pyautogui.click(posicao_15)
                

                break



            break
        
        if time.time() - inicio > timeout_seg:
         print("⏱️ Tempo limite atingido. Abortando seleção")
         logging.info("⏱️ Tempo limite atingido. Abortando seleção")
         tirar_print()
         sys.exit()
         

        print("⌛ Aguardando janela de confirmação de desprogramação ...")
        logging.info("⌛ Aguardando janela de confirmação de desprogramação ...")
        time.sleep(intervalo_seg)
        pyautogui.click(posicao_10) 


# === Editar o lote de OS ===

def editar_os(label):
    
    flag_travamento = 0
    flag_erro = 0
    flag_janela_oculta = 0   

    timeout_seg = 600   # tempo máximo para tentar (em segundos)
    intervalo_seg = 10  # tempo entre tentativas
    inicio = time.time()
    flag_confirmacao_4 = 0
    flag_confirmacao_2 = 0


    pyautogui.click(posicao_10)
    time.sleep(5)
    pyautogui.hotkey('ctrl','a')
    time.sleep(2)
    pyautogui.click(posicao_15)
    time.sleep(2)



    while True:
        
        
        if flag_erro == 1:
          pyautogui.click(posicao_10)
          time.sleep(5)
          pyautogui.hotkey('ctrl','a')
          time.sleep(2)
          pyautogui.click(posicao_15)
          time.sleep(2)
          flag_erro = 0

        try:
         confirmacao = pyautogui.locateOnScreen(janela_editar_os, confidence=0.8)

        except ImageNotFoundException:
         
         confirmacao = None

        try:
         confirmacao_2 = pyautogui.locateOnScreen(janela_confirm_editar, confidence=0.8)

        except ImageNotFoundException:
         
         confirmacao_2 = None

        if confirmacao_2:

            print("🟨 OS programadas detectadas")
            logging.info("🟨 OS programadas detectadas")
            time.sleep(2)
            pyautogui.click(imagem_botao_yes_desprog)
            time.sleep(1)
            flag_confirmacao_2 = 1

            

    
        if confirmacao:
            
            print("🟨 Janela de edição de OS detectada")
            logging.info("🟨 Janela de edição de OS detectada")
            time.sleep(15)
            pyautogui.click(posicao_16)
            time.sleep(2)
            pyautogui.click(posicao_17)
            time.sleep(2)
            pyautogui.click(posicao_18)
            time.sleep(2)

            inicio = time.time()

            try:

             confirmacao_1_2 = pyautogui.locateOnScreen(janela_edicao_habilidade, confidence=0.8)

            except ImageNotFoundException:

             confirmacao_1_2 = None

            if confirmacao_1_2:
               
               print("🟨 Janela de edição de habilidade da turma detectada")
               logging.info("🟨 Janela de edição de habilidade da turma detectada")
               time.sleep(2)

               if(label == "LM"):
                 pyautogui.write('PREV_PBT')
                 time.sleep(5)
               if(label == "LV"):
                 pyautogui.write('PREV_LV')
                 time.sleep(5)  
               if(label == "REDES"):
                 pyautogui.write('PREV_REDES')
                 time.sleep(5)
               if(label == "LEVE"):
                 pyautogui.write('PREV_LEVE')
                 time.sleep(5)
                                     
               
               
               pyautogui.hotkey('enter')
               time.sleep(5)
               pyautogui.write('1')
               time.sleep(2)
               pyautogui.hotkey('enter')
               time.sleep(5)
               pyautogui.write('NÃO')
               time.sleep(2)
               pyautogui.hotkey('enter')
               time.sleep(5)
               pyautogui.write('S')
               time.sleep(2)
               pyautogui.hotkey('enter')
               time.sleep(5)
               pyautogui.write('EQM')
               time.sleep(2)
               pyautogui.hotkey('enter')
               time.sleep(5)
               pyautogui.click(posicao_19)
               time.sleep(5)
               pyautogui.click(posicao_20)
               time.sleep(2)

               inicio = time.time()

               while True:

                 try:

                  confirmacao_3 = pyautogui.locateOnScreen(imagem_caracteristica_propria_eps, confidence=0.9)

                 except ImageNotFoundException:

                   confirmacao_3 = None

                 if confirmacao_3:

                    print("🟨 campo de caracteristica 'EQUIPE PRÓPRIA OU EPS detectado")
                    logging.info("🟨 campo de caracteristica 'EQUIPE PRÓPRIA OU EPS detectado")
                    pyautogui.click(imagem_caracteristica_propria_eps)
                    time.sleep(5)
                    pyautogui.hotkey('enter')
                    time.sleep(5)
                    pyautogui.write('S')
                    time.sleep(5)
                    pyautogui.click(posicao_19)
                    time.sleep(2)
                    pyautogui.click(posicao_20)
                    time.sleep(2)
                    pyautogui.click(posicao_21)
                    time.sleep(2)

                    inicio = time.time()

                    while True:
                     
                     try:

                      confirmacao_4 = pyautogui.locateOnScreen(janela_atencao_editar_os, confidence=0.8)

                     except ImageNotFoundException:

                      confirmacao_4 = None

                     if confirmacao_4:
                       
                       pyautogui.click(botao_ok_janela_atencao_editar)
                       time.sleep(2)
                       flag_confirmacao_4 = 1
                       break
                     
                     if time.time() - inicio > timeout_seg:
                       
                       flag_janela_oculta = verificar_janela_oculta(janela_atencao_editar_os)
                       
                       if flag_janela_oculta == 0:
                        print("⏱️ Tempo limite atingido. Abortando seleção")
                        logging.info("⏱️ Tempo limite atingido. Abortando seleção")
                        tirar_print()
                        sys.exit()

                   
                     
                     print("⌛ Aguardando confirmação 4 - editar OS...")
                     logging.info("⌛ Aguardando confirmação 4 - editar OS...")
                     verificar_travamento_eqm()
                     verificar_erro_eqm()
                     
                     time.sleep(intervalo_seg)
                     pyautogui.click(posicao_10)

                 if flag_confirmacao_4 == 1:
                    break 

                 print("⌛ Aguardando detecção do campo de caracteristica 'EQUIPE PRÓPRIA OU EPS' ...")
                 logging.info("⌛ Aguardando detecção do campo de caracteristica 'EQUIPE PRÓPRIA OU EPS' ...")
                 pyautogui.scroll(-2000000000)
                 time.sleep(2)
                 pyautogui.scroll(-2000000000)
                 time.sleep(intervalo_seg)

            if flag_confirmacao_4 == 1:
             break      

                 
            print("⌛ Aguardando detecção da janela de edição de características ...")
            logging.info("⌛ Aguardando detecção da janela de edição de características ...")
            flag_travamento = verificar_travamento_eqm()
            flag_erro = verificar_erro_eqm()
            time.sleep(intervalo_seg)   
            pyautogui.click(posicao_10) 



        if flag_confirmacao_4 == 1:
         break 
      

        if time.time() - inicio > timeout_seg:
         
         flag_janela_oculta = verificar_janela_oculta(janela_editar_os)
          
         if flag_janela_oculta == 0:

           print("⏱️ Tempo limite atingido. Abortando seleção")
           logging.info("⏱️ Tempo limite atingido. Abortando seleção")
           tirar_print()
           sys.exit()
         

        print("⌛ Aguardando janela de edição de OS...")
        logging.info("⌛ Aguardando janela de edição de OS...")
        flag_travamento = verificar_travamento_eqm()
        flag_erro = verificar_erro_eqm()
        time.sleep(intervalo_seg)
        pyautogui.click(posicao_10)




def programar_os(idx):
    
    flag_travamento = 0
    flag_erro = 0
    flag_janela_oculta = 0 
    
    timeout_seg = 600   # tempo máximo para tentar (em segundos)
    intervalo_seg = 10  # tempo entre tentativas
    inicio = time.time()

    flag_confirmacao_3 = 0
    flag_confirmacao_2 = 0
    flag_sucesso = 0


    time.sleep(30)
    pyautogui.click(posicao_10)
    time.sleep(2)
    pyautogui.hotkey('ctrl','a')
    time.sleep(2)
    pyautogui.click(posicao_13)
    time.sleep(2)
    pyautogui.click(posicao_22)
    

    while True:
        
        if flag_erro == 1:
          pyautogui.click(posicao_10)
          time.sleep(2)
          pyautogui.hotkey('ctrl','a')
          time.sleep(2)
          pyautogui.click(posicao_13)
          time.sleep(2)
          pyautogui.click(posicao_22)


        try:
         
         confirmacao = pyautogui.locateOnScreen(janela_confirm_programar, confidence=0.8)

        except ImageNotFoundException:
         
         confirmacao = None
        

        
        if confirmacao:

            print("🟨 Janela de confirmação de programação de OS detectada")
            logging.info("🟨 Janela de confirmação de programação de OS detectada")
            time.sleep(2)
            pyautogui.click(imagem_botao_yes_desprog)
            time.sleep(1)

            inicio = time.time()

            while True:
             
               if flag_erro == 1:
                pyautogui.click(posicao_10)
                time.sleep(2)
                pyautogui.hotkey('ctrl','a')
                time.sleep(2)
                pyautogui.click(posicao_13)
                time.sleep(2)
                pyautogui.click(posicao_22)               
               
               try:
         
                confirmacao_1_2 = pyautogui.locateOnScreen(janela_aviso_editar_programadas, confidence=0.8)

               except ImageNotFoundException:
         
                confirmacao_1_2 = None
               
               try:
         
                confirmacao_2 = pyautogui.locateOnScreen(janela_programar_lote, confidence=0.8)

               except ImageNotFoundException:
         
                confirmacao_2 = None

               try:
         
                confirmacao_3 = pyautogui.locateOnScreen(janela_aviso_programar_lote, confidence=0.8)

               except ImageNotFoundException:
         
                confirmacao_3 = None


                if confirmacao_1_2:

                 print("🟨 Janela de aviso de edição de OS programadas detectada")
                 logging.info("🟨 Janela de aviso de edição de OS programadas detectada")
                 time.sleep(2)
                 pyautogui.click(posicao_10)
                 time.sleep(2)
                 pyautogui.click(botao_sim_aviso_programar_lote)


               if confirmacao_3:
                  
                  if flag_confirmacao_3 == 0:
                   print("🟨 Janela de aviso de substituição de lote de OS detectada")
                   logging.info("🟨 Janela de aviso de substituição de lote de OS detectada")
                   time.sleep(2)
                   pyautogui.click(posicao_10)
                   time.sleep(2)
                   pyautogui.click(botao_sim_aviso_programar_lote)
                   time.sleep(2)
                   flag_confirmacao_3 = 1

                  

        
               if confirmacao_2:
                 
                 if flag_confirmacao_2 == 0:

                  #pyautogui.displayMousePosition()
 

                  print("🟨 Janela de programação de lote de OS detectada")
                  logging.info("🟨 Janela de programação de lote de OS detectada")
                  time.sleep(2)

                 

                  pyautogui.click(posicao_24)
                  time.sleep(2)
                  pyautogui.write('01')
                  time.sleep(2)
                  pyautogui.hotkey('enter')
                  time.sleep(2)
                  
                  
                   
                  pyautogui.doubleClick(posicao_25) 
                  time.sleep(2)
                  pyautogui.write(f'{amanha:%d/%m/%Y}')
                  time.sleep(2)
                  pyautogui.hotkey('enter')
                  time.sleep(2)

                  

                  pyautogui.doubleClick(posicao_26)
                  time.sleep(2)
                  pyautogui.write('31/12/2026')
                  time.sleep(2)
                  pyautogui.hotkey('enter')
                  time.sleep(2)
                   
                  

                  pyautogui.click(posicao_27)
                  time.sleep(2)
                  pyautogui.write('30')
                  time.sleep(2)
                  pyautogui.hotkey('enter')
                  time.sleep(2)                
                  pyautogui.click(posicao_23)
                   

                 flag_confirmacao_2 = 1

                 inicio = time.time()
                   
                 while True:
                      
           
                      try:
         
                       confirmacao_4 = pyautogui.locateOnScreen(janela_confirm_programar_final, confidence=0.8)
 
                      except ImageNotFoundException:
         
                       confirmacao_4 = None

                      if confirmacao_4:
                          
                          print("🟨 Janela de confirmação de programação de lote de OS detectada")
                          logging.info("🟨 Janela de confirmação de programação de lote de OS detectada")
                          time.sleep(2)
                          pyautogui.click(imagem_botao_yes_desprog)
                          time.sleep(2)

                          inicio = time.time()

                          while True:
                      
                           try:
         
                             confirmacao_5 = pyautogui.locateOnScreen(janela_confirm_programar_final, confidence=0.8)
 
                           except ImageNotFoundException:
         
                              confirmacao_5 = None

                           try:
         
                             confirmacao_6 = pyautogui.locateOnScreen(janela_operacao_efetuada_sucesso, confidence=0.8)
 
                           except ImageNotFoundException:
         
                              confirmacao_6 = None 


                           if confirmacao_5:
                             
                             print("🟨 Janela de confirmação de programação de lote de OS detectada")
                             logging.info("🟨 Janela de confirmação de programação de lote de OS detectada")
                             time.sleep(2)
                             pyautogui.click(imagem_botao_yes_desprog)
                             time.sleep(2)
                             
                             break
                           
                           if confirmacao_6:
                             
                             print(f"🟨 programação do lote {idx + 1} efetuado com sucesso")
                             logging.info(f"🟨 programação do lote {idx + 1} efetuado com sucesso")
                             time.sleep(2)
                             pyautogui.click(botao_ok_sucesso)
                             time.sleep(2)
                             flag_sucesso = 1 

                             break



                           print("⌛ aguardando confirmação final de programação do lote")
                           logging.info("⌛ aguardando confirmação final de programação do lote")
                           flag_travamento = verificar_travamento_eqm()
                           flag_erro = verificar_erro_eqm()
                           time.sleep(intervalo_seg)
                           pyautogui.click(posicao_10)

                      if flag_sucesso == 1 :
                        time.sleep(2)
                        break



                      if time.time() - inicio > timeout_seg:

                        flag_janela_oculta = verificar_janela_oculta(janela_confirm_programar_final)

                        if flag_janela_oculta == 0:
                        
                         print("⏱️ Tempo limite atingido. Abortando seleção")
                         logging.info("⏱️ Tempo limite atingido. Abortando seleção")
                         tirar_print()
                         sys.exit()
                        
               
                      print("⌛ aguardando janela de confirmação de programação de lote de OS...")
                      logging.info("⌛ aguardando janela de confirmação de programação de lote de OS...")                      
                      flag_travamento = verificar_travamento_eqm()
                      flag_erro = verificar_erro_eqm()                      
                      time.sleep(intervalo_seg)
                      pyautogui.click(posicao_10)


               if flag_sucesso == 1 :
                  time.sleep(2)
                  break          
              
               
               if time.time() - inicio > timeout_seg:
                  
                  
                 flag_janela_oculta = verificar_janela_oculta(janela_programar_lote)

                 if flag_janela_oculta == 0:
                        
                    print("⏱️ Tempo limite atingido. Abortando seleção")
                    logging.info("⏱️ Tempo limite atingido. Abortando seleção")
                    tirar_print()
                    sys.exit()
               
               
               print("⌛ aguardando janela de programação de lote de OS...")
               logging.info("⌛ aguardando janela de programação de lote de OS...")
               flag_travamento = verificar_travamento_eqm()
               flag_erro = verificar_erro_eqm()
               time.sleep(intervalo_seg)
               pyautogui.click(posicao_10)
        
    
        
        
        if flag_sucesso == 1 :
          time.sleep(2)
          break       

        if time.time() - inicio > timeout_seg:

          flag_janela_oculta = verificar_janela_oculta(janela_confirm_programar)

          if flag_janela_oculta == 0:
                        
           print("⏱️ Tempo limite atingido. Abortando seleção")
           logging.info("⏱️ Tempo limite atingido. Abortando seleção")
           tirar_print()
           sys.exit()
        

        
        print("⌛ Aguardando janela de confirmação de programação de OS...")
        logging.info("⌛ Aguardando janela de confirmação de programação de OS...")
        flag_travamento = verificar_travamento_eqm()
        flag_erro = verificar_erro_eqm()
        time.sleep(intervalo_seg)
        pyautogui.click(posicao_10)


                



# === rotina do robô ===
  

def processar_lotes(df_os, num_lotes, label, start_lote=1):
  
  
  # usar para testar rotinas | 1 para pular rotina
  pular1 = 0
  pular2 = 0
  pular3 = 0
  pular4 = 0
  pular5 = 0
  

  


  for idx in range(start_lote-1,num_lotes):
   
   

   print(f"\n=== Iniciando lote {idx+1}/{num_lotes} [{label}] ===")
   logging.info(f"\n=== Iniciando lote {idx+1}/{num_lotes} [{label}] ===")

  

   if pular1 == 1:
    print("🛑 Interrupção manual 1 detectada. Pulando etapa.")
   else:
    abrir_janela_selecao()

   
   if pular2 == 1:
    print("🛑 Interrupção manual 2 detectada. Pulando etapa.")
   else:
    abrir_selecao_colar_os(df_os, idx)

   time.sleep(2)

# === desbloquear o lote de OS ===

   if pular3 == 1:
    print("🛑 Interrupção manual 3 detectada. Pulando etapa.")
   else:
    desbloquear_os()

   time.sleep(2)

   
   if pular4 == 1:
    print("🛑 Interrupção manual 4 detectada. Pulando etapa.")
   else:
    editar_os(label)
   
   time.sleep(2)

   if pular5 == 1:
     print("🛑 Interrupção manual 5 detectada. Pulando etapa.")
   else:
     programar_os(idx)
  
  #  if (flag_sucesso == idx + 1):
  #    print(f"Lote ({label}): {flag_sucesso} programado com sucesso!")

# if num_lotes_REDES > 2:
#      processar_lotes(df_REDES, num_lotes_REDES, "REDES",start_lote=1)   

# if num_lotes_LM > 0:
#     processar_lotes(df_LM, num_lotes_LM, "LM",start_lote=1)

if num_lotes_LV > 0:
    processar_lotes(df_LV, num_lotes_LV, "LV",start_lote=9)

if num_lotes_LEVE > 0:
    processar_lotes(df_LEVE, num_lotes_LEVE, "LEVE",start_lote=1)
 


