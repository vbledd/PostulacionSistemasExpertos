var bodegas = new Vue({
    el: '#appBodegas',
    delimiters: ['${','}'],
    data: {
      
      
      listadoBodegas : [],

      id : '',
      nombre: '',
      direccion : '',
     
 

    },
    watch : {
       
    },
    methods: {
 
      listar: function(){

        ruta='/api/bodegas/listar';
        axios
        .get(ruta)
        .then(response => {                       
           
            if(response.status == 200){
          
              this.listadoBodegas = JSON.parse(response.data)
        
            }


        })
        .catch(error => {
           // para el manejo de errores
           console.log(error);
        });


      },

      eliminar: function(){

        ruta = '/api/bodegas/eliminar';
        token = document.getElementById('csrf').value;

        datosPOST = new URLSearchParams()

        datosPOST.append('id',this.id);
      
        header={
            headers:{
                'X-CSRFToken': token,
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        };

        axios
        .post(ruta, datosPOST, header)
        .then(response => {
            
           if(response.status === 200){
            emergente.menu();
            this.listar();
            alert("Se elimino correctamente la bodega "+this.nombre);
           }

        })

        .catch(error => {
           // para el manejo de errores
           console.log(error);
         
        });
        
    },

    nuevo: function(){

      ruta = '/api/bodegas/crear';
      token = document.getElementById('csrf').value;

      datosPOST = new URLSearchParams()

      datosPOST.append('nombre',this.nombre);
      datosPOST.append('direccion',this.direccion);
 
    
      header={
          headers:{
              'X-CSRFToken': token,
              'Content-Type': 'application/x-www-form-urlencoded'
          }
      };

      axios
      .post(ruta, datosPOST, header)
      .then(response => {
          
         if(response.status === 201){
          emergente.menu();
          this.listar();
          alert("Fue creado correctamente la bodega "+this.nombre);
         }
         

      })

      .catch(error => {
         // para el manejo de errores
         console.log(error);
         
          alert("El nombre de la bodega se encuentra en uso")
        
       
      });
      
  },

  editar: function(){

    ruta = '/api/bodegas/editar';
    token = document.getElementById('csrf').value;

    datosPOST = new URLSearchParams()

    datosPOST.append('id',this.id);
    datosPOST.append('nombre',this.nombre);
    datosPOST.append('direccion',this.direccion);
    
  
    header={
        headers:{
            'X-CSRFToken': token,
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    };

    axios
    .post(ruta, datosPOST, header)
    .then(response => {
        
       if(response.status === 200){
        emergente.menu();
        this.listar();
        alert("Fue editada correctamente la bodega "+this.nombre);
       }
       

    })

    .catch(error => {
       // para el manejo de errores
       console.log(error);
       
        alert("El nombre de la bodega se encuentra en uso")
      
     
    });
    
},

      datos: function(id){

        ruta='/api/bodegas/datos?id='+id;
        axios
        .get(ruta)
        .then(response => {                       
           
            if(response.status == 200){
          
              datos = JSON.parse(response.data)
              

              this.id = datos[0].pk
              this.nombre = datos[0].fields.nombre
              this.direccion = datos[0].fields.direccion
             
        
            }


        })
        .catch(error => {
           // para el manejo de errores
           console.log(error);
        });


      },

      limpiarCampos: function(){

        this.id = ''
        this.nombre = ''
        this.direccion = ''
        
      },
   
      ventanaNuevo: function(){
        
        emergente.titulo = "Nueva Bodega";
        emergente.btn = 0;
        this.limpiarCampos()
        emergente.menu();
      },

      ventanaEditar: function(id){
        this.datos(id)
        emergente.titulo = "Editar Bodega";
        emergente.btn = 1;
        emergente.menu();
      },

    },

    created() {
        
      this.listar();
     
      },
    
  });


