
    	var select = false
    	var m = document.getElementById("meaning_0");
    	m.addEventListener("click", function(){
    		if(select) {
 				m.style.borderColor = "green";
 				m.style.borderRadius = "30px";
    			
    		}
    		else
    			{
    				m.style.borderColor = null;
    				m.style.borderRadius = null;
    			};
			
			select = !select
			});
    	var selectw = false
    	var w = document.getElementById("word_durino");
    	w.addEventListener("click", function(){
    		if(selectw) {
 				w.style.borderColor = "green";
 				w.style.borderRadius = "30px";
    			
    		}
    		else
    			{
    				w.style.borderColor = null;
    				w.style.borderRadius = null;
    			};
			
			selectw = !selectw
			});



<form id="myForm" action="action.php" method="post">
  <input type='hidden' id= 'hiddenField' name='id' value='' />

<script> 
  function mySubmit() {
     document.getElementById('hiddenField').value = "Whatever I want here";
     document.getElementById("myForm").submit();
   }
</script>