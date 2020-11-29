
function capture() {
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

		cell2.className = 'coluna-nome-advogado';
		cell1.className = 'coluna-num-oab';
		cell3.className = 'coluna-btn';
		
		if(isLawyerEqual(oab)){
			cell1.innerHTML = oab;
			cell2.innerHTML = name;
			cell3.innerHTML = '<input type="button" class="btn btn-danger" id = "btn-remove" value="X" onclick="deleteRow(this)"/>';
			
		}else{
			alert("Advogado já adicionado!");
		}
		clearInput('oab');
		clearInput('name-advogado');
		
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

	if(isEmpty(nameTask) || isEmpty(descricao) || !thereIsLawyer()){
		alert("Por favor, digite todos os dados da tarefa!");
	}
	else{
		ajaxTask(nameTask,descricao);
		
		//clearAllInputs();
		//clearTable();
	}
}

function clearAllInputs(){
	clearInput('oab');
	clearInput('name-task');
	clearInput('name-advogado');
	clearInput('desc');
}

function thereIsLawyer(){
	let table = document.getElementById("Tabela");
	let linhas = table.rows;
	return (linhas.length > 0);
}

function isLawyerEqual(str){
	let colunas = document.getElementsByClassName('coluna-num-oab');
	for (let i = 0; i < colunas.length; i = i+1){
		if(colunas[i].innerText === str){
			return false;
		}
	}
	return true;
}

function ajaxTask(taskNome,taskDesc){
	$.ajax({
		url:'http://127.0.0.1:8080/task/save',
		method: "POST",
		data: JSON.stringify({
			"nome" : taskNome,
			"descricao": taskDesc
		}),
		dataType: "json",
		contentType: "application/json",
        success:function(responsedata){
			addLawyer(responsedata["msg"]["task_id"]);
        }
	 })
	 
}

function addLawyer(id){
	let oab = document.getElementsByClassName('coluna-num-oab');
	let name = document.getElementsByClassName('coluna-nome-advogado');
	console.log(oab);
	for (let i = 0; i < oab.length; i = i+1){
		ajaxLawyer(id, name[i].innerText, oab[i].innerText);
	}
}

function ajaxLawyer(id, name, oab){
	$.ajax({
		url:'http://127.0.0.1:8080/lawyer/save',
		method: "POST",
		data: JSON.stringify({
			"task_id": id,
			"nome": name,
			"oab": oab
		}),
		dataType: "json",
		contentType: "application/json",
        success:function(responsedata){
			console.log(responsedata)
        }
	 })	 
}

