flag = 1;
function form_validation(){
    var name = document.getElementById('_fullname').value;
    var letters = /^[a-zA-Z]*$/;
    console.log(name);
    var address = document.getElementById('_address')
    console.log(address);
    var mobiles = document.getElementById('_number').value;
    var text = /^\d{10}$/;
    console.log(mobiles);
    var email = document.getElementById('_username').value;
    var re = /\S+@\S+\.\S+/;
    console.log(email);
    var password = document.getElementById('_password').value;
    var pass = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
    console.log(password);
    var cpassword = document.getElementById('_confirmpassword').value;
    console.log(cpassword);
    // var btns = document.getElementById('_btn').value;
    // console.log(btns);
    // empty block
    if(name == ""){
        name_error.innerHTML = 'please enter your name';
        name_error.style.display = "block";
        name_error.style.color = "red";
        flag = 0;
    }
    // length
    else if(name.length < 3){
        name_error.innerHTML = 'name must contain at least 3 letters';
        name_error.style.display = "block";
        flag = 0;
    }
    //special character
    else if(!name.match(letters)){
        name_error.innerHTML = 'Special characters not allowed';
        name_error.style.display = "block";
        flag = 0;
    }
    else{
        name_error.style.display = "none";
        flag = 1;
    }
    if(address == ""){
        address_error.innerHTML = 'please enter your address';
        address_error.style.display = "block";
        address_error.style.color = "red";
        flag = 0;
    }
    else{
        address_error.style.display = "none";
        flag = 1;
    }
    if(mobiles ==""){
        phonenumber_error.innerHTML = 'Please enter the mobile number';
        phonenumber_error.style.display = "block";
        phonenumber_error.style.color = "red";
        flag = 0;
    }
    else if(!mobiles.match(text)){
        phonenumber_error.innerHTML = 'enter valid number';
        phonenumber_error.style.display = "block";
        phonenumber_error.style.color = "red";
        flag = 0;
    }
    else{
        phonenumber_error.style.display = "none";
        flag = 1;
    }
    if(email == ""){
        username_error.innerHTML = 'please enter your email';
        username_error.style.display = "block";
        username_error.style.color = "red";
        flag =0;
    }
    else if(!email.match(re)){
        username_error.innerHTML = 'enter valid email';
        username_error.style.display = "block";
        username_error.style.color = "red";
        flag = 0;
    }
    else{
        username_error.style.display = "none";
        flag = 1;
    }
    
    if(password == ""){
        password_error.innerHTML = 'please enter the password';
        password_error.style.display = "block";
        password_error.style.color = "red";
        flag = 0;
    }
    else if(!password.match(pass)){
        password_error.innerHTML = 'Must contain atleast one number, one uppercase,one lowercase,one special character and at least 8 or more character';
        password_error.style.display = "block";
        password_error.style.color = "red";
        flag = 0;
    }
    else{
        password_error.style.display = "none";
        flag = 1;
    }
    if(cpassword == ""){
        confirmpassword_error.innerHTML = 'please confirm the password';
        confirmpassword_error.style.display = "block";
        confirmpassword_error.style.color = "red";
        flag = 0;
    }
    else if(password!= cpassword){
        confirmpassword_error.innerHTML = 'password not match';
        confirmpassword_error.style.display = "block";
        confirmpassword_error.style.color = "red";
        flag = 0;
    }
    else{
        confirmpassword_error.style.display = "none";
        // window.location.href = 'loginpage.html';
        flag = 1;

    }
    if(flag == 0){
        return false;
    }
    else{
        return true;
    }
    // if(btns.status === 'ok'){
    //     alert('success');
    //     window.location.href ="loginpage.html";
    //     return true;
    // }
    // else{
    //     return false;
    // }
}