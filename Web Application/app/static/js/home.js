var x = get_initials(); 

function get_initials() {
  var str = "Pramath Ramesh";
  var words = str.split(" ");
  var initials = words[0].charAt(0) + words[1].charAt(0);
  return initials;   
}  
document.getElementById("demo").innerHTML = "<p data-letters="+x+"> My Name</p>";