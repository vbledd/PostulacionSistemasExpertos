var bodegas = new Vue({
    el: '#appBodegas',
    delimiters: ['${','}'],
    data: {
      
      
      listadoBodegas : [],

     
     
 

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

      entrar: function(id){

        ir('/bodegas/productos?id='+id)
      }

      

    },

    created() {
        
      this.listar();
     
      },
    
  });


