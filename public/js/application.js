$(function(){
  $('input#table_search').quicksearch('table tbody.main tr');
  
  $("#more").hide()  
  $("#page_header a.more_link").click(function(e){  
    $("#more").fadeToggle("slow")
    e.preventDefault();
  })
  
  $("#health_table tr").hide()
  $("#health_table tr:first").show()
  $("#health_table tr.odd, #health_table tr.even").show()
  
  $("#health_table .more_link").click(function(e){
    $(this).parent().parent().nextUntil(".even, .odd").fadeToggle("slow")
    e.preventDefault();
  })
  
})
