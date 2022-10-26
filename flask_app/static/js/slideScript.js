// Login/Registration Slider

const signinBtn = document.querySelector('.signinBtn');
const signupBtn = document.querySelector('.signupBtn');
const formBx = document.querySelector('.formBx');
const slideBody = document.querySelector('.slideBody');


signupBtn.onclick = function () {
    formBx.classList.add('active')
    slideBody.classList.add('active')
}

signinBtn.onclick = function () {
    formBx.classList.remove('active')
    slideBody.classList.remove('active')
}

function added() {
    var change = document.getElementById("added");
    if (change.innerHTML == "Add to My Picks") {
        change.innerHTML = "Added";
    }
    else {
        change.innerHTML = "Add to My Picks"
    }
}

Email.send({
    Host: "smtp.yourisp.com",
    Username: "username",
    Password: "password",
    To: 'them@website.com',
    From: "you@isp.com",
    Subject: "Let's Pick Somewhere to Eat!",
    Body: "Here's the code to join my room: <enter code here>. And the link would be here: <link>."
}).then(
    message => alert(message)
);