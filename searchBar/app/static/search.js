$(document).ready(function(){
    console.log("here")
    // var searchResults=$('#results').data();
    // console.log(searchResults)
    // let results2 = $("meta[property='results']").attr('content');
 
    // google.charts.load('current', {'packages':['corechart']});
    //   google.charts.setOnLoadCallback(drawChart);
      let results2 = $("meta[property='results']").attr('content');
      // console.log(Array.from(results2))
      console.log(results2)
      resultsForGraph=results2.replaceAll("(","[").replaceAll(")","]")
      console.log(resultsForGraph.length===results2.length)
      // console.log(results2.replace(")","]"))
      // console.log(typeof(results2)); // its a string :((
      // console.log(results2[3])
      // listLength=results2.length;
      // resultArray=[]
      // for (let i=0;i<listLength;i++){
      //     data=[]
      //     while (results2[i]!="("){
      //       i=i+1
      //     }
      //     if (results2[i]==="("){
      //       county=
      //     }

      //     data.push(results2[0][0])
      //     data.push(results2[0][1])
      //     resultArray.push(data)
      google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);
    
    //   console.log(result);
    function drawChart(results=resultsForGraph) {
        console.log("in api function")
        var data = google.visualization.DataTable();
        data.addColumn("County","Farmers from County")
        data.addRows(results)
        console.log(data)
        // var data = google.visualization.arrayToDataTable([
        //   ['Task', 'Hours per Day'],
        //   [,11],
        //   ['Eat',      2],
        //   ['Commute',  2],
        //   ['Watch TV', 2],
        //   ['Sleep',    7]
        // ]);

        var options = {
          title: 'My Daily Activities'
        };
  
        var chart = new google.visualization.PieChart(document.getElementById('piechart'));
        chart.draw(data, options);
      }
      drawChart()

});