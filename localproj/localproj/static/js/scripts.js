
//Search bar index page
var search_btn = document.querySelector(".search_btn");
var close_btn = document.querySelector(".close_btn");
var search_box_wrap = document.querySelector(".search_box_wrap");
var input_search = document.querySelector(".input_search");

search_btn.addEventListener("click", function(){
	search_box_wrap.classList.add("active");
	input_search.focus();
});

close_btn.addEventListener("click", function(){
	search_box_wrap.classList.remove("active");
});

// contact us page
function sendEmail(){
    Email.send({
            Host : "smtp.gmail.com",
            Username : "dangjunhan@gmail.com",
            Password : "password",
            To : 'dangjunhan@gmail.com',
            From : document.getElementById("email").value,
            Subject : "New contact form Enquiry",
            Body : "And this is the body"
        }).then(
          message => alert(message)
        );
    }

