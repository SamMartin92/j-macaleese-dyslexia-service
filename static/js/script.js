const contactForm = document.getElementById("conact-form");
const successMessage = document.getElementById("success-message")

const guardianCheckBox = document.getElementById("is_guardian")

guardianCheckBox.addEventListener("click", function(){
    let childNameInput = document.getElementById("childs_name");
    childNameInput.toggleAttribute("disabled");
  });

function sendMail(contactForm) {
        emailjs.send("service_f794snj", "template_3as9mrv", {
            form_name: contactForm.name.value,
            form_email: contactForm.emailaddress.value,
            form_phone: contactForm.phone.value,
            message: contactForm.message.value
        })
            .then(
                function (response) {
                    console.log(response);
                    contactForm.classList.add("hidden");
                    successMessage.classList.remove("hidden");
                }
            ),
            function (error) {
                console.log("Error", error)
            };

            return false
    }


    function childsNameDisableToggle() {
        

        
    }