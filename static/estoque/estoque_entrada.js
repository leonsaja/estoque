var campo_saldo = document.querySelector("#id_estoque-0-saldo"),
	quantidade = document.querySelector("#id_estoque-0-quantidade"),
	produto = document.querySelector("#id_estoque-0-produto"),
	campo1 = document.querySelector(".id_saldo");

campo_saldo.setAttribute("type", "hidden");
campo1.textContent = "";

function ProdutoId() {
	return (pk = produto.value);
}

$(document).on("change", produto, function () {
	let pk = ProdutoId();
	let url = "/produto/" + pk + "/json";

	$.ajax({
		url: url,
		type: "GET",
		success: function (response) {
			estoque = response.data[0].estoque;
			var quant = quantidade.value;
			var total = Number(estoque) + Number(quant);
			campo1.textContent = total;

			if (campo1.innerHTML < 0) {
				campo1.innerHTML = "";
				quantidade.value = "";
			
				alert("O saldo não pode ser negativo.");
			}
			campo_saldo.value = total;
		},
		error: function (xhr) {
			// body...
		},
	});
});

// async function ProdutoJson() {
// 	var idProduto = ProdutoId();
// var produtos = await fetch(`http://localhost:8000/produto/${idProduto}/json`);
// 	var data = await produtos.json();
// 	var estoque = data.data[0].estoque;

// 	if (campo1.innerHTML < 0) {
// 		campo1.innerHTML = "";
// 		alert("O saldo não pode ser negativo.");
// 	}
// }
