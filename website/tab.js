function $_GET(param) {
  var vars = {};
  window.location.href.replace( location.hash, '' ).replace(
    /[?&]+([^=&]+)=?([^&]*)?/gi, // regexp
    function( m, key, value ) { // callback
      vars[key] = value !== undefined ? value : '';
    }
  );

  if ( param ) {
    return vars[param] ? vars[param] : null;
  }
  return vars;
}
function time(timestamp){
  var date = new Date(timestamp*1000);
  // Hours part from the timestamp
  var hours = date.getHours();
  // Minutes part from the timestamp
  var minutes = "0" + date.getMinutes();
  // Seconds part from the timestamp
  var seconds = "0" + date.getSeconds();

  // Will display time in 10:30:23 format
  var formattedTime = hours + ':' + minutes.substr(-2) + ':' + seconds.substr(-2);
  return formattedTime;

}


function genTab(json){

  texttab="";
  console.log(json["patient info"][0][0])
  subtitle= document.querySelector(".lead")
  subtitle.innerHTML=json["patient info"][0];
  console.log(json["patient statuses"][0][0]);
  for (const item in json["patient statuses"]){
    tab = document.querySelector('#tab')
    console.log(json["patient statuses"][item][0]);
    texttab+="<tr><th scope=\"row\"> </th><td>" + time(json["patient statuses"][item][1]) + "</td>";
    if(json["patient statuses"][item][3]==="pending"){
      console.log("teo")
      console.log(json["rank"][0][0])
      texttab+="<td>" + json["rank"][0][0] + "</td>";
    }
    else{
      texttab+="<td> Finished </td>";
    }
    texttab+="<td>" + json["patient statuses"][item][2] + "</td>";
    texttab+="<td>" + json["patient statuses"][item][3] + "</td>";

      /*<td>Otto</td>
      <td>@mdo</td>
    </tr>;*/

    tab.innerHTML=texttab;
  }
}
//const array = url.split('/');
//const lastsegment = array[array.length-1];
user=$_GET("user")
fetch("http://localhost:5000/patients/"+user)
.then(response => response.json())
.then(json => genTab(json))
