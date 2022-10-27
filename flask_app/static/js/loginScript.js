const loginBtn = document.querySelector('.loginBtn');
const registerBtn = document.querySelector('.registerBtn');
const formBox = document.querySelector('.formBox');
const loginBody = document.querySelector('.loginBody');


registerBtn.onclick = function () {
    formBox.classList.add('active')
    loginBody.classList.add('active')
}

loginBtn.onclick = function () {
    formBox.classList.remove('active')
    loginBody.classList.remove('active')
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