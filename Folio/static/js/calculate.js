  function calculatePrice(){

      //Get selected data  


	  var width = document.getElementById("width");
	  width = parseInt(width.value);

	  var height = document.getElementById("height");
	  height = parseInt(height.value);
	  
	

      var elt = document.getElementById("style");
      var style = elt.options[elt.selectedIndex].value;

      elt = document.getElementById("materials");
      var materials = elt.options[elt.selectedIndex].value;

      elt = document.getElementById("priority");
      var priority= elt.options[elt.selectedIndex].value;

      //convert data to integers
      style = parseInt(style);
      materials = parseInt(materials);
      priority = parseInt(priority);
    
   

      //calculate total value  
      var total = 500 + ((height + width) /2) *(style + materials + priority);

      //print value to  PicExtPrice 
      document.getElementById("PicExtPrice").value=total;

 }