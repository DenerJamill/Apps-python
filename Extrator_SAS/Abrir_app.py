import os
import pyautogui
from time import sleep
import signal
import subprocess
import psutil as psutil


def exporta_arquivo(arq):
    """
    BOT criado para automatizar o processo de exportar o programa completo de um projeto SAS 7.1
    :param arq: Arquivo a ser aberto
    :Saída: Arquivo .sas exportado
    """
    arquivo = arq
    shell_process = subprocess.Popen([arquivo], shell=True)
    aberto = pyautogui.locateOnScreen('sas_guide.PNG')

    def mover_mouse():
        pyautogui.moveTo(660, 0)

    cont = 0
    while aberto is None:
        # sleep()
        aberto = pyautogui.locateOnScreen('sas_guide.PNG')
        if cont == 0:
            print('Abrindo programa! Aguarde...', end='')
            cont += 1
        else:
            print('.', end='')
    print()
    sleep(3)
    arquivo_em_uso = pyautogui.locateOnScreen('arquivo_em_uso.PNG')
    if arquivo_em_uso is not None:
        aeu_no = pyautogui.locateOnScreen('server_nao.PNG')
        pyautogui.click(aeu_no)
        mover_mouse()
        sleep(1)
    change_server = pyautogui.locateOnScreen('change_server.PNG')
    if change_server is not None:
        nao_server = pyautogui.locateCenterOnScreen('server_nao.PNG')
        pyautogui.click(nao_server)
        mover_mouse()
        sleep(1)
    print('Iniciando operações.')
    pyautogui.press(['alt', 'f'])
    sleep(1)
    pyautogui.press('r')
    sleep(1)
    bloqueado = pyautogui.locateCenterOnScreen('bloqueado.png')
    erro = pyautogui.locateCenterOnScreen('erro.PNG')
    if bloqueado is not None or erro is not None:
        pass

    else:
        pyautogui.press('l')
        sleep(1)
        x = 0
        y = 0
        cont = 0
        alerta = pyautogui.locateOnScreen('alerta.PNG')
        alerta2 = pyautogui.locateOnScreen('erro.PNG')
        while x == 0 and cont < 300:
            export = pyautogui.locateCenterOnScreen('dialogo_export.PNG')
            if alerta is None and alerta2 is None and export is None:
                alerta = pyautogui.locateOnScreen('alerta.PNG')
                alerta2 = pyautogui.locateOnScreen('erro.PNG')
                cont += 1
                print(f'.', end='')
                # sleep(0.5)
            elif (alerta is not None or alerta2 is not None) and y == 0:
                pyautogui.press('enter')
                mover_mouse()
                y += 1
            elif export is not None:
                pyautogui.click(export)
                mover_mouse()
                x += 1
        if cont == 300:
            print('Não achei as opções de exportações. Encerrando Programa...')
        sleep(1)
        replace = pyautogui.locateOnScreen('replace.PNG')
        if replace is not None:
            replace_sim = pyautogui.locateCenterOnScreen('replace_sim.PNG')
            pyautogui.click(replace_sim)
            mover_mouse()
            sleep(1)

        encode = pyautogui.locateOnScreen('alerta.PNG')
        if encode is not None:
            encode_sim = pyautogui.locateOnScreen('replace_sim.PNG')
            pyautogui.click(encode_sim)
            sleep(1)

    parent = psutil.Process(shell_process.pid)
    children = parent.children(recursive=True)
    child_pid = children[0].pid
    os.kill(child_pid, signal.SIGTERM)
    os.kill(shell_process.pid, signal.SIGTERM)
    print('\nPrograma encerrado!')