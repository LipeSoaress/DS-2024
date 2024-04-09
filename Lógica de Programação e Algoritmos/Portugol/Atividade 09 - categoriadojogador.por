programa{
	funcao inicio(){
		inteiro idd

		escreva("Qual é a Idade do Jogardor: ")
		leia(idd)
		
		limpa()
		
		se(idd <= 13){
			escreva("Sua Categoria é infantil")
		} senao se (idd <= 17){
			escreva("Sua Categoria é juvenil")
		}senao se (idd > 17){
			escreva("Sua Categoria é Sênior")
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 103; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */