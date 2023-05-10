$(document).ready(function(){
    $("#formModificar").submit(function(e){
        e.preventDefault();

        var nombre_modi    = $("#nombreM").val();
        var clave_modi     = $("#passwordM").val();
        var con_clave_modi = $("#con_passwordM").val();
        var email_modi     = $("#emailM").val();

        let msjMostrarModi = "";
        let enviar = false;


        //validar nombre
        if(nombre_modi.trim().length < 4 || nombre_modi.trim().length > 10){
            msjMostrarModi = msjMostrarModi + "-El nombre debe tener entre 4 y 10 caracteres";
            enviar = true;
        }

        var letra = nombre_modi.trim().charAt(0);
        if(!esMayuscula(letra)){
            msjMostrarModi += "<br>-El nombre debe comenzar con mayúscula";
            enviar = true;
        }
    
        
        if(nombre_modi.trim() == ""){
            msjMostrarModi += "<br>-El campo nombre no puede estar vacío";
            enviar = true;
        }

        //validar password
        if(clave_modi.trim().length < 8 || clave_modi.trim().length > 12){
            msjMostrarModi = msjMostrarModi + "<br>-Clave inválida debe tener entre 8 y 12 caracteres";
            enviar = true;
        }

        if(clave_modi.trim()  == ""){
            msjMostrarModi += "<br>-Clave inválida no puede estar vacío";
            enviar = true;
        }

        if (!clave_modi.match(/([A-Z])/)){
           msjMostrarModi += "<br>-Clave inválida Falta una letra mayúscula";
            enviar = true;
        }

        if (!clave_modi.match(/([a-z])/)){
            msjMostrarModi += "<br>-Clave inválida Falta una letra minúscula";
             enviar = true;
         }

         if (!clave_modi.match(/([0-9])/)){
            msjMostrarModi += "<br>-Clave inválida Debe contener al menos un numero";
            enviar = true;
         }

        if (!clave_modi.match(/([!,%,&,@,#,$,^,,?,_,~,.])/)){
            msjMostrarModi += "<br>-Clave inválida Debe contener un caracter especial  !,%,&,@,#,$,^,,?,_,~,.";
            enviar = true;
        }

        //valida la clave confirmada

        if (con_clave_modi.trim() != clave_modi.trim()){
            msjMostrarModi += "<br>-La clave confirmada no es la misma";
            enviar = true;
        }

        //valida correo

        if((email_modi).trim().indexOf('@', 0) == -1 || (email_modi).trim().indexOf('.', 0) == -1) {
            msjMostrarModi += "<br>-El correo electrónico introducido es inválido. Debe contener un @";
            enviar = true;
        }
        var emailRegex = /^[^\s@]+@[^\s@]+.[^\s@]+$/; 

        if (!emailRegex.test(email_modi)) {
            msjMostrarModi += "<br>-No debe comenzar con @";
            enviar = true;
        }

        if(email_modi.trim() == ""){
            msjMostrarModi += "<br>-El campo correo no puede estar vacío";
            enviar = true;
        }




















        if(enviar){
            $("#mensaje_modificar").html(msjMostrarModi);
        }
        else{
            $("#mensaje_modificar").html("-Perfil Modificado exitosamente.");
        }
    });

    function esMayuscula(letra){
        console.log("Estoy aqui");
        console.log(letra);
        console.log(letra.toUpperCase());

        if(letra == letra.toUpperCase()){
            return true;
        }
        else{
            return false;
        }
    }
});