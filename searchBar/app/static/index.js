$(document).ready(function() {
    //When the search button is clicked 
    console.log("index here")
    $("#SearchButton").click(function() {
        // get value of the selected query from the dropdown
        let selectValue = $('#searchDropdown').val();
        // route to search page/optionselected when search button is clicked
        window.location.href = '/search/'+selectValue;

      
      })
    
});