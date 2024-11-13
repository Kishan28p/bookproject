function ShowAlert(){
var username=document.getElementById('username').value;
var firstname=document.getElementById('firstname').value;
var lastname=document.getElementById('lastname').value;
var email=document.getElementById('email').value;
var password=document.getElementById('password').value;
var password1=document.getElementById('password1').value;

if (!username || !firstname || !lastname || !email || !password || !password1){
alert("Please fill out the required field");
}
else{
alert("Registration Successful");
}

}