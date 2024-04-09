programa{
	funcao inicio(){
		cadeia inf
		
		escreva("digite o dia da semana: ")
		leia(inf)

		limpa()

		se(inf == "2"){
			escreva("segunda")
		}senao se(inf == "3"){
			escreva("terça")
		}senao se(inf == "4"){
			escreva("quarta")
		}senao se(inf == "5"){
			escreva("quinta")
		} senao se(inf == "6"){
			escreva("sexta")
		} senao se(inf == "7"){
			escreva("sábado")
		} senao se(inf == "1"){
			escreva("domingo")
		} senao {
			escreva("digite o dia da semana: ")
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 434; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */