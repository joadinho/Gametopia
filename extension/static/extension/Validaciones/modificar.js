$(document).ready(function(){
    $("#formModificar").submit(function(e){
        

        var clave_modi     = $("#passwordM").val();
        var con_clave_modi = $("#con_passwordM").val();
        var clave_modiP     = $("#claveN").val();
        var con_clave_modiP = $("#claveCN").val();
        

        let msjMostrarModi = "";
        let enviar = false;

        //validar password

        if(clave_modi.trim().length < 8 || clave_modi.trim().length > 12){
            msjMostrarModi = msjMostrarModi + "<br>-Clave inválida debe tener entre 8 y 12 caracteres";
            enviar = true;
            e.preventDefault();
        }

        if(clave_modi.trim()  == ""){
            msjMostrarModi += "<br>-Clave inválida no puede estar vacío";
            enviar = true;
            e.preventDefault();
        }

        if (!clave_modi.match(/([A-Z])/)){
           msjMostrarModi += "<br>-Clave inválida Falta una letra mayúscula";
            enviar = true;
            e.preventDefault();
        }

        if (!clave_modi.match(/([a-z])/)){
            msjMostrarModi += "<br>-Clave inválida Falta una letra minúscula";
             enviar = true;
             e.preventDefault();
         }

         if (!clave_modi.match(/([0-9])/)){
            msjMostrarModi += "<br>-Clave inválida Debe contener al menos un numero";
            enviar = true;
            e.preventDefault();
         }

        if (!clave_modi.match(/([!,%,&,@,#,$,^,,?,_,~,.])/)){
            msjMostrarModi += "<br>-Clave inválida Debe contener un caracter especial  !,%,&,@,#,$,^,,?,_,~,.";
            enviar = true;
            e.preventDefault();
        }

        //validar passwordP

        if(clave_modiP.trim().length < 8 || clave_modiP.trim().length > 12){
            msjMostrarModi = msjMostrarModi + "<br>-Clave inválida debe tener entre 8 y 12 caracteres";
            enviar = true;
            e.preventDefault();
        }

        if(clave_modiP.trim()  == ""){
            msjMostrarModi += "<br>-Clave inválida no puede estar vacío";
            enviar = true;
            e.preventDefault();
        }

        if (!clave_modiP.match(/([A-Z])/)){
           msjMostrarModi += "<br>-Clave inválida Falta una letra mayúscula";
            enviar = true;
            e.preventDefault();
        }

        if (!clave_modiP.match(/([a-z])/)){
            msjMostrarModi += "<br>-Clave inválida Falta una letra minúscula";
             enviar = true;
             e.preventDefault();
         }

         if (!clave_modiP.match(/([0-9])/)){
            msjMostrarModi += "<br>-Clave inválida Debe contener al menos un numero";
            enviar = true;
            e.preventDefault();
         }

        if (!clave_modiP.match(/([!,%,&,@,#,$,^,,?,_,~,.])/)){
            msjMostrarModi += "<br>-Clave inválida Debe contener un caracter especial  !,%,&,@,#,$,^,,?,_,~,.";
            enviar = true;
            e.preventDefault();
        }

        //valida la clave confirmada

        if (con_clave_modi.trim() != clave_modi.trim()){
            msjMostrarModi += "<br>-La clave confirmada no es la misma";
            enviar = true;
            e.preventDefault();
        }

        //valida la clave confirmadaP
        if (con_clave_modiP.trim() != con_clave_modiP.trim()){
            msjMostrarModi += "<br>-La clave confirmada no es la misma";
            enviar = true;
            e.preventDefault();
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