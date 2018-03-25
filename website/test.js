function displayMeteo(json){
  for(i=0; i<5 ;i++){
  var node = document.createElement("LI");
  var textnode = document.createTextNode("Water");         // Create a text node

    let test="fcst_day_"+i;
  let date = json[test].date;
  let Tmin = json[test].tmin;
  let Tmax = json[test].tmax;

  //data.textContent="le " + date + " il fait minimum " + Tmin + " et max " + Tmax ;
  textnode.textContent ="le " + date + " il fait minimum " + Tmin + " et max " + Tmax ;
  node.appendChild(textnode);                              // Append the text to <li>
  document.getElementById("data").appendChild(node);
  }
}

function onClick(){
  const text= document.querySelector('input');
  //console.log(text.value);
  fetch("https://www.prevision-meteo.ch/services/json/"+text.value)
    .then(response => response.json())
    .then(json => {
      return new Promise((resolve, reject) => {
        if (json.errors)
          reject(json.errors[0]);
        else
          resolve(json);
      })
    })
    .then(json => displayMeteo(json))
    .catch(err => console.log(err));
  };

const data= document.querySelector('#data');

const button = document.querySelector('button');
let test;
button.addEventListener('click',onClick);




//const text= document.querySelector('text');
//console.log(text);
