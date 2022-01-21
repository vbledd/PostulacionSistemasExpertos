var emergente = new Vue({
    el: '#appEmergente',
    delimiters: ['${','}'],
    data: {
      
    
      bmenu:'none',
      titulo : '',
      btn : 0,
      

    },
    watch : {
       
    },
    methods: {
 
        menu: function(){


          if (this.bmenu == "none"){
            this.bmenu = ''
          }else{
            this.bmenu = 'none'
          }

         
        },

       

        
    
        
        
    },
    created() {
        
      },
    
  });


