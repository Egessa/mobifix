function validateForm() {
  var name = document.forms["myForm"]["fname"].value;
  var lname = document.forms["myForm"]["lname"].value;
  var mail = document.forms["myForm"]["email"].value;
  var telephone = document.forms["myForm"]["telephone"].value;
  var message = document.forms["myForm"]["message"].value;
}
if (name == "")
{
  alert("Input First name");
  return false;
}

if (lname == "")
{
  alert("Input Last Name");
  return false;
}

if (mail == "")
{
  alert("Input Email");
  return false;
}

if (telephone == "")
{
  alert("Input Phone Number");
  return false;
}


if (message == "") {
  alert("Input Message");
  return false;
}

function sendMessage()
{
  alert("works");
  return false;
}
