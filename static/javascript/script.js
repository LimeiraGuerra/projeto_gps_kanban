	function capturar()
	{
        if(document.getElementById('name-advogado').value == '' ||  document.getElementById('oab').value == '')
        {
                
           alert("Por favor, digite novamente os dados do advogado!")
        }
        else{
                var name = document.getElementById('name-advogado').value;
                var oab = document.getElementById('oab').value;
        
                var table = document.getElementById('Tabela');

                var newRow = table.insertRow(0);
               
                var cell1 = newRow.insertCell(0);
                var cell2 = newRow.insertCell(1);
                var cell3 = newRow.insertCell(2);
                
                cell1.innerHTML = oab;
                cell2.innerHTML = name;        
                cell3.innerHTML = '<input type="button" class="btn btn-danger" value="X" onclick="deleteRow(this)"/>';
        }
         }
