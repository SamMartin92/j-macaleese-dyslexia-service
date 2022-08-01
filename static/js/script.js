const contactForm = document.getElementById("contact-form");
const successMessage = document.getElementById("success-message")


const guardianCheckBox = document.getElementById("is_guardian")
const bookingSubmit = document.getElementById("booking-submit")


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

guardianCheckBox.addEventListener("click", function () {
    let childNameInput = document.getElementById("childs_name");
    childNameInput.toggleAttribute("disabled");
});


bookingSubmit.addEventListener("click", function () {
    let dateInput = document.getElementById("id_booking_date")
    let modalContent = document.querySelector(".modal-content")
    

    if (dateInput.value == "") {
        modalContent.innerHTML = `<div class="modal-header">
        <h5 class="modal-title" id="staticBackdropLabel">Booking Unsuccessful</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
            <p>Please select a date</p>
        </div>
        <div class="modal-footer">
            <button type="button" id="close-modal-btn" class="btn btn-secondary" data-bs-dismiss="modal">Ok!</button>
        </div>`

        let closeModalBtn = document.getElementById("close-modal-btn")

        closeModalBtn.addEventListener("click", function () {
            modalContent.innerHTML = `<div class="modal-header">
            <h5 class="modal-title" id="staticBackdropLabel">Booking Submitted</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
            <p>Thank you for submitting your booking request!</p>
            <p>Booking available to view in pending bookings. Please contact Jennie to us to arrange
                payment if any payments or outstanding or your booking may not be accepted.</p>
            <li class="ms-3"><i class="fa-solid fa-phone"> </i>+353 86 087 3335</li>
            <li class="ms-3"><i class="fa-solid fa-envelope"> </i>jenniemcaleese@hotmail.com</li>
        </div>
        <div class="modal-footer">
            <button type="button" id="close-modal-btn" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="submit" class="btn btn-primary">I understand</button>
        </div>`
        });
    }

})