$(function(){
  $(".clpBtn").prop('disabled', true)
  var strnt = $("#crdPrice").text()
  
  $(".dolarBtn").click( function(){
    $(".dolarBtn").prop('disabled', true)
    $.getJSON('https://mindicador.cl/api', function(data) {
      var dolarInd = data;
      var precio1 = parseInt(strnt)
      var precio2 = parseFloat(dolarInd.dolar.valor)
      var res = precio1 / precio2
      let fl = res.toFixed(2)
      var dolar = parseFloat(fl)
      $("#crdPrice").text(dolar)

      $(".clpBtn").prop('disabled', false)
      
    }).fail(function() {
      console.log('Error al consumir la API!');
    });
  })

  $('.clpBtn').click(function(){
    $(".clpBtn").prop('disabled', true)
    $('#crdPrice').text(strnt)
    $(".dolarBtn").prop('disabled', false)
  })

})