function loginToRegister() {
  var x = document.getElementById("login-panel");
  var y = document.getElementById("register-panel");
  if (x.style.display === "none") {
    x.style.display = "block";
    y.style.display = "none";
    document.getElementById("login-reg-section").style.height=60+"%";
  } else {
  	x.style.display = "none";
    y.style.display = "block";
    document.getElementById("login-reg-section").style.height=80+"%";
  }
}
