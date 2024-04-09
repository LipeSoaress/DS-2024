programa{
	
	funcao inicio() {
	inteiro livro

		escreva("A: R$ 0,25 por livro + R$ 7,50 fixo")
		escreva("\nB: R$ 0,50 por livro + R$ 2,50 fixo")
		escreva("\naQuantos livros você deseja: ")
		leia(livro)

		limpa()

		se (livro < 20){
			escreva("A melhor opção é a A")
		}senao se (livro == 20){
			escreva("oOs dois dão o mesmo desconto")
		} senao
			escreva("A melhor é a B")
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 346; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */