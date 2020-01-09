function validateForm() {
  var name = document.forms["myForm"]["fname"].value;
  var lname = document.forms["myForm"]["lname"].value;
  var mail = document.forms["myForm"]["email"].value;
  var subject = document.forms["myForm"]["subject"].value;
  var message = document.forms["myForm"]["message"].value;
}
  if (name == "") {
    alert("Input First name");
    return false;
  }

    if (lname == "") {
      alert("Input Last Name");
      return false;
    }

    if (mail == "") {
      alert("Input Email");
      return false;
    }

    if (message == "") {
      alert("Input Message");
      return false;
    }

function send(){
  alert("works");
}
