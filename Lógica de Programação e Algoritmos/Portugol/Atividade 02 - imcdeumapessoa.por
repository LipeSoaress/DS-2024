programa {
  funcao inicio() {
  real altura
  real peso
  real imc

   escreva("Digite sua altura:")
   leia(altura)

   escreva("Digite seu peso:")
   leia(peso)

   imc = peso / (altura * altura)
 
   escreva("o IMC será: ", imc)
   escreva("\nAltura informada:", altura)
   escreva("\nPeso informado:", peso)

    se(imc > 30) {
    	 escreva("\nCuidado com a Saúde")
    } senao {
    	escreva("\nTudo Ok")
    }
   
  }
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 67; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */