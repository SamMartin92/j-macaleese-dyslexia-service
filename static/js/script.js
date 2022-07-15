function sendMail(contactForm) {
        emailjs.send("service_f794snj", "template_3as9mrv", {
            form_name: contactForm.name.value,
            form_email: contactForm.emailaddress.value,
            form_phone: contactForm.phone.value,
            message: contactForm.message.value
        })
            .then(
                function (response) {
                    console.log("Yay", response);
                }
            ),
            function (error) {
                console.log("Error", error)
            };

            return false
    }
