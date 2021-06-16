function cadastrar() {
  var name = $("#name").val()
  var email= $("#email").val()
  var address= $("#address").val()
  var city = $("#city").val()
  var state= $("#state").val()
  var cep= $("#cep").val()

  var settings = {
    "url": "http://localhost:5000/cadastrar",
    "method": "POST",
    "timeout": 0,
    "headers": {
      "Content-Type": "application/x-www-form-urlencoded"
    },
    "data": {
      "name": name,
      "email": email,
      "address": address,
      "city": city,
      "state": state,
      "cep": cep
    }
  }

  $.ajax(settings).done(function (response) {
    console.log(response)
  })
}
function cadastro(){
  window.location.replace("/")
}
function pesquisar(){
  window.location.replace("/pesquisar")
}
function busca(){
  var name= $("#name").val()

  window.location.replace("/busca?name=" + name)
}

function editar(){
  window.location.replace("/editar")
}

function pesquisa_edit(){
  var name= $("#name").val()
  window.location.replace("/infoedit?name=" + name)
}

function buscar_deletar(){
  window.location.replace("/delete")
}
function pesquisa_delete(){
  var name= $("#name").val()
  window.location.replace("/info_delete?name=" + name)
}

function edit(){
  var name= $("#name").val()
  var email= $("#email").val()
  var address= $("#address").val()
  var city= $("#city").val()
  var state= $("#state").val()
  var cep= $("#cep").val()

  var settings = {
    "url": "http://localhost:5000/edit",
    "method": "PUT",
    "timeout": 0,
    "headers": {
      "Content-Type": "application/x-www-form-urlencoded"
    },
    "data": {
      "name": name,
      "email": email,
      "address": address,
      "city": city,
      "state": state,
      "cep": cep
    }
  };

  $.ajax(settings).done(function (response) {
    if (response==200) {
        window.location.replace("/busca?name=" + name)
    }
    else {
      alert("alguma coisa deu errado!!")
    }
  })
}
function deletar(){
  var name= $("#name").val()
  var email= $("#email").val()
  var address= $("#address").val()
  var city= $("#city").val()
  var state= $("#state").val()
  var cep= $("#cep").val()

  var settings = {
    "url": "http://localhost:5000/deletar",
    "method": "DELETE",
    "timeout": 0,
    "headers": {
      "Content-Type": "application/x-www-form-urlencoded"
    },
    "data": {
      "name": name,
      "email": email,
      "address": address,
      "city": city,
      "state": state,
      "cep": cep
    }
  };
  $.ajax(settings).done(function (response) {
    if (response==200) {
        window.location.replace("/")
    }
    else {
      alert("alguma coisa deu errado!!")
    }
  })
}
