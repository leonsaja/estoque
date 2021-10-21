var saldo = document.querySelector("#id_estoque-0-saldo"),
	quanti = document.querySelector("#id_estoque-0-quantidade");

quanti.addEventListener('change', ProdutoJson);
    
async function ProdutoJson() {
    console.log("teste");
    var produtos = await fetch(`http://localhost:8000/produto/1/json`),
			data = await produtos.json();
    var estoque=data.data[0].estoque;
    var quantidade = parseInt( quanti.value);
    console.log('quant',quantidade);

    if (quantidade <= 0) {
			alert("Quantidade não permitida !");
		} else {
			var total = quantidade+ estoque;
			saldo.value = total;
		}
       
    console.log(total);

}


