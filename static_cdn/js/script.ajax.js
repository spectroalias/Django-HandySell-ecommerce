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
					buttonType.html("<button type='submit' class='btn btn-primary glyphicon glyphicon-shopping-cart'> Remove from cart</button>")
				}else {
					buttonType.html("<button type='submit' class='btn btn-primary glyphicon glyphicon-shopping-cart'> Add to cart</button>")
				}
				$("#cartIcon").text(data.cart_count)
				$(".subTotal").text(data.cart_total)
				$(".Total").text(data.total_amount)
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
	// auto search implementation.
	var searchForm = $("#form-search")
	var searchQuery = searchForm.find("[name='q']")
	var typeInterval = 1000
	var typeTimer;
	searchForm.keyup(function(event){
		clearTimeout(typeTimer)
		typeTimer = setTimeout(performSearch,typeInterval)
	})
	function performSearch(){
		visualSearching()
		var q = searchQuery.val()
		setTimeout(function(){
			window.location.href='/search/?q='+q
		},1500)
	}
	function visualSearching(event){
		var searchButton = searchForm.find('.button-search-form')
		searchButton.addClass("disabled")
		searchButton.html("<i class='fas fa-stroopwafel fa-spin'></i>")
	} 

	$(".delete-product").on('submit', function() {
		if(confirm("Really ? , you want to Delete this?")) return true;
		else return false;
	});
});