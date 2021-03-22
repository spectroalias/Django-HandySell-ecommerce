 $(document).ready(function(){

//  this handles the asynchronous communicaion of cart update.
 	var cartForm = $(".form-cart-update")
 	cartForm.submit(function(event){
 		event.preventDefault()
 		var thisForm = $(this)
 		var actionURL = thisForm.attr("action")
 		var formMethod = thisForm.attr("method")
 		var formData = thisForm.serialize()
 		// JSON format
 		$.ajax({
			url: actionURL,
			method: formMethod,
			data: formData,
			success: function(data){
				var buttonType = thisForm.find(".cartUpdate")
				if (data.added){
					buttonType.html("<button type='submit' class='btn btn-primary glyphicon glyphicon-cart'>Remove from cart</button>")
				}else {
					buttonType.html("<button type='submit' class='btn btn-primary glyphicon glyphicon-cart'>Add to cart</button>")
				}
				$("#cartIcon").text(data.cart_count)
			},
			error: function(errorData){
				$.confirm({
					title: 'Something went wrong',
					content: errorData,
					draggable: true,
				});
			},		
 		})
 	})

});