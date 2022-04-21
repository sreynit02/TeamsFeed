$(document).ready(function(){
    console.log("here")
    // var searchResults=$('#results').data();
    // console.log(searchResults)
    // let results2 = $("meta[property='results']").attr('content');
    // console.log(results2)
    // google.charts.load('current', {'packages':['corechart']});
    //   google.charts.setOnLoadCallback(drawChart);
      let results2 = $("meta[property='results']").attr('content');
      console.log(typeof(results2)); // its a string :((
      // console.log(results2[3])
      // listLength=results2.length;
      // resultArray=[]
      // for (let i=0;i<listLength;i++){
      //     data=[]
      //     data.push(results2[0][0])
      //     data.push(results2[0][1])
      //     resultArray.push(data)
    
    
    //   console.log(result);
    function drawChart() {
        var data = google.visualization.arrayToDataTable(results2);

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

});