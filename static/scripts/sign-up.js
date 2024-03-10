function validateForm() {
    var username = document.getElementById("username").value;
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    var passwordVerify = document.getElementById("password_verify").value;

    // Check if any field is empty
    if (username === "" || email === "" || password === "" || passwordVerify === "") {
        alert("Please fill out all fields.");
        return false;
    }

    // Check if email is valid
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        alert("Please enter a valid email address.");
        return false;
    }

    // Check if passwords match
    if (password !== passwordVerify) {
        alert("Passwords do not match.");
        return false;
    }

    // If all checks pass, return true to submit the form
    return true;
}
     function register() {
        if(validateForm()){
            var username = document.getElementById("username").value;
            var email = document.getElementById("email").value;
            var password = document.getElementById("password").value;
            localStorage.setItem('rememberedUsername', username);
            localStorage.setItem('rememberedPassword', password);
            $.ajax({
                url: '/create_account',
                type: 'GET',
                data: {username: username, password: password, email: email},
                success: function(response) {
                    if(response["valid"] === "True"){
                        var params = {
                          username: username,
                          password: password,
                          email: email
                        };
                        var queryString = $.param(params);
                        targetURL = `/profile`
                        var finalURL = targetURL + '?' + queryString;
                        window.location.replace(finalURL)
                    }
                    else if(response["valid"] === "email_error"){
                        alert("This email is already in use. Please try another email.");
                    }
                    else{
                        alert("There was an internal server error while creating your account. Please try again in a few moments.");
                    }
                },
                error: function(error) {
                    alert("There was an internal server error while creating your account. Please try again in a few moments.");
                }
            });
        }
     }