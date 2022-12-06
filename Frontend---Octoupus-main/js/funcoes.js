function validar() {
    let foto = document.getElementById('imagem').value
    let codig = document.getElementById('codigo').value
    let nome = document.getElementById('nome').value
    let quantidade = document.getElementById('quantidade').value

    if (foto == '', codig == '', nome == '', quantidade == '') {
        alert('Todos os campos devem ser preenchidos')
    }
    else {
        cadastrarprodutos(foto, codig, nome, parseInt(quantidade))
    }
}

function cadastrarprodutos(imagem, codig, nome, qtidade) {
    let novoprod = {imagem, codig, nome, qtidade};
    let produtos = localStorage.getItem("produtos")
    if (produtos == null) {produtos = []}
    else {produtos = JSON.parse(produtos)}
    produtos.push(novoprod);
    localStorage.setItem("produtos", JSON.stringify(produtos));
    location.reload();
}


function inventario() {
    if(typeof(Storage) != "undefined") {
        let produtos = localStorage.getItem("produtos");
        if(produtos == null) {
            document.write("<p>Ainda não há itens cadastrados</p>")
        }
        else {
            produtos = JSON.parse(produtos)
            produtos.forEach(produto => {
                document.write("<ul>");
                document.write("<li>Imagem do Produto:"+produto.imagem+"</li>")
                document.write("<li>Codigo de barras:"+produto.codig+"</li>")
                document.write("<li>Nome do Produto:"+produto.nome+"</li>")
                document.write("<li>Quantidade do Produto:"+produto.qtidade+"</li>")
                document.write("</ul>");
            });
        }
    }
}
