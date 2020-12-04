
function capture() {
	let name = document.getElementById('name-advogado').value.trim();
	let oab = document.getElementById('oab').value.trim();

	if (isEmpty(name) || isEmpty(oab)) {
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
		cell3.className = 'coluna-btn btn-danger btn-remove';

		if (isLawyerEqual(oab)) {
			cell1.innerHTML = oab;
			cell2.innerHTML = name;
			cell3.innerHTML = '<i class="material-icons icon-remove">close</i>';
			cell3.addEventListener("click", ()=>{deleteRow(cell3)});
			//'<button class="btn btn-danger btn-remove p-0" onclick="deleteRow(this)"/><i class="material-icons icon-remove">close</i></button>';
		
		} else {
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

function clearTable() {
	let table = document.getElementById("Tabela");
	let linhas = table.rows;
	for (let i = linhas.length - 1; i >= 0; i = i - 1) {
		table.deleteRow(i);
	}
}

$('#formModal').on('hide.bs.modal', ()=> {
	clearTable();
	clearAllInputs();
});

function clearInput(idInput) {
	document.getElementById(idInput).value = '';
}

function isEmpty(str) {
	return (str.length === 0);
}

function addTask() {
	let nameTask = document.getElementById('name-task').value.trim();
	let descricao = document.getElementById('desc').value.trim();

	if (isEmpty(nameTask) || isEmpty(descricao) || !thereIsLawyer()) {
		alert("Por favor, digite todos os dados da tarefa!");
	}
	else {
		newTask(getFormTaskJson(nameTask, descricao));
	}
}

function clearAllInputs() {
	clearInput('oab');
	clearInput('name-task');
	clearInput('name-advogado');
	clearInput('desc');
}

function thereIsLawyer() {
	let table = document.getElementById("Tabela");
	let linhas = table.rows;
	return (linhas.length > 0);
}

function isLawyerEqual(str) {
	let colunas = document.getElementsByClassName('coluna-num-oab');
	for (let i = 0; i < colunas.length; i = i + 1) {
		if (colunas[i].innerText === str) {
			return false;
		}
	}
	return true;
}

function newTask(taskJson) {
	$.ajax({
		url:'/task/save',
		method: "POST",
		data: taskJson,
		dataType: "json",
		contentType: "application/json"
	}).done((data) => {
		if (data.success){
			addTaskToView("colunaAberto", data.response);
			$('#formModal').modal('hide')
		}
		else{
			alert("Algum erro aconteceu!");
		}	
		resetJqueryFuncs();
	});
}

function getFormTaskJson(taskNome, taskDesc) {
	return JSON.stringify({
		"name": taskNome,
		"desc": taskDesc,
		"lawyers": addLawyers()
	});
}

function addTaskToView(columnId, task) {
	$("#" + columnId).append(
		`<div class="card border-dark mb-3">
		<div class="card-header p-2 d-inline-flex">
			<h5>${ task.task_id } - ${ task.name }</h5>
			<div class="ml-auto">
				<button data-id="${ task.task_id }" type="button" class="btn bg-tranparent p-0">
					<i  class="material-icons">delete</i>
				</button>
			</div>
		</div>
		<div class="card-body p-2" data-toggle="collapse" data-target="#taskInfo${ task.task_id }" aria-expanded="false" aria-controls="taskInfo">
			<div role="button" class="text-center text-muted">
				<span class="material-icons">expand_more</span>
				Expandir descrição
				<span class="material-icons">expand_more</span>
			</div>
			<div class="collapse" id="taskInfo${ task.task_id }">
				<p class="card-text">${ task.desc }</p>
				<h6>Advogados:</h6>
				<table class="table table-bordered table-hover tabela-advogado">
					<thead>
						<tr>
							<th scope="col">OAB</th>
							<th scope="col">Nome</th>
						</tr>
					</thead>
					<tbody>
						${addTableAdvs(task.lawyers)}
					</tbody>
				</table>
			</div>
		</div>
		<div class="card-footer d-flex p-0">
			<a role="button" onclick="changeStatus(this, ${ task.task_id }, 'back')" class="btn btn-secondary d-block w-100 separator-left status-btn-ret">
				<i class="material-icons">
					arrow_back_ios
				</i>
				Retroceder
			</a>
			<a role="button" onclick="changeStatus(this, ${ task.task_id }, 'forward')" class="btn btn-secondary d-block w-100 status-btn-av">
				Avançar
				<i class="material-icons">
					arrow_forward_ios
				</i>
			</a>
		</div>
	</div>`
	);
}

function addTableAdvs(advs) {
	let rows = "";
	advs.forEach(adv=>{
		rows += 
		`<tr>
			<td>${adv.oab}</td>
			<td>${adv.name}</td>
		</tr>`
	});
	return rows;
}


function addLawyers() {
	let oab = document.getElementsByClassName('coluna-num-oab');
	let name = document.getElementsByClassName('coluna-nome-advogado');
	let advs = [];
	for (let i = 0; i < oab.length; i++) {
		advs.push({
			"oab": oab[i].innerText,
			"name": name[i].innerText
		});
	}
	return advs;
}

function resetJqueryFuncs() {
	$("[aria-controls='taskInfo']").on("shown.bs.collapse", (e)=>{collapseLabel($(e.target))});
	$("[aria-controls='taskInfo']").on("hidden.bs.collapse", (e)=>{expandLabel($(e.target))});
	$("button[data-id]").off("click");
	$("button[data-id]").on("click", (e)=>{deleteTask($(e.target))});
}

function collapseLabel(t) {
	t.prev()[0].innerHTML =
		`<span class="material-icons">expand_less</span>
		Encolher descrição
		<span class="material-icons">expand_less</span>`;
}

function expandLabel(t) {
	t.prev()[0].innerHTML =
		`<span class="material-icons">expand_more</span>
		Expandir descrição
		<span class="material-icons">expand_more</span>`
}

function deleteTask(t) {
	if(confirm("Deseja realmente excluir?")){
		$.post("/task/delete/"+t.parent().data("id"))
		.done((data) => {
			if (data.success){
				t.closest(".card").remove();
			}
			else{
				alert("Algum erro aconteceu!");
			}
		});
	}
	resetJqueryFuncs();
}

function changeStatus(t, id, movement) {
	let column = $(t).closest("[data-type]");
	let columnIdx = parseInt(column.data("idx"));
	if (movement == "forward" && columnIdx < 3) {
		let newColumn = $(`[data-idx='${columnIdx+1}']`);
		updateStatus(id, newColumn.data("type"), $(t).closest(".card"), newColumn);
	}
	else if (movement == "back" && columnIdx > 1) {
		let newColumn = $(`[data-idx='${columnIdx-1}']`);
		updateStatus(id, newColumn.data("type"), $(t).closest(".card"), newColumn);
	}
}

function updateStatus(id, status, card, newColumn){
	$.post(`/task/status/${id}/${status}`)
		.done((data) => {
			if (data.success){
				newColumn.append(card);
			}
			else{
				console.log(data)
				alert("Algum erro aconteceu!");
			}
		});
}

resetJqueryFuncs();
/*function ajaxTask(taskNome,taskDesc){
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
			console.log(responsedata["msg"]["task_id"]);
			addLawyer(responsedata["msg"]["task_id"]);
		}
	 })
	 
}*/

/*function ajaxLawyer(id, name, oab){
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
}*/


