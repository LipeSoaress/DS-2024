programa {
	funcao inicio() {
		real n1, inf, tx

		escreva("A Taxação Atual? ")
		leia(tx)
		escreva("\nQual será a conversão?")
		escreva("\n[1] Real para Dolar")
		escreva("\n[2] Dolar para Real")
		escreva("\nEscolha: ")
		leia(n1)

		limpa()

		se(n1 == 1){
		escreva("Digite o Valor: ")
		leia(inf)
		escreva("USD: ", (inf/tx))
		}senao se(n1 == 2){
		escreva("Digite o Valor: ")
		leia(inf)
		escreva("\nBRL: ", (tx*inf))
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 83; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */