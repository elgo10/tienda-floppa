//verificar datos aquí, SOLO VERIFICAR TIPOS DE DATOS
/**
 *  insertar <script src="https://code.jquery.com/jquery-3.7.0.min.js"></script> en html
 * ANTES DE LINKEAR EL ARCHIVO
 */
$(function () {
  let numero = '1234567890';
  let letras = ' qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNMáéíóúÁÉÍÓÚ';

  // Validar
  $('.txtRut').keypress(function(e)
  {
    let caracter = String.fromCharCode(e.which);
    if(numero.indexOf(caracter) < 0)
        return false;
  })

  $('.txtDv').keypress(function(e)
    {
        let patron = numero + 'kK';
        let caracter = String.fromCharCode(e.which);
        if(patron.indexOf(caracter) < 0)
            return false;
    })
  $('.txtNombre').keypress(function(e)
  {
    let caracter = String.fromCharCode(e.which);
    if (letras.indexOf(caracter) < 0)
      return false;
  })
  $('.txtApellido').keypress(function(e)
  {
    let caracter = String.fromCharCode(e.which);
    if (letras.indexOf(caracter) < 0)
      return false;
  })
  $('.txtDescripcion').keypress(function(e)
  {
    let patron = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM ';
    let caracter = String.fromCharCode(e.which);
    if (patron.indexOf(caracter) < 0)
      return false;
  })
  $('.txtStock').keypress(function(e)
  {
    let patron = numero;
    let caracter = String.fromCharCode(e.which);
    if (patron.indexOf(caracter) < 0)
      return false;
  })
  $('.txtPrecio').keypress(function (e) 
  {
    let patron = numero;
    let caracter = String.fromCharCode(e.which);
    if (patron.indexOf(caracter) < 0)
      return false;
  })

  $('.txtVenc').keypress(function(e)
    {
        let patron = numero + '/';
        let caracter = String.fromCharCode(e.which);
        if(patron.indexOf(caracter) < 0)
            return false;
    })
    


  $('.txtEmail').keypress(function(e)
    {
        let patron = numero + 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM@_-.';
        let caracter = String.fromCharCode(e.which);
        if(patron.indexOf(caracter) < 0)
            return false;
    }) 

  // ejercicio: validar el rut.
  $('.btnAceptar').click(function(){


    if (!$.trim($('.txtNombre').val())) {
      alert("Falta el nombre");
      $('.txtNombre').focus();
    }
    else if (!$('.txtdescripcion').val()) {
      alert("Falta La Descripcion");
      $('.txtDescripcion').focus();
    }
    else if (!$('.txtStock').val()) {
      alert("Falta Stock");
      $('.txtDescripcion').focus();
    }
    else if (!$('.txtPrecio').val()) {
      alert("Falta El precio");
      $('.txtDescripcion').focus();
    }
  })
  $('.btnLimpiar').click(function(){
    $('.txtNombre, .txtDescripcion, .txtstock, .txtprecio').val('');
    /*$('.txtRut').val('');
    $('.txtDv').val('');
    $('.txtNombre').val('');
    $('.txtEmail').val('');*/
    $('.txtRut').focus()
  })

  //Validar inicio sesion
  $('#btnSesion').click(function(){
    let email = ''
    let pass = ''
    email = $('.txtEmail').val()
    pass = $('.txtPass').val()
    if (email.length < 1) {
      alert('el Email está vacío')
      return false
    } else if (pass.length < 1) {
      alert('la contraseña está vacía')
      return false
    }
    alert('validado')
    alert('correo: ' + $('.txtEmail').val() + '\n' + 'contraseña: ' + $('.txtPass').val())
  })

  //Registrarse
  $('#btnnSesion').click(function(){

    if(!$('.txtRut').val())
    {
      alert('Ingrese un rut')
      $('.txtRut').focus()
      return false
    } 
    if(!$('.txtDv').val())
    {
      alert('Ingrese un Dígito verificador')
      $('.txtDv').focus()
      return false
    } else if (!$('.txtNombre').val()){
      alert('Ingrese un Nombre')
      $('.txtNombre').focus()
      return false
    } else if (!$('.txtApellido').val()){
      alert('Ingrese un Apellido')
      $('.txtApellido').focus()
      return false
    } else if (!$('.txtEmail').val()){
      alert('Ingrese un correo electrónico')
      $('.txtEmail').focus()
      return false
    } else if (!$('.txtPass').val()){
      alert('Ingrese una contraseña')
      $('.txtPass').focus()
      return false
    }

    alert('validado')
    alert('Rut: ' + $('.txtRut').val() + ' - ' + $('.txtDv').val() + '\n' + 'Nombre: ' + $('.txtNombre').val() +
    'Apellido: ' + $('.txtApellido').val() + '\n' + 'correo: ' + $('.txtEmail').val() + '\n' + 'contraseña: ' + $('.txtPass').val())
  })

  $('#btnSubmit').click(function(){
    if (!$.trim($('.txtNombre').val())) {
      alert("Falta el nombre");
      $('.txtNombre').focus();
      return false
    } else if (!$('.txtDescripcion').val()) {
      alert("Falta La Descripcion");
      $('.txtDescripcion').focus();
      return false
    } else if (!$('.txtStock').val()){
      alert('Ingrese el stock')
      $('.txtStock').focus()
      return false
    } else if (!$('.txtPrecio').val()){
      alert('Ingrese el precio del producto')
      $('.txtPrecio').focus()
      return false
    } 
    alert('Validado')
    alert('Nombre: ' + $('.txtNombre').val() + '\n ' + 'Descripcion: ' + $('.txtDescripcion').val() +
    '\n ' + 'Stock: ' + $('.txtStock').val() + '\n ' + 'Precio' + $('.txtPrecio').val())
    return false
  })

  function esValidoElRut(Rut, Digito) {
    Digito = Digito.toUpperCase();
    var longitud = Rut.length;
    var factor = 2;
    var sumaProducto = 0;
    var con = 0;
    var caracter = 0;

    for (con = longitud - 1; con >= 0; con--) {
      caracter = Rut.charAt(con);
      sumaProducto += (factor * caracter);
      if (++factor > 7)
        factor = 2;
    }

    var digitoAuxiliar = 11 - (sumaProducto % 11);
    var caracteres = "123456789K0";
    var digitoCaracter = caracteres.charAt(digitoAuxiliar);
    return digitoCaracter == Digito ? 1 : 0;
  }
})
