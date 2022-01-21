var productos = new Vue({
    el: '#appProductos',
    delimiters: ['${','}'],
    data: {
      
      
      listadoProductos : [],

      id : '',
      codigo :'',
      nombre: '',
      detalle : '',
      valor: '',
 

    },
    watch : {
       
    },
    methods: {
 
      productos: function(){

        ruta='/api/productos/listar';
        axios
        .get(ruta)
        .then(response => {                       
           
            if(response.status == 200){
          
              this.listadoProductos = JSON.parse(response.data)
        
            }


        })
        .catch(error => {
           // para el manejo de errores
           console.log(error);
        });


      },

      eliminarProducto: function(){

        ruta = '/api/productos/eliminar';
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
            this.productos();
            alert("Se elimino correctamente el producto "+this.nombre);
           }

        })

        .catch(error => {
           // para el manejo de errores
           console.log(error);
         
        });
        
    },

    nuevoProducto: function(){

      ruta = '/api/productos/crear';
      token = document.getElementById('csrf').value;

      datosPOST = new URLSearchParams()

      datosPOST.append('codigo',this.codigo);
      datosPOST.append('nombre',this.nombre);
      datosPOST.append('detalle',this.detalle);
      datosPOST.append('valor',this.valor);
    
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
          this.productos();
          alert("Fue creado correctamente el producto "+this.nombre);
         }
         

      })

      .catch(error => {
         // para el manejo de errores
         console.log(error);
         
          alert("El codigo del producto ya se encuentra en uso")
        
       
      });
      
  },

  editarProducto: function(){

    ruta = '/api/productos/editar';
    token = document.getElementById('csrf').value;

    datosPOST = new URLSearchParams()

    datosPOST.append('id',this.id);
    datosPOST.append('codigo',this.codigo);
    datosPOST.append('nombre',this.nombre);
    datosPOST.append('detalle',this.detalle);
    datosPOST.append('valor',this.valor);
  
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
        this.productos();
        alert("Fue editado correctamente el producto "+this.nombre);
       }
       

    })

    .catch(error => {
       // para el manejo de errores
       console.log(error);
       
        alert("El codigo del producto ya se encuentra en uso")
      
     
    });
    
},

      datos: function(id){

        ruta='/api/productos/datos?id='+id;
        axios
        .get(ruta)
        .then(response => {                       
           
            if(response.status == 200){
          
              datos = JSON.parse(response.data)
              

              this.id = datos[0].pk
              this.codigo = datos[0].fields.codigo
              this.nombre = datos[0].fields.nombre
              this.detalle = datos[0].fields.detalle
              this.valor = datos[0].fields.valor
        
            }


        })
        .catch(error => {
           // para el manejo de errores
           console.log(error);
        });


      },

      limpiarCampos: function(){

        this.id = ''
        this.codigo = ''
        this.nombre = ''
        this.detalle = ''
        this.valor = ''
      },
   
      ventanaNuevo: function(){
        
        emergente.titulo = "Nuevo Producto";
        emergente.btn = 0;
        this.limpiarCampos()
        emergente.menu();
      },

      ventanaEditar: function(id){
        this.datos(id)
        emergente.titulo = "Editar Producto";
        emergente.btn = 1;
        emergente.menu();
      },

    },

    created() {
        
      this.productos();
     
      },
    
  });


