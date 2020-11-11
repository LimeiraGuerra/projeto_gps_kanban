function capturar()
{
    var nome = document.getElementById('name-advogado').value;
    var oab = documet.getElementById('oab').value;
    var table = document.getElementeByTagName('table')[0];

    var newRow = table.insertRow(1);
    document.getElementById('valor').innerHTML = nome; 
    var cell1 = newRow.insertCell(0);
    var cell2 = newRow.insertCell(1);

    cell1.innerHTML = oab;
    cell2.innerHTML = nome;

}
