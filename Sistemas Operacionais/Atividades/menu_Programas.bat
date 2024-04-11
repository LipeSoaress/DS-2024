@echo off
::BIBLIOTECA (DIC.) UTF-8
chcp 65001 >nul 
:loop
echo Escolha uma opção
echo 1 - Abrir Calculadora
echo 2 - Abrir Bloco de Notas
echo 3 - Abrir Paint

::CRIAR UMA VARIÁVEL E ATRIBUIR VALOR
set /p opcao="Digite sua opção: "

if "%opcao%"=="1" (
	start calc.exe
)
if "%opcao%"=="2" (
	start notepad.exe
)
if "%opcao%"=="3" (
	start mspaint.exe
)
cls
goto loop