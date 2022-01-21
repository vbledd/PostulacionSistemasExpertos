var resumen = new Vue({
    el: '#appresumen',
    delimiters: ['${','}'],
    data: {
      
      cantidadProductos : 0,
      listadoProductos : [],
      stockBodegas : 0,
      listadoBodegas : []
      

    },
    watch : {
       
    },
    methods: {
 
      productos: function(){

        ruta='/api/productos/resumen';
        axios
        .get(ruta)
        .then(response => {                       
           
            if(response.status == 200){
          
              this.cantidadProductos = response.data['cantidad'];
              this.listadoProductos = JSON.parse(response.data['datos'])
            
              
            }


        })
        .catch(error => {
           // para el manejo de errores
           console.log(error);
        });


    },
    bodega: function(){

      ruta='/api/bodegas/resumen';
      axios
      .get(ruta)
      .then(response => {                       
         
          if(response.status == 200){
        
            this.stockBodegas = response.data[0]['total'];
            this.listadoBodegas = response.data[0]['datos']

            console.log(this.stockBodegas)
            console.log(this.listadoBodegas)
            
            
          }


      })
      .catch(error => {
         // para el manejo de errores
         console.log(error);
      });


  },

        
    
        
        
    },
    created() {
        
      this.productos();
      this.bodega();
      },
    
  });


