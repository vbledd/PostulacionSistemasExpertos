var productos = new Vue({
    el: '#appProductos',
    delimiters: ['${','}'],
    data: {
      
      
      listadoProductos : [],
      productosBuscados: [],
      buscar : '',
      bodegaId: 0,
      seleccionado: 'No existe producto seleccionado',
      idSeleccionado: 0,
      stock: 0,
      stockActual: 0,
      stockFinal :0,
 

    },
    watch : {
       
    },
    methods: {
 
      listar: function(){
       
       ruta='/api/bodegas/productos?idBodega='+this.bodegaId;
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

      ventanaNuevo: function(){
        
        emergente.titulo = "Seleccionar Producto";
        emergente.btn = 0;
        this.buscador();
        emergente.menu();
      },

      buscador: function(){
       
        ruta='/api/productos/buscador?buscar='+this.buscar;
         axios
         .get(ruta)
         .then(response => {                       
            
             if(response.status == 200){
           
               this.productosBuscados = JSON.parse(response.data)
               
             }
 
 
         })
         .catch(error => {
            // para el manejo de errores
            console.log(error);
         });
 
 
       },

       producto: function(idProd){
       
        ruta='/api/bodegas/productos/especifico?idBodega='+this.bodegaId+'&idProducto='+idProd;
        
         axios
         .get(ruta)
         .then(response => {                       
            
             if(response.status == 200){
              data = JSON.parse(response.data)
              this.stockActual = data[0].fields.stock
              this.stockFinal = this.stockActual
             
               
             }
 
 
         })
         .catch(error => {
            // para el manejo de errores
            //console.log(error);
         });
 
 
       },


       seleccionar: function(id,nombre){
        this.seleccionado = "Seleccionado: "+nombre;
        this.idSeleccionado = id;
        this.producto(id);
       },

       seleccionar2: function(id,nombre){
        this.ventanaNuevo()
        this.seleccionado = "Seleccionado: "+nombre;
        this.idSeleccionado = id;
        this.producto(id);
       },

       limpiarDatos:function(){

        this.seleccionado = "No existe producto seleccionado"
        this.idSeleccionado = 0;
        this.stockActual = 0;
        this.stock = 0;
        this.stockFinal= 0;
       },

       agregarItem : function(){

        ruta = '/api/bodegas/stock/agregar';
        token = document.getElementById('csrf').value;
    
        datosPOST = new URLSearchParams()
    
        datosPOST.append('idBodega',this.bodegaId);
        datosPOST.append('idProducto',this.idSeleccionado);
        datosPOST.append('stock',this.stockFinal);
        
        
      
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
            this.listar();
            emergente.menu();
            this.limpiarDatos()
            
            alert("se agrego correctamente al stock");
            }
            
    
        })
    
        .catch(error => {
            // para el manejo de errores
            console.log(error);
            
            alert("Error de consulta")
          
          
        });
        
        
       },

       calcularStock : function(){
        this.stockFinal = Number(this.stockActual) + Number(this.stock); 
       }


    },

    created() {
      
      this.bodegaId= document.getElementById('idBodega').value;
      this.listar();
     
      },
    
  });


