function addRow(tableID) {
  var table = document.getElementById(tableID);
  var rowCount = table.rows.length;
  var row = table.insertRow(rowCount);
  var colCount = table.rows[0].cells.length;

  for(var i=0; i<colCount; i++) {
    var newRow = row.insertCell(i);

    newRow.innerHTML = table.rows[0].cells[i].innerHTML;
    newRow.childNodes[0].value = "";
  }
}

function deleteRow(row) {
  var table = document.getElementById("data");
  var rowCount = table.rows.length;
  if (rowCount > 1) {
    var rowIndex = row.parentNode.parentNode.rowIndex;
    document.getElementById("data").deleteRow(rowIndex);
  }
  else {
    alert("Please specify at least one value.");
  }
}
