function opsi(data) {
  var allRows = data.split(/\r?n|\r/);
      var table = "<table>";
  for(var singleRow=0;singleRow<allRows.length;singleRow++){
    if(singleRow === 0){
      table += "<thead>";
      table += "<tr>";
    } else{
      table += "<tr>";
    }
    var rowCells = allRows[singleRow].split(',');
    for(var rowSingleCell=0;rowSingleCell<rowCells.length;rowSingleCell++){
      if(singleRow === 0){
        table += "<th>";
        table += rowCells[rowSingleCell];
        table += "</th>";
      } else {
        table += "<td>";
        table += rowCells[rowSingleCell];
        table += "</td>";
      }
    }
    if(singleRow === 0){
      table += "</tr>";
      table += "</thead>";
      table += "<tbody>"
    } else {
      table += "</tr>";
    }
  }
  table += "</tbody>";
  table += "</table>";
  $("body").append(table);
}
$.ajax({
  url: "data.csv",
  dataType: "text",
}).done(opsi);