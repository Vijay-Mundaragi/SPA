function update_fn(data){
  get_html(data, "/update");
}


function delete_fn(data){
  console.log(data);
  get_html(data, "/delete");
}


function get_html(data, url_info){
  console.log(data);
  var obj = {};
  obj["id"] = data;
  $.ajax({
        type: "POST",
        url: url_info,
        dataType: "text html",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(obj),
        success: function (data) {
               $("html").html(data);
            },
            error: function () {
             console.log("Error Occured");
            }
    });
}


function read_students(){
    $.getJSON('/sample_spa/v1/student', function(data) {
    obj = data
    // console.log(obj)
    $.ajax({
        type: "POST",
        url: "/student_list",
        dataType: "text html",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(obj),
        success: function (data) {
               // console.log(data);
               $("#div1").html(data);
            },
            error: function () {
             console.log("Error Occured");
             alert("Error Occurred")
            }
    });
    });

}


$("#read").click(function() {
	read_students();
});


$("#create").click(function() {
  $.ajax({
      type: "GET",
            url: "/",
            success: function (data) {
               $("html").html(data);
             }
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
  $.ajax({
            type: "POST",
            url: "/sample_spa/v1/student",
            dataType: "json",
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify(obj),
            success: function (data) {
               console.log(data);
               // alert("Successfully Created Student record");
               read_students();
            },
            error: function () {
             console.log("Error Occured");
             alert("Error Occured");
            
            }
        });
});


$("#update_form").submit(function(event){
	event.preventDefault();
	var $items = $('#usn, #fname, #lname, #pno, #email, #gpa');
	var obj = {};
	$items.each(function() {
	    obj[this.id] = $(this).val();
        console.log($(this).val());
	});
	console.log(obj)
	$.ajax({
            type: "PUT",
            url: "/sample_spa/v1/student/"+$("#usn").val(),
            dataType: "json",
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify(obj),
            success: function (data) {
               // alert('Success');
               read_students();
            },
            error: function () {
             alert('Error');
            }
        });
});


$("#delete_form").submit(function(event){
	event.preventDefault();
	var $items = $('#usn');
	var obj = {};
	$items.each(function() {
	    obj[this.id] = $(this).val();
	});
	console.log(obj)
	$.ajax({
            type: "DELETE",
            url: "/sample_spa/v1/student/"+$("#usn").val(),
            dataType: "json",
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify(obj),
            success: function (data) {
               // alert('Success');
               read_students();
            },
            error: function () {
             alert('Error');
            }
        });
});