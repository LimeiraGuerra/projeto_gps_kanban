function capturar() {
	if (document.getElementById('name-advogado').value == '' || document.getElementById('oab').value == '') {

		alert("Por favor, digite novamente os dados do advogado!")
	}
	else {
		var name = document.getElementById('name-advogado').value;
		var oab = document.getElementById('oab').value;

		var table = document.getElementById('Tabela');

		var newRow = table.insertRow(0);

		var cell1 = newRow.insertCell(0);
		var cell2 = newRow.insertCell(1);
		var cell3 = newRow.insertCell(2);

		cell1.className = 'coluna-nome-advogado';
		cell2.className = 'coluna-num-oab';
		cell3.className = 'coluna-btn';

		cell1.innerHTML = oab;
		cell2.innerHTML = name;
		cell3.innerHTML = '<input type="button" class="btn btn-danger" id = "btn-remove" value="X" onclick="deleteRow(this)"/>';
	}

}
function deleteRow(t) {
	var row = t.parentNode.parentNode;
	document.getElementById("Tabela").deleteRow(row.rowIndex);
	console.log(row);

}

function addTask(){
	let taskNome = document.getElementById("name-adv").value;
	let taskDesc = document.getElementById("desc").value;
	//$("#form-task").ajaxForm // https://stackoverflow.com/questions/18614240/jquery-form-not-working-as-expected-ajaxform-is-not-a-function
	$.ajax({
		url:'http://localhost:8080/task/save',
		method: "POST",
		data: JSON.stringify({
			"nome" : taskNome,
			"descricao": taskDesc
		}),
		dataType: "json",
		contentType: "application/json",
        success:function(responsedata){
			addLawyer(responsedata["msg"]["id"]);
			console.log(responsedata)
        }
	 })
	 
}

function addLawyer(id){

}
