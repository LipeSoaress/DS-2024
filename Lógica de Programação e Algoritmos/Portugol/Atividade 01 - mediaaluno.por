programa {
  funcao inicio() {
    real numero_1
    real numero_2
    real numero_3
    real soma

    escreva("Digite o primeiro número: ")
    leia(numero_1)

    escreva("Digite o segundo número: ")
    leia(numero_2)

    escreva("Digite o segundo número:")
    leia(numero_3)
    
    soma = (numero_1 + numero_2 + numero_3) / 3

    limpa()
    
    escreva("A média do aluno é: ", soma)

    se(soma >= 7) {
    	escreva("\nAluno aprovado")
    } senao se(soma >= 3){
    	escreva("\nAluno em Recuperação") 
    } senao {
    	escreva("\nAluno reprovado")
    }
  }
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 575; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */