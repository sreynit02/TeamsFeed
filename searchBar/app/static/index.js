$(document).ready(function() {
    //When the search button is clicked 
    $("#SearchButton").click(function() {
        // get text of the selected query from the dropdown
        let selectText = $('#searchDropdown :selected').text();
        // route to search page when search button is clicked
        window.location.href = '/search';
        console.log(selectText);
       
      })
});