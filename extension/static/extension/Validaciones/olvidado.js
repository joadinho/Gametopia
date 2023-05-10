$(document).ready(function(){
    $("#formOlvidado").submit(function(e){
        e.preventDefault();

        var email_ol = $("#emailO").val();

        let msjMostrarOlvidado = "";
        let enviar = false;

        //valida email
        if((email_ol).trim().indexOf('@', 0) == -1 || (email_ol).trim().indexOf('.', 0) == -1) {
            msjMostrarOlvidado += "-El correo electrónico introducido es inválido. Debe contener un @";
            enviar = true;
        }  
        if(email_ol.trim() == ""){
            msjMostrarOlvidado += "<br>-El campo correo no puede estar vacío";
            enviar = true;
        }
        var emailRegex = /^[^\s@]+@[^\s@]+.[^\s@]+$/; 

        if (!emailRegex.test(email_ol)) {
            msjMostrarOlvidado += "<br>-No debe comenzar con @";
            enviar = true;
        }


        if(enviar){
            $("#mensaje_Olvidado").html(msjMostrarOlvidado);
        }
        else{
            $("#mensaje_Olvidado").html("-En unos minutos le llegará el codigo.");
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