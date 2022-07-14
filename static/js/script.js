function sendMail(contactForm) {
    emailjs.send("service_f794snj", "template_o5n61zc", {
            "form_name": contactForm.name.value,
            "message": contactForm.message.value,
            "form_email": contactForm.emailaddress.value,
            "form_phone": contactForm.phone.value
        }, "Hd3kDcWXoTUyVhO8I")
        .then(
            function (response) {
                console.log("Yay", response);
            }
        ),
        function (error) {
            console.log("Error", error)
        };

    
}