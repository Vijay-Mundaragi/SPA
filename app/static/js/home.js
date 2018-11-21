$("#read").click(function() {
	result = "<table class='table table-striped'>\
  <thead>\
    <tr>\
      <th scope='col'>USN</th>\
      <th scope='col'>Fname</th>\
      <th scope='col'>Lname</th>\
      <th scope='col'>GPA</th>\
      <th scope='col'>Email</th>\
      <th scope='col'>Phone</th>\
    </tr>"

	$.getJSON('/sample_spa/v1/student', function(data) {
		console.log(data)
		$.each(data, function(key, value)
		{
			result = result + "<tr><td>"+value.usn+"</td>"+"<td>"+value.fname+"</td>"+"<td>"+value.lname+"</td>"+"<td>"+value.gpa+"</td>"+"<td>"+value.email+"</td>"+"<td>"+value.phone+"</td></tr>";
			console.log(result);
		})
		$("#div1").html(result);  
	});  	
});


$("#create_form").submit(function(event){
	event.preventDefault();
	var $items = $('#fname, #lname, #pno, #email, #gpa');
	
	var obj = {};
	
	$items.each(function() {
	    obj[this.id] = $(this).val();
	});

	console.log(obj)

	// $.post("/sample_spa/v1/student", obj, function(data){
	// 	console.log(data);
	// });

	$.ajax({
            type: "POST",
            url: "/sample_spa/v1/student",
            dataType: "json",
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify(obj),
            success: function (data) {
               alert('Success');

            },
            error: function () {
             alert('Error');
            }
        });


	// $.post('/sample_spa/v1/student', function(data) {
	// 	console.log(data); 	
	// });
});