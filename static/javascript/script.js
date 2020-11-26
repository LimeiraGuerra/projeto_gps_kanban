
function capturar() {
	let name = document.getElementById('name-advogado').value.trim();
	let oab = document.getElementById('oab').value.trim();

	if (isEmpty(name) || isEmpty(oab) ) {
		alert("Por favor, digite novamente os dados do advogado!");
	}
	else {
		
		let table = document.getElementById('Tabela');

		let newRow = table.insertRow(0);

		let cell1 = newRow.insertCell(0);
		let cell2 = newRow.insertCell(1);
		let cell3 = newRow.insertCell(2);

		cell1.className = 'coluna-nome-advogado';
		cell2.className = 'coluna-num-oab';
		cell3.className = 'coluna-btn';

		cell1.innerHTML = oab;
		cell2.innerHTML = name;
		cell3.innerHTML = '<input type="button" class="btn btn-danger" id = "btn-remove" value="X" onclick="deleteRow(this)"/>';
		clearInput('oab');
		clearInput('name-advogado')
	}

}
function deleteRow(t) {
	let row = t.parentNode.parentNode;
	document.getElementById("Tabela").deleteRow(row.rowIndex);
}

function clearTable(){
	let table = document.getElementById("Tabela");
	let linhas = table.rows;
	for (let i = linhas.length-1; i >= 0; i = i-1){
		table.deleteRow(i);
	}
}

function cancel(){
	clearTable();
	clearAllInputs();
}

function clearInput(idInput){
	document.getElementById(idInput).value = '';
}

function isEmpty(str) {
    return (str.length === 0);
}

function addTask(){
	let nameTask = document.getElementById('name-task').value.trim();
	let descricao = document.getElementById('desc').value.trim();

	if(isEmpty(nameTask) || isEmpty(descricao)){
		alert("Por favor, digite todos os dados da tarefa!");
	}
	else{
		alert("vai ser add");
		clearTable();
		clearAllInputs();
	}
	
}

function clearAllInputs(){
	clearInput('oab');
	clearInput('name-task');
	clearInput('name-advogado');
	clearInput('desc');
}
