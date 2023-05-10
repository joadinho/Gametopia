$(document).ready(function(){
    $("#formJuego").submit(function(e){
        e.preventDefault();
        
        var nombreJ      = $("#NombreJ").val();
        var descripcionJ = $("#DescripcionJ").val();
        var plataformaJ  = $("#PlataformaJ").val();
        var trailerJ     = $("#TrailerJ").val();

        let msjMostrarAgregar = "";
        let enviar = false;

        //validar nombre
        if(nombreJ.trim().length < 4 || nombreJ.trim().length > 85){
            msjMostrarAgregar = msjMostrarAgregar + "-El nombre del juego debe tener entre 4 y 85 caracteres";
            enviar = true;
        }

        var letra = nombreJ.trim().charAt(0);
        if(!esMayuscula(letra)){
            msjMostrarAgregar += "<br>-El nombre debe comenzar con mayúscula";
            enviar = true;
        }
    
        
        if(nombreJ.trim() == ""){
            msjMostrarAgregar += "<br>-El campo nombre no puede estar vacío";
            enviar = true;
        }

        //valida la descripcion
        if(descripcionJ.trim().length < 50 || descripcionJ.trim().length > 2500){
            msjMostrarAgregar = msjMostrarAgregar + "<br>-La descripción debe tener entre 50 y 2500 caracteres";
            enviar = true;
        }

        var letra = descripcionJ.trim().charAt(0);
        if(!esMayuscula(letra)){
            msjMostrarAgregar += "<br>-La descripción debe comenzar con mayúscula";
            enviar = true;
        }
    
        
        if(descripcionJ.trim() == ""){
            msjMostrarAgregar += "<br>-El campo descripción no puede estar vacío";
            enviar = true;
        }

        //valida las plataformas



        if (!["xbox series", "playstation 3", "nintendo", "pc","xbox one","playstation 4","playstation 5","xbox 360"].includes(plataformaJ.toLowerCase())) {
            msjMostrarAgregar += "<br>-La plataforma ingresada es inválida";
            enviar = true;
          }

          //valida el trailer
            if (!/^(https?|ftp):[//)?(www.)?[^\s/$.?#].[^\s]*$/i.test(trailerJ)) {
                    msjMostrarAgregar += "<br>-Url inválido debe comenzar con https: ";
                    enviar = true;
                }
            


        

        

        


















        if(enviar){
            $("#mensaje_agregar").html(msjMostrarAgregar);
        }
        else{
            $("#mensaje_agregar").html("-Juego agregado exitosamente.");
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