programa{
	funcao inicio(){
		inteiro inf
		
		escreva("digite o número: ")
		leia(inf)

		limpa()

		se(inf == 1){
			escreva("Janeiro")
		}senao se(inf == 2){
			escreva("Fevereiro")
		}senao se(inf == 3){
			escreva("Março")
		}senao se(inf == 4){
			escreva("Abril")
		} senao se(inf == 5){
			escreva("Maio")
		} senao se(inf == 6){
			escreva("Junho")
		} senao se(inf == 7){
			escreva("Julho")
		} senao se(inf == 8) {
			escreva("Agosto")
		}senao se (inf == 9){
			escreva("Setembro")
		}senao se (inf == 10){
			escreva("Outubro")
		}senao se (inf == 11){
			escreva("Novembro")
		}senao se (inf == 12){
			escreva("Dezembro")
		}senao {
			escreva("mês invalido")
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 647; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */