const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
$(".btn-delete-record").click(function() {
	let url = $(this).data("url");
	Swal.fire({
		title: "Delete this data?",
		icon: "warning",
		confirmButtonText: "Remove",
		cancelButtonText: "Cancel",
		showCancelButton: true
	}).then(result => {
		if (result.value) {
			$('.loading-div').removeClass('hidden');
			const request = new Request(
			    url,
			    {
			        method: 'POST',
			        headers: {'X-CSRFToken': csrftoken},
			        mode: 'same-origin' // Do not send CSRF token to another domain.
			    }
			);
			fetch(request).then(response => response.json())
		    .then(data => {
		        $('.loading-div').addClass('hidden');
				Swal.fire({
						title: data.message,
						icon: "success",
						confirmButtonText: "OK"
					})
					.then(function() {
						window.location.reload();
					});
		    })
		    .catch(error => console.error(error));
		}
	});
});